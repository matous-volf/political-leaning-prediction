import os
from abc import ABC, abstractmethod
from copy import deepcopy
from os import PathLike
from pathlib import Path
from typing import (
    Callable,
    Dict,
    Generator,
    Iterable,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
)

import evaluate
import matplotlib.pyplot as plt
import numpy as np
import torch
from datasets import Dataset, IterableDataset
from pandas import DataFrame
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
from sklearn.utils import compute_class_weight
from tqdm.notebook import tqdm
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    DataCollator,
    EvalPrediction,
    IntervalStrategy,
    PreTrainedModel,
    PreTrainedTokenizerBase,
    Trainer,
    TrainerCallback,
    TrainingArguments,
)

from utils.base_directory import base_directory

T = TypeVar("T")

available_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

DATASET_BENCHMARK_MODEL_NAMES = sorted(
    [
        "google-bert/bert-base-cased",
        "FacebookAI/roberta-base",
        "launch/POLITICS",
    ],
    key=lambda model_name: model_name.split("/")[-1],
)
DATASET_BENCHMARK_MODELS_MAX_LENGTH = 512


class Model(ABC):
    def __init__(
        self,
        tokenizer,
        model,
        label_count: int,
        model_max_length: int | None = None,
    ) -> None:
        model.to(available_device)
        self.tokenizer = tokenizer
        self.model = model
        self.label_count = label_count
        self.model_max_length = (
            self.tokenizer.model_max_length
            if model_max_length is None
            else model_max_length
        )
        self.name = type(self).__name__

    @abstractmethod
    def predict(self, text: str, truncate_tokens: bool = True) -> int:
        pass

    def get_tokens(
        self,
        text: str,
        truncate_tokens: bool,
        return_tensors: str | None = "pt",
    ):
        tokenizer_args = {
            "max_length": self.model_max_length,
            "truncation": truncate_tokens,
        }

        if return_tensors:
            tokenizer_args["return_tensors"] = return_tensors

        return self.tokenizer(text, **tokenizer_args).to(available_device)

    def get_output(self, tokens):
        with torch.no_grad():
            return self.model(**tokens)


class PoliticalnessModel(Model, ABC):
    def __init__(
        self,
        tokenizer,
        model,
        model_max_length: int | None = None,
    ):
        super().__init__(
            tokenizer,
            model,
            2,
            model_max_length,
        )


class CustomPoliticalnessModel(PoliticalnessModel):
    def __init__(
        self,
        path: PathLike[str],
        model_name: str,
        tokenizer_name: str,
        model_max_length: int,
    ) -> None:
        model = AutoModelForSequenceClassification.from_pretrained(
            base_directory / "models" / path / model_name
        )
        super().__init__(
            AutoTokenizer.from_pretrained(tokenizer_name),
            model,
            model_max_length,
        )
        self.name = str(Path(path, model_name))

    def predict(self, text: str, truncate_tokens: bool = True) -> int:
        tokens = self.get_tokens(text, truncate_tokens)
        output = self.get_output(tokens)
        return torch.argmax(output.logits, dim=-1).item()


class LeaningModel(Model, ABC):
    def __init__(
        self,
        tokenizer,
        model,
        model_max_length: int | None = None,
        supports_center_leaning_class: bool | None = None,
    ):
        self.supports_center_leaning_class = (
            model.config.num_labels >= 3
            if supports_center_leaning_class is None
            else supports_center_leaning_class
        )
        super().__init__(
            tokenizer,
            model,
            3 if self.supports_center_leaning_class else 2,
            model_max_length,
        )


class CustomLeaningModel(LeaningModel):
    def __init__(
        self,
        path: PathLike[str],
        model_name: str,
        tokenizer_name: str,
        model_max_length: int,
    ) -> None:
        model = AutoModelForSequenceClassification.from_pretrained(
            base_directory / "models" / path / model_name
        )
        super().__init__(
            AutoTokenizer.from_pretrained(tokenizer_name),
            model,
            model_max_length,
        )
        self.name = str(Path(path, model_name))

    def predict(self, text: str, truncate_tokens: bool = True) -> int:
        tokens = self.get_tokens(text, truncate_tokens)
        output = self.get_output(tokens)
        return torch.argmax(output.logits, dim=-1).item()


def get_custom_models(path: PathLike[str], cls: Type[T]) -> Generator[T, None, None]:
    for model, tokenizer_name in zip(
        sorted(os.listdir(base_directory / "models" / path)),
        DATASET_BENCHMARK_MODEL_NAMES,
    ):
        for dataset in sorted(os.listdir(base_directory / "models" / path / model)):
            yield cls(
                path,
                f"{model}/{dataset}",
                tokenizer_name,
                DATASET_BENCHMARK_MODELS_MAX_LENGTH,
            )


def get_custom_politicalness_models(path: PathLike[str]):
    return get_custom_models(path, CustomPoliticalnessModel)


def get_custom_leaning_models(path: PathLike[str]):
    return get_custom_models(path, CustomLeaningModel)


class CustomTrainer(Trainer):
    def __init__(
        self,
        class_weights: torch.Tensor,
        model: Union[PreTrainedModel, torch.nn.Module] = None,
        args: TrainingArguments = None,
        data_collator: Optional[DataCollator] = None,
        train_dataset: Optional[Union[Dataset, IterableDataset, "Dataset"]] = None,
        eval_dataset: Optional[Union[Dataset, Dict[str, Dataset], "Dataset"]] = None,
        tokenizer: Optional[PreTrainedTokenizerBase] = None,
        model_init: Optional[Callable[[], PreTrainedModel]] = None,
        compute_loss_func: Optional[Callable] = None,
        compute_metrics: Optional[Callable[[EvalPrediction], Dict]] = None,
        callbacks: Optional[List[TrainerCallback]] = None,
        optimizers: Tuple[torch.optim.Optimizer, torch.optim.lr_scheduler.LambdaLR] = (
            None,
            None,
        ),
        preprocess_logits_for_metrics: Optional[
            Callable[[torch.Tensor, torch.Tensor], torch.Tensor]
        ] = None,
    ):
        super().__init__(
            model,
            args,
            data_collator,
            train_dataset,
            eval_dataset,
            tokenizer,
            model_init,
            compute_loss_func,
            compute_metrics,
            callbacks,
            optimizers,
            preprocess_logits_for_metrics,
        )
        self.class_weights = class_weights

    def compute_loss(
        self, model, inputs, return_outputs=False, num_items_in_batch=None
    ):
        labels = inputs.get("labels")
        outputs = model(**inputs)
        logits = outputs.get("logits")
        loss_fct = torch.nn.CrossEntropyLoss(weight=self.class_weights).to(
            available_device
        )
        loss = loss_fct(logits.view(-1, self.model.config.num_labels), labels.view(-1))
        return (loss, outputs) if return_outputs else loss


def finetune_models(
    output_path: PathLike,
    train_datasets: Iterable[Dataset],
    eval_datasets: Iterable[Dataset],
    eval_strategy: IntervalStrategy,
    training_seed: int,
    data_seed: int,
    learning_rate: float = 5e-5,
):
    def tokenize_dataset(dataset: Dataset, tokenizer) -> Dataset:
        return dataset.map(
            lambda batch: tokenizer(
                batch["text"],
                max_length=DATASET_BENCHMARK_MODELS_MAX_LENGTH,
                truncation=True,
                padding="max_length",
            ),
            batched=True,
        )

    def compute_metrics(eval_pred):
        logits, references = eval_pred
        predictions = np.argmax(logits, axis=-1)
        return compute_metric_result(None, predictions, references).__dict__

    for model_name in DATASET_BENCHMARK_MODEL_NAMES:
        print(f"fine-tuning {model_name} into {output_path}:")

        tokenizer = AutoTokenizer.from_pretrained(model_name)
        for train_dataset, eval_dataset in zip(train_datasets, eval_datasets):
            print(f"  {train_dataset.info.dataset_name}")
            output_directory = (
                base_directory
                / "models"
                / output_path
                / model_name.split("/")[-1]
                / train_dataset.info.dataset_name
            )

            train_dataset_tokenized = tokenize_dataset(train_dataset, tokenizer)
            eval_dataset_tokenized = tokenize_dataset(eval_dataset, tokenizer)

            training_arguments = TrainingArguments(
                learning_rate=learning_rate,
                auto_find_batch_size=True,
                eval_strategy=(
                    eval_strategy if len(eval_dataset) > 0 else IntervalStrategy.NO
                ),
                save_strategy=IntervalStrategy.NO,
                output_dir=output_directory,
                seed=training_seed,
                data_seed=data_seed,
            )
            trainer = CustomTrainer(
                model_init=lambda: AutoModelForSequenceClassification.from_pretrained(
                    model_name,
                    num_labels=len(train_dataset.unique("label")),
                ),
                args=training_arguments,
                train_dataset=train_dataset_tokenized,
                eval_dataset=eval_dataset_tokenized,
                compute_metrics=compute_metrics,
                class_weights=torch.from_numpy(
                    compute_class_weight(
                        class_weight="balanced",
                        classes=np.sort(train_dataset.unique("label")),
                        y=train_dataset["label"],
                    ).astype(np.float32)
                ),
            )
            trainer.train()
            trainer.save_model(output_directory)


class MetricResult:
    def __init__(
        self,
        count,
        accuracy,
        f1,
        precision,
        recall,
        confusion_matrix,
    ):
        self.count = count
        self.accuracy = accuracy
        self.f1 = f1
        self.precision = precision
        self.recall = recall
        self.confusion_matrix = confusion_matrix


def mean_without_training_datasets(df):
    df_mean = deepcopy(df)
    for index in df_mean.index:
        for column in df_mean.columns:
            # Exclude the dataset the model has been trained on from the calculation of the average.
            if index.split("/")[-1] == column:
                df_mean.loc[index, column] = np.nan
    return df_mean.mean(axis=1, skipna=True).round(3)


class MetricResults:
    def __init__(
        self,
        results: List[List[MetricResult]],
        model_names: List[str],
        dataset_names: List[str],
    ):
        self.count = DataFrame(
            list(
                map(
                    lambda row: list(
                        map(lambda col: f"{col.count[0]} / {col.count[1]}", row)
                    ),
                    results,
                )
            ),
            index=model_names,
            columns=dataset_names,
        )

        self.accuracy = DataFrame(
            list(map(lambda row: list(map(lambda col: col.accuracy, row)), results)),
            index=model_names,
            columns=dataset_names,
        )
        self.accuracy["average"] = mean_without_training_datasets(self.accuracy)

        self.f1 = DataFrame(
            list(map(lambda row: list(map(lambda col: col.f1, row)), results)),
            index=model_names,
            columns=dataset_names,
        )
        self.f1["average"] = mean_without_training_datasets(self.f1)

        self.precision = DataFrame(
            list(map(lambda row: list(map(lambda col: col.precision, row)), results)),
            index=model_names,
            columns=dataset_names,
        )
        self.precision["average"] = mean_without_training_datasets(self.precision)

        self.recall = DataFrame(
            list(map(lambda row: list(map(lambda col: col.recall, row)), results)),
            index=model_names,
            columns=dataset_names,
        )
        self.recall["average"] = mean_without_training_datasets(self.recall)

        self.confusion_matrix = DataFrame(
            list(
                map(
                    lambda row: list(map(lambda col: col.confusion_matrix, row)),
                    results,
                )
            ),
            index=model_names,
            columns=dataset_names,
        )

    def save_confusion_matrix_images(
        self, path: PathLike[str], label_mapping: dict[str, int]
    ):
        for index, row in self.confusion_matrix.iterrows():
            for col in self.confusion_matrix.columns:
                display = ConfusionMatrixDisplay(
                    confusion_matrix=row[col],
                    display_labels=list(label_mapping.keys()),
                )
                subdirectory = path / index
                subdirectory.mkdir(parents=True, exist_ok=True)
                figure = display.plot().figure_
                figure.savefig(subdirectory / f"{col}.svg", format="svg")
                plt.close(figure)


def evaluate_models(
    get_models: Callable[[], Generator[Model, None, None]],
    datasets: List[Dataset],
) -> MetricResults:
    results = []

    for model in get_models():
        print(f"evaluating {model.name} on:")

        results.append([])

        for dataset in datasets:
            print(f"  {dataset.info.dataset_name}")

            predictions = []
            for text in tqdm(dataset["text"]):
                predictions.append(model.predict(text))

            results[-1].append(
                compute_metric_result(
                    range(model.label_count), predictions, dataset["label"]
                )
            )

    return MetricResults(
        results,
        list(map(lambda model: model.name, get_models())),
        list(map(lambda dataset: dataset.info.dataset_name, datasets)),
    )


def compute_metric_result(labels, predictions, references):
    metric_accuracy = evaluate.load("accuracy")
    metric_f1 = evaluate.load("f1")
    metric_precision = evaluate.load("precision")
    metric_recall = evaluate.load("recall")

    accuracy = metric_accuracy.compute(predictions=predictions, references=references)
    f1 = metric_f1.compute(
        predictions=predictions, references=references, average="weighted"
    )
    precision = metric_precision.compute(
        predictions=predictions, references=references, average="weighted"
    )
    recall = metric_recall.compute(
        predictions=predictions, references=references, average="weighted"
    )

    return MetricResult(
        (round(len(predictions) * accuracy["accuracy"]), len(predictions)),
        round(accuracy["accuracy"], 3),
        round(f1["f1"], 3),
        round(precision["precision"], 3),
        round(recall["recall"], 3),
        confusion_matrix(references, predictions, labels=labels),
    )

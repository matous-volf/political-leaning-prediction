import os
from abc import ABC, abstractmethod
from os import PathLike
from pathlib import Path
from typing import (
    Callable,
    Generator,
    Iterable,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    Dict,
)

import numpy as np
import torch
from datasets import Dataset, IterableDataset
from evaluate import EvaluationModule
from pandas import DataFrame
from sklearn.metrics import accuracy_score
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
        model_max_length: int | None = None,
    ) -> None:
        model.to(available_device)
        self.tokenizer = tokenizer
        self.model = model
        self.model_max_length = (
            self.tokenizer.model_max_length
            if model_max_length is None
            else model_max_length
        )
        self.name = type(self).__name__

    @abstractmethod
    def predict(self, text: str, truncate_tokens: bool) -> int:
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


class CustomPoliticalnessModel(Model):
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

    def predict(self, text: str, truncate_tokens: bool) -> int:
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
        super().__init__(tokenizer, model, model_max_length)
        self.supports_center_leaning_class = (
            model.config.num_labels >= 3
            if supports_center_leaning_class is None
            else supports_center_leaning_class
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

    def predict(self, text: str, truncate_tokens: bool) -> int:
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
    metric: EvaluationModule,
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
        logits, labels = eval_pred
        predictions = np.argmax(logits, axis=-1)
        return metric.compute(predictions=predictions, references=labels)

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
                class_weights=compute_class_weight(
                    class_weight="balanced",
                    classes=np.sort(train_dataset.unique("label")),
                    y=train_dataset["label"],
                ),
            )
            trainer.train()
            trainer.save_model(output_directory)


def evaluate_models(
    get_models: Callable[[], Generator[Model, None, None]],
    datasets: List[Dataset],
    truncate_tokens: bool,
):
    accuracy_results = []

    for model in get_models():
        print(f"evaluating {model.name} on:")

        accuracy_results.append([])
        total_predictions_count = 0
        total_correct_predictions_count = 0

        for dataset in datasets:
            print(f"  {dataset.info.dataset_name}")

            predictions = []
            for text in tqdm(dataset["text"]):
                try:
                    predictions.append(model.predict(text, truncate_tokens))
                except RuntimeError:
                    if truncate_tokens:
                        raise
                    predictions.append(None)

            valid_indices = [
                i for i, prediction in enumerate(predictions) if prediction is not None
            ]
            predictions = list([predictions[i] for i in valid_indices])
            accuracy = (
                accuracy_score(
                    dataset.to_pandas()["label"].iloc[valid_indices].tolist(),
                    predictions,
                )
                if len(predictions) > 0
                else 0
            )

            predictions_count = len(valid_indices)
            correct_predictions_count = predictions_count * accuracy

            accuracy_results[-1].append(
                f"{correct_predictions_count:.0f} / {predictions_count} ({accuracy * 100:.0f} %)"
            )
            # Skip the evaluation of the models trained on the same dataset for the calculation of
            # the average.
            if model.name.split("/")[-1] != dataset.info.dataset_name:
                total_predictions_count += predictions_count
                total_correct_predictions_count += correct_predictions_count

        average_accuracy = (
            total_correct_predictions_count / total_predictions_count
            if total_predictions_count > 0
            else 0
        )
        accuracy_results[-1].append(
            f"{total_correct_predictions_count:.0f} / {total_predictions_count} ({average_accuracy * 100:.0f} %)"
        )

    return DataFrame(
        accuracy_results,
        index=list(map(lambda model: model.name, get_models())),
        columns=list(map(lambda dataset: dataset.info.dataset_name, datasets))
        + ["average"],
    )

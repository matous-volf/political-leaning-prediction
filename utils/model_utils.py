import os
from abc import ABC, abstractmethod
from enum import Enum
from os import PathLike
from typing import Generator, Iterable

import numpy as np
import torch
from datasets import Dataset
from evaluate import EvaluationModule
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    BertTokenizer,
    DistilBertForSequenceClassification,
    IntervalStrategy,
    RobertaTokenizer,
    Trainer,
    TrainingArguments,
    pipeline,
)

from utils.base_directory import BASE_DIRECTORY

POLITICAL_LEANING_WITH_CENTER_LABEL_MAPPING = {"left": 0, "center": 1, "right": 2}
POLITICAL_LEANING_NO_CENTER_LABEL_MAPPING = {"left": 0, "right": 1}

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

CUSTOM_MODELS_MAX_LENGTH = 512
DATASET_BENCHMARK_MODEL_NAMES = sorted(
    [
        "google-bert/bert-base-cased",
        "FacebookAI/roberta-base",
        "launch/POLITICS",
    ],
    key=lambda model_name: model_name.split("/")[-1],
)


class Leaning(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class Model(ABC):
    def __init__(
        self,
        tokenizer,
        model,
        model_max_length: int | None = None,
        supports_center_leaning: bool | None = None,
    ) -> None:
        model.to(DEVICE)
        self.tokenizer = tokenizer
        self.model = model
        self.model_max_length = (
            self.tokenizer.model_max_length
            if model_max_length is None
            else model_max_length
        )
        self.name = type(self).__name__
        self.supports_center_leaning = (
            model.config.num_labels >= 3
            if supports_center_leaning is None
            else supports_center_leaning
        )

    @abstractmethod
    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        pass

    def get_tokens(
        self,
        article_body: str,
        truncate_tokens: bool,
        return_tensors: str | None = "pt",
    ):
        tokenizer_args = {
            "max_length": self.model_max_length,
            "truncation": truncate_tokens,
        }

        if return_tensors:
            tokenizer_args["return_tensors"] = return_tensors

        return self.tokenizer(article_body, **tokenizer_args).to(DEVICE)

    def get_output(self, tokens):
        with torch.no_grad():
            return self.model(**tokens)


class PoliticalBiasBert(Model):
    def __init__(self) -> None:
        super().__init__(
            AutoTokenizer.from_pretrained(
                "bert-base-cased",
                code_revision="cd5ef92a9fb2f889e972770a36d4ed042daf221e",
            ),
            AutoModelForSequenceClassification.from_pretrained(
                "bucketresearch/politicalBiasBERT",
                code_revision="fd40172e075c046ec5f47bae270d17c2b91cf847",
            ),
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        tokens = self.get_tokens(article_body, truncate_tokens)
        output = self.get_output(tokens)
        return [Leaning.LEFT, Leaning.CENTER, Leaning.RIGHT][
            torch.argmax(output.logits, dim=-1)
        ]


class PoliticalBiasPredictionAllsidesDeberta(Model):
    def __init__(self) -> None:
        super().__init__(
            AutoTokenizer.from_pretrained(
                "premsa/political-bias-prediction-allsides-DeBERTa",
                code_revision="e28374fcbb66f6ce21faf224fa3bdcb6d054ec46",
            ),
            AutoModelForSequenceClassification.from_pretrained(
                "premsa/political-bias-prediction-allsides-DeBERTa",
                code_revision="e28374fcbb66f6ce21faf224fa3bdcb6d054ec46",
            ),
            512,
        )
        self.pipe = pipeline(
            "text-classification",
            model=self.model,
            tokenizer=self.tokenizer,
            device=DEVICE,
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        output = self.pipe(article_body)
        return {
            "LABEL_0": Leaning.LEFT,
            "LABEL_1": Leaning.CENTER,
            "LABEL_2": Leaning.RIGHT,
        }[output[0]["label"]]


class DistilBertPoliticalBias(Model):
    def __init__(self) -> None:
        super().__init__(
            RobertaTokenizer.from_pretrained(
                "cajcodes/DistilBERT-PoliticalBias",
                revision="ebfc38d3fac856b86fda2e08357da171b53896a2",
            ),
            DistilBertForSequenceClassification.from_pretrained(
                "cajcodes/DistilBERT-PoliticalBias",
                revision="ebfc38d3fac856b86fda2e08357da171b53896a2",
            ),
            512,
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        article_body = article_body.replace("\n", "").replace("``", '"')
        tokens = self.get_tokens(article_body, truncate_tokens)
        unk_token_id = self.tokenizer.convert_tokens_to_ids(self.tokenizer.unk_token)
        tokens["input_ids"][
            tokens["input_ids"] >= self.model.config.vocab_size
        ] = unk_token_id
        output = self.get_output(tokens)
        return [
            Leaning.RIGHT,
            Leaning.RIGHT,
            Leaning.CENTER,
            Leaning.LEFT,
            Leaning.LEFT,
        ][torch.argmax(output.logits, dim=-1)]


class BertPoliticalBiasFinetune(Model):
    def __init__(self) -> None:
        super().__init__(
            BertTokenizer.from_pretrained(
                "bert-base-uncased", revision="86b5e0934494bd15c9632b12f734a8a67f723594"
            ),
            AutoModelForSequenceClassification.from_pretrained(
                "jhonalevc1995/BERT-political_bias-finetune",
                code_revision="7ceb614323352d05051d13d2d60f89d8a4595dc5",
            ),
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        tokens = self.get_tokens(article_body, truncate_tokens)
        output = self.get_output(tokens)
        return [Leaning.LEFT, Leaning.RIGHT][torch.argmax(output.logits, dim=-1)]


class DistilBertPoliticalFinetune(Model):
    def __init__(self) -> None:
        super().__init__(
            AutoTokenizer.from_pretrained(
                "harshal-11/DistillBERT-Political-Finetune",
                code_revision="4e218bdcc3c69844bcb8aab1bf218e7942292222",
            ),
            AutoModelForSequenceClassification.from_pretrained(
                "harshal-11/DistillBERT-Political-Finetune",
                code_revision="4e218bdcc3c69844bcb8aab1bf218e7942292222",
            ),
            512,
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        tokens = self.get_tokens(article_body, truncate_tokens)
        output = self.get_output(tokens)
        return [Leaning.LEFT, Leaning.CENTER, Leaning.RIGHT][
            torch.argmax(output.logits, dim=-1)
        ]


class PoliticalIdeologiesRobertaFinetuned(Model):
    def __init__(self) -> None:
        super().__init__(
            AutoTokenizer.from_pretrained(
                "JyotiNayak/political_ideologies_detection_roberta_finetuned",
                code_revision="3e82956ad2f1d0880b8c4d370d513f92a1a3591a",
            ),
            AutoModelForSequenceClassification.from_pretrained(
                "JyotiNayak/political_ideologies_detection_roberta_finetuned",
                code_revision="3e82956ad2f1d0880b8c4d370d513f92a1a3591a",
            ),
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        tokens = self.get_tokens(article_body, truncate_tokens)
        output = self.get_output(tokens)
        return [Leaning.RIGHT, Leaning.LEFT][torch.argmax(output.logits, dim=-1)]


class DebertaPoliticalClassification(Model):
    def __init__(self) -> None:
        super().__init__(
            AutoTokenizer.from_pretrained(
                "oscpalML/DeBERTa-political-classification",
                code_revision="26e16d1c52121d834ff374c07944bc085e1b1656",
            ),
            AutoModelForSequenceClassification.from_pretrained(
                "oscpalML/DeBERTa-political-classification",
                code_revision="26e16d1c52121d834ff374c07944bc085e1b1656",
            ),
            512,
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        tokens = self.get_tokens(article_body, truncate_tokens)
        output = self.get_output(tokens)
        return [Leaning.LEFT, Leaning.RIGHT][torch.argmax(output.logits, dim=-1)]


class DistilBertPoliticalTweets(Model):
    def __init__(self) -> None:
        super().__init__(
            AutoTokenizer.from_pretrained(
                "m-newhauser/distilbert-political-tweets",
                code_revision="b7c4530e8c44cf8dcf448a6e5e5e460df33f83bf",
            ),
            AutoModelForSequenceClassification.from_pretrained(
                "m-newhauser/distilbert-political-tweets",
                code_revision="b7c4530e8c44cf8dcf448a6e5e5e460df33f83bf",
            ),
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        tokens = self.get_tokens(article_body, truncate_tokens)
        output = self.get_output(tokens)
        return [Leaning.RIGHT, Leaning.LEFT][torch.argmax(output.logits, dim=-1)]


class PoliticalDebateLarge(Model):
    def __init__(self) -> None:
        super().__init__(
            AutoTokenizer.from_pretrained(
                "mlburnham/Political_DEBATE_large_v1.0",
                code_revision="3568d6f7bdd58a2792b27699cf88435409318ecf",
            ),
            AutoModelForSequenceClassification.from_pretrained(
                "mlburnham/Political_DEBATE_large_v1.0",
                code_revision="3568d6f7bdd58a2792b27699cf88435409318ecf",
            ),
            supports_center_leaning=True,
        )
        self.pipe = pipeline(
            "zero-shot-classification",
            model=self.model,
            tokenizer=self.tokenizer,
            device=DEVICE,
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        hypothesis_template = "This text supports {} political leaning."
        output = self.pipe(
            article_body,
            ["left", "center", "right"],
            hypothesis_template=hypothesis_template,
            multi_label=False,
        )
        return {"left": Leaning.LEFT, "center": Leaning.CENTER, "right": Leaning.RIGHT}[
            output["labels"][0]
        ]


class CustomModel(Model):
    def __init__(
        self, model_name: str, tokenizer_name: str, model_max_length: int
    ) -> None:
        model = AutoModelForSequenceClassification.from_pretrained(
            BASE_DIRECTORY / "models_custom" / model_name
        )
        super().__init__(
            AutoTokenizer.from_pretrained(tokenizer_name),
            model,
            model_max_length,
        )
        self.name = model_name

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        tokens = self.get_tokens(article_body, truncate_tokens)
        output = self.get_output(tokens)
        labels = (
            [Leaning.LEFT, Leaning.CENTER, Leaning.RIGHT]
            if self.supports_center_leaning
            else [Leaning.LEFT, Leaning.RIGHT]
        )
        return labels[torch.argmax(output.logits, dim=-1)]


def get_existing_models() -> Generator[Model, None, None]:
    # Caution is necessary with creating lists to yield from. The models cannot be instantiated
    # right away, as that would completely undermine the usage of the generator. It could cause the
    # memory to overflow. Instead, models need to be yielded one at a time.
    for model_class in [
        PoliticalBiasBert,
        PoliticalBiasPredictionAllsidesDeberta,
        DistilBertPoliticalBias,
        BertPoliticalBiasFinetune,
        DistilBertPoliticalFinetune,
        PoliticalIdeologiesRobertaFinetuned,
        DebertaPoliticalClassification,
        DistilBertPoliticalTweets,
        PoliticalDebateLarge,
    ]:
        yield model_class()


def get_leave_one_in_dataset_benchmark_models() -> Generator[Model, None, None]:
    return get_dataset_benchmark_models("leave_one_in")


def get_leave_one_out_dataset_benchmark_models() -> Generator[Model, None, None]:
    return get_dataset_benchmark_models("leave_one_out")


def get_dataset_benchmark_models(benchmark_name: str):
    for model, tokenizer_name in zip(
        sorted(
            os.listdir(
                BASE_DIRECTORY / "models_custom" / "dataset_benchmark" / benchmark_name
            )
        ),
        DATASET_BENCHMARK_MODEL_NAMES,
    ):
        for dataset in sorted(
            os.listdir(
                BASE_DIRECTORY
                / "models_custom"
                / "dataset_benchmark"
                / benchmark_name
                / model
            )
        ):
            yield CustomModel(
                f"dataset_benchmark/{benchmark_name}/{model}/{dataset}",
                tokenizer_name,
                CUSTOM_MODELS_MAX_LENGTH,
            )


def finetune_custom_models(
    output_path: PathLike,
    train_datasets: Iterable[Dataset],
    eval_datasets: Iterable[Dataset],
    metric: EvaluationModule,
    eval_strategy: IntervalStrategy,
    training_seed: int,
    data_seed: int,
    learning_rate: float = 5e-5,
):
    def tokenize_dataset(dataset, tokenizer):
        return dataset.map(
            lambda batch: tokenizer(
                batch["body"],
                max_length=CUSTOM_MODELS_MAX_LENGTH,
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
                BASE_DIRECTORY
                / "models_custom"
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
            trainer = Trainer(
                model_init=lambda: AutoModelForSequenceClassification.from_pretrained(
                    model_name,
                    num_labels=len(train_dataset.unique("label")),
                ),
                args=training_arguments,
                train_dataset=train_dataset_tokenized,
                eval_dataset=eval_dataset_tokenized,
                compute_metrics=compute_metrics,
            )
            trainer.train()
            trainer.save_model(output_directory)

import os
from abc import ABC, abstractmethod
from enum import Enum
from typing import Generator

import torch
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    BertTokenizer,
    DistilBertForSequenceClassification,
    RobertaTokenizer,
    pipeline,
)

from utils.base_directory import BASE_DIRECTORY

POLITICAL_LEANING_LABEL_MAPPING = {"left": 0, "center": 1, "right": 2}
POLITICAL_LEANING_NO_CENTER_LABEL_MAPPING = {"left": 0, "right": 1}

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

dataset_benchmark_model_names = [
    "FacebookAI/roberta-base",
    "google-bert/bert-base-cased",
]


class Leaning(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class Model(ABC):
    def __init__(
        self,
        tokenizer,
        model,
        supports_center_leaning: bool,
        model_max_length: int | None = None,
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
        self.supports_center_leaning = supports_center_leaning

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
            AutoTokenizer.from_pretrained("bert-base-cased"),
            AutoModelForSequenceClassification.from_pretrained(
                "bucketresearch/politicalBiasBERT"
            ),
            True,
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
                "premsa/political-bias-prediction-allsides-DeBERTa"
            ),
            AutoModelForSequenceClassification.from_pretrained(
                "premsa/political-bias-prediction-allsides-DeBERTa"
            ),
            True,
            512,
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        pipe = pipeline(
            "text-classification",
            model=self.model,
            tokenizer=self.tokenizer,
            device=DEVICE,
        )
        output = pipe(article_body)
        return {
            "LABEL_0": Leaning.LEFT,
            "LABEL_1": Leaning.CENTER,
            "LABEL_2": Leaning.RIGHT,
        }[output[0]["label"]]


class DistilBertPoliticalBias(Model):
    def __init__(self) -> None:
        super().__init__(
            RobertaTokenizer.from_pretrained("cajcodes/DistilBERT-PoliticalBias"),
            DistilBertForSequenceClassification.from_pretrained(
                "cajcodes/DistilBERT-PoliticalBias"
            ),
            True,
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
            BertTokenizer.from_pretrained("bert-base-uncased"),
            AutoModelForSequenceClassification.from_pretrained(
                "jhonalevc1995/BERT-political_bias-finetune"
            ),
            False,
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        tokens = self.get_tokens(article_body, truncate_tokens)
        output = self.get_output(tokens)
        return [Leaning.LEFT, Leaning.RIGHT][torch.argmax(output.logits, dim=-1)]


class DistilBertPoliticalFinetune(Model):
    def __init__(self) -> None:
        super().__init__(
            AutoTokenizer.from_pretrained("harshal-11/DistillBERT-Political-Finetune"),
            AutoModelForSequenceClassification.from_pretrained(
                "harshal-11/DistillBERT-Political-Finetune"
            ),
            True,
            512,
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        tokens = self.get_tokens(article_body, truncate_tokens)
        output = self.get_output(tokens)
        return [Leaning.LEFT, Leaning.CENTER, Leaning.RIGHT][
            torch.argmax(output.logits, dim=-1)
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
            model.config.num_labels == 3,
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
    yield from [
        PoliticalBiasBert(),
        PoliticalBiasPredictionAllsidesDeberta(),
        DistilBertPoliticalBias(),
        BertPoliticalBiasFinetune(),
        DistilBertPoliticalFinetune(),
    ]


def get_dataset_benchmark_models() -> Generator[Model, None, None]:
    custom_models_max_length = 512

    for model, tokenizer_name in zip(
        os.listdir(BASE_DIRECTORY / "models_custom" / "dataset_benchmark"),
        dataset_benchmark_model_names,
    ):
        for dataset in sorted(
            os.listdir(BASE_DIRECTORY / "models_custom" / "dataset_benchmark" / model)
        ):
            yield CustomModel(
                f"dataset_benchmark/{model}/{dataset}",
                tokenizer_name,
                custom_models_max_length,
            )

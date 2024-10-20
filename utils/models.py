from abc import ABC, abstractmethod
from enum import Enum
from typing import List

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, DistilBertForSequenceClassification, \
    RobertaTokenizer, BertTokenizer, pipeline


class Leaning(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class Model(ABC):
    def __init__(self, tokenizer, model, supports_center_leaning: bool, model_max_length: int | None = None):
        self.tokenizer = tokenizer
        self.model = model
        self.model_max_length = self.tokenizer.model_max_length if model_max_length is None else model_max_length
        self.name = type(self).__name__
        self.supports_center_leaning = supports_center_leaning

    @abstractmethod
    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        pass

    def get_tokens(self, article_body: str, truncate_tokens: bool, return_tensors: str | None = "pt"):
        tokenizer_args = {
            "max_length": self.model_max_length,
            "truncation": truncate_tokens
        }

        if return_tensors:
            tokenizer_args["return_tensors"] = return_tensors

        return self.tokenizer(article_body, **tokenizer_args)

    def get_output(self, tokens):
        with torch.no_grad():
            return self.model(**tokens)


class PoliticalBiasBert(Model):
    def __init__(self):
        super().__init__(
            AutoTokenizer.from_pretrained("bert-base-cased"),
            AutoModelForSequenceClassification.from_pretrained("bucketresearch/politicalBiasBERT"),
            True
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        tokens = self.get_tokens(article_body, truncate_tokens)
        output = self.get_output(tokens)
        return [Leaning.LEFT, Leaning.CENTER, Leaning.RIGHT][torch.argmax(output.logits, dim=-1)]


class PoliticalBiasPredictionAllsidesDeberta(Model):
    def __init__(self):
        super().__init__(
            AutoTokenizer.from_pretrained("premsa/political-bias-prediction-allsides-DeBERTa"),
            AutoModelForSequenceClassification.from_pretrained("premsa/political-bias-prediction-allsides-DeBERTa"),
            True,
            512
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        pipe = pipeline("text-classification", model=self.model, tokenizer=self.tokenizer)
        output = pipe(article_body)
        return {
            "LABEL_0": Leaning.LEFT,
            "LABEL_1": Leaning.CENTER,
            "LABEL_2": Leaning.RIGHT
        }[output[0]["label"]]

class DistilBertPoliticalBias(Model):
    def __init__(self):
        super().__init__(
            RobertaTokenizer.from_pretrained("cajcodes/DistilBERT-PoliticalBias"),
            DistilBertForSequenceClassification.from_pretrained("cajcodes/DistilBERT-PoliticalBias"),
            True,
            512
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        article_body = article_body.replace("\n", "").replace("``", "\"")
        tokens = self.get_tokens(article_body, truncate_tokens)
        unk_token_id = self.tokenizer.convert_tokens_to_ids(self.tokenizer.unk_token)
        tokens["input_ids"][tokens["input_ids"] >= self.model.config.vocab_size] = unk_token_id
        output = self.get_output(tokens)
        return [Leaning.RIGHT, Leaning.RIGHT, Leaning.CENTER, Leaning.LEFT, Leaning.LEFT][
            torch.argmax(output.logits, dim=-1)
        ]


class BertPoliticalBiasFineTune(Model):
    def __init__(self):
        super().__init__(
            BertTokenizer.from_pretrained("bert-base-uncased"),
            AutoModelForSequenceClassification.from_pretrained("jhonalevc1995/BERT-political_bias-finetune"),
            False
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        tokens = self.get_tokens(article_body, truncate_tokens)
        output = self.get_output(tokens)
        return [Leaning.LEFT, Leaning.RIGHT][torch.argmax(output.logits, dim=-1)]


class DistilBertPoliticalFinetune(Model):
    def __init__(self):
        super().__init__(
            AutoTokenizer.from_pretrained("harshal-11/DistillBERT-Political-Finetune"),
            AutoModelForSequenceClassification.from_pretrained("harshal-11/DistillBERT-Political-Finetune"),
            True,
            512
        )

    def predict(self, article_body: str, truncate_tokens: bool) -> Leaning:
        tokens = self.get_tokens(article_body, truncate_tokens)
        output = self.get_output(tokens)
        return [Leaning.LEFT, Leaning.CENTER, Leaning.RIGHT][torch.argmax(output.logits, dim=-1)]


def get_models() -> List[Model]:
    return [
        PoliticalBiasBert(),
        PoliticalBiasPredictionAllsidesDeberta(),
        DistilBertPoliticalBias(),
        BertPoliticalBiasFineTune(),
        DistilBertPoliticalFinetune()
    ]

from typing import Generator

import torch
from adapters import AutoAdapterModel
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    pipeline,
)

from utils.model_utils import Model, available_device


def get_existing_politicalness_models() -> Generator[Model, None, None]:
    # Caution is necessary with creating lists to yield from. The models cannot be instantiated
    # right away, as that would completely undermine the usage of the generator. It could cause the
    # memory to overflow. Instead, models need to be yielded one at a time.
    for model_class in [TopicPolitics]:
        yield model_class()


class TopicPolitics(Model):
    def __init__(self) -> None:
        super().__init__(
            AutoTokenizer.from_pretrained(
                "dell-research-harvard/topic-politics",
                code_revision="eb68c30bcecd019b1d2a93d3b595136126a30e07",
            ),
            AutoModelForSequenceClassification.from_pretrained(
                "dell-research-harvard/topic-politics",
                code_revision="eb68c30bcecd019b1d2a93d3b595136126a30e07",
            ),
        )

    def predict(self, text: str, truncate_tokens: bool) -> int:
        tokens = self.get_tokens(text, truncate_tokens)
        output = self.get_output(tokens)
        return torch.argmax(output.logits, dim=-1).item()


class ClassifierMainSubjectPolitics(Model):
    def __init__(self) -> None:
        super().__init__(
            AutoTokenizer.from_pretrained(
                "gptmurdock/classifier-main_subjects_politics",
                code_revision="520f5a8c4a687b4b0bb66ad4ac29e3495c4e150e",
            ),
            AutoModelForSequenceClassification.from_pretrained(
                "gptmurdock/classifier-main_subjects_politics",
                code_revision="520f5a8c4a687b4b0bb66ad4ac29e3495c4e150e",
            ),
        )

    def predict(self, text: str, truncate_tokens: bool) -> int:
        tokens = self.get_tokens(text, truncate_tokens)
        output = self.get_output(tokens)
        return torch.argmax(output.logits, dim=-1).item()


class PoliticalBiasDebertaMnli(Model):
    def __init__(self) -> None:
        model = AutoAdapterModel.from_pretrained(
            "microsoft/deberta-base-mnli",
            code_revision="3e4177c6b8c8d12094658e170aab4e15002ece30",
        )
        model.load_adapter(
            "SOUMYADEEPSAR/political_bias_deberta-mnli",
            version="3e4177c6b8c8d12094658e170aab4e15002ece30",
            set_active=True,
        )
        super().__init__(
            AutoTokenizer.from_pretrained(
                "microsoft/deberta-base-mnli",
                code_revision="a80a6eb013898011540b19bf1f64e21eb61e53d6",
            ),
            model,
            512,
        )

    def predict(self, text: str, truncate_tokens: bool) -> int:
        tokens = self.get_tokens(text, truncate_tokens)
        output = self.get_output(tokens)
        return [1, 0][torch.argmax(output.logits, dim=-1).item()]


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
        )
        self.pipe = pipeline(
            "zero-shot-classification",
            model=self.model,
            tokenizer=self.tokenizer,
            device=available_device,
        )

    def predict(self, text: str, truncate_tokens: bool) -> int:
        hypothesis_template = "This text {} politics."
        output = self.pipe(
            text,
            ["is not", "is"],
            hypothesis_template=hypothesis_template,
            multi_label=False,
        )
        return {"is not": 0, "is": 1}[output["labels"][0]]

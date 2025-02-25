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

from utils.model_utils import LeaningModel, available_device


def get_existing_leaning_models() -> Generator[LeaningModel, None, None]:
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


class PoliticalBiasBert(LeaningModel):
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

    def predict(self, text: str, truncate_tokens: bool = True) -> int:
        tokens = self.get_tokens(text, truncate_tokens)
        output = self.get_output(tokens)
        return [0, 1, 2][torch.argmax(output.logits, dim=-1).item()]


class PoliticalBiasPredictionAllsidesDeberta(LeaningModel):
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
            device=available_device,
        )

    def predict(self, text: str, _truncate_tokens: bool = True) -> int:
        output = self.pipe(text)
        return {
            "LABEL_0": 0,
            "LABEL_1": 1,
            "LABEL_2": 2,
        }[output[0]["label"]]


class DistilBertPoliticalBias(LeaningModel):
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

    def predict(self, text: str, truncate_tokens: bool = True) -> int:
        text = text.replace("\n", "").replace("``", '"')
        tokens = self.get_tokens(text, truncate_tokens)
        unk_token_id = self.tokenizer.convert_tokens_to_ids(self.tokenizer.unk_token)
        tokens["input_ids"][
            tokens["input_ids"] >= self.model.config.vocab_size
        ] = unk_token_id
        output = self.get_output(tokens)
        return [2, 2, 1, 0, 0][torch.argmax(output.logits, dim=-1).item()]


class BertPoliticalBiasFinetune(LeaningModel):
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

    def predict(self, text: str, truncate_tokens: bool = True) -> int:
        tokens = self.get_tokens(text, truncate_tokens)
        output = self.get_output(tokens)
        return [0, 1][torch.argmax(output.logits, dim=-1).item()]


class DistilBertPoliticalFinetune(LeaningModel):
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

    def predict(self, text: str, truncate_tokens: bool = True) -> int:
        tokens = self.get_tokens(text, truncate_tokens)
        output = self.get_output(tokens)
        return [0, 1, 2][torch.argmax(output.logits, dim=-1).item()]


class PoliticalIdeologiesRobertaFinetuned(LeaningModel):
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

    def predict(self, text: str, truncate_tokens: bool = True) -> int:
        tokens = self.get_tokens(text, truncate_tokens)
        output = self.get_output(tokens)
        return [1, 0][torch.argmax(output.logits, dim=-1).item()]


class DebertaPoliticalClassification(LeaningModel):
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

    def predict(self, text: str, truncate_tokens: bool = True) -> int:
        tokens = self.get_tokens(text, truncate_tokens)
        output = self.get_output(tokens)
        return [0, 1][torch.argmax(output.logits, dim=-1).item()]


class DistilBertPoliticalTweets(LeaningModel):
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

    def predict(self, text: str, truncate_tokens: bool = True) -> int:
        tokens = self.get_tokens(text, truncate_tokens)
        output = self.get_output(tokens)
        return [1, 0][torch.argmax(output.logits, dim=-1)]


class PoliticalDebateLarge(LeaningModel):
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
            supports_center_leaning_class=True,
        )
        self.pipe = pipeline(
            "zero-shot-classification",
            model=self.model,
            tokenizer=self.tokenizer,
            device=available_device,
        )

    def predict(self, text: str, _truncate_tokens: bool = True) -> int:
        hypothesis_template = "This text supports {} political leaning."
        output = self.pipe(
            text,
            ["left", "center", "right"],
            hypothesis_template=hypothesis_template,
            multi_label=False,
        )
        return {"left": 0, "center": 1, "right": 2}[output["labels"][0]]

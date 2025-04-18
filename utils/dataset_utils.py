import os
from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Generator, Self, Type, TypeVar

import datasets
import math
import numpy as np
import pandas as pd
from pandas import DataFrame

from utils.base_directory import base_directory

T = TypeVar("T")

LEANING_LEAVE_ONE_OUT_BENCHMARK_EXCLUDED_NAMES = [
    "webis_bias_flipper_18",
    "webis_news_bias_20",
]

leaning_with_center_label_mapping = {"left": 0, "center": 1, "right": 2}
leaning_no_center_label_mapping = {"left": 0, "right": 1}
politicalness_label_mapping = {"non-political": 0, "political": 1}

datasets_directory = base_directory / "datasets"


class Dataset(ABC):
    def __init__(self, name: str, dataframe: DataFrame, label_column_name: str) -> None:
        self.name = name
        self.dataframe = dataframe
        self.label_column_name = label_column_name
        self.has_title = self.dataframe.get("title") is not None

    @abstractmethod
    def label_mapping(self) -> dict[str, int]:
        pass

    def take_even_class_sample_by_size(self, size: int) -> Self:
        dataset = deepcopy(self)
        if size < self.dataframe[self.label_column_name].nunique():
            raise ValueError(
                "The sample size must be at least the number of present classes."
            )

        class_sample_count = int(
            np.ceil(size / dataset.dataframe[self.label_column_name].nunique())
        )
        dataset.dataframe = (
            dataset.dataframe.groupby(
                self.label_column_name, group_keys=False, observed=True
            )
            .apply(lambda group: systematic_sample(group, class_sample_count))
            .head(size)
        )

        return dataset

    def take_even_class_sample_by_fraction(self, fraction: float) -> Self:
        return self.take_even_class_sample_by_size(
            round(len(self.dataframe) * fraction)
        )

    def transform_train_texts(self) -> Self:
        dataset = deepcopy(self)
        if dataset.has_title:
            dataset.dataframe["text"] = (
                dataset.dataframe["title"].fillna("")
                + "\n\n"
                + dataset.dataframe["body"].fillna("")
            ).str.strip()
        else:
            dataset.dataframe["text"] = dataset.dataframe["body"]
        return dataset

    def transform_train_labels(
        self, label_mapping: dict[str, int] | None = None
    ) -> Self:
        dataset = deepcopy(self)
        dataset.dataframe["label"] = (
            dataset.dataframe[self.label_column_name]
            .cat.rename_categories(
                self.label_mapping() if label_mapping is None else label_mapping
            )
            .cat.remove_unused_categories()
        )
        return dataset

    def transform_for_inference(
        self, label_mapping: dict[str, int] | None = None
    ) -> Self:
        dataset = deepcopy(self)
        dataset = dataset.transform_train_texts()
        dataset = dataset.transform_train_labels(label_mapping)
        dataset.dataframe = dataset.dataframe[["text", "label"]]
        return dataset

    def prepare_for_intersection_comparison(self, body_slice_size: int) -> Self:
        dataset = deepcopy(self)

        if dataset.has_title:
            dataset.dataframe["title"] = (
                dataset.dataframe["title"]
                .str.replace(r"[^a-zA-Z]", "", regex=True)
                .str.lower()
            )
            dataset.dataframe["has_notnull_title"] = dataset.dataframe["title"].notna()
        else:
            dataset.dataframe["title"] = np.nan
            dataset.dataframe["has_notnull_title"] = False

        dataset.dataframe["body"] = (
            dataset.dataframe["body"]
            .str.replace(r"[^a-zA-Z]", "", regex=True)
            .str.lower()
        )
        dataset.dataframe["has_notnull_body"] = dataset.dataframe["body"].notna()

        dataset.dataframe["body_slice"] = dataset.dataframe["body"].map(
            lambda body: (
                body[
                    math.floor(len(body) / 2 - body_slice_size / 2) : math.ceil(
                        len(body) / 2 + body_slice_size / 2
                    )
                ]
                if pd.notna(body) and len(body) > body_slice_size
                else body
            )
        )

        return dataset

    def to_huggingface(self) -> datasets.Dataset:
        return datasets.Dataset.from_pandas(
            self.dataframe, info=datasets.DatasetInfo(dataset_name=self.name)
        )


class PoliticalnessDataset(Dataset):
    def __init__(self, name: str, dataframe: DataFrame):
        super().__init__(name, dataframe, "politicalness")

    def label_mapping(self) -> dict[str, int]:
        return politicalness_label_mapping


class PoliticalLeaningDataset(Dataset):
    def __init__(self, name: str, dataframe: DataFrame):
        super().__init__(name, dataframe, "leaning")

    def label_mapping(self) -> dict[str, int]:
        return (
            leaning_with_center_label_mapping
            if self.has_center_leaning_class()
            else leaning_no_center_label_mapping
        )

    def has_center_leaning_class(self):
        return len(self.dataframe["leaning"].unique()) == 3

    def take_balanced_class_sample_by_size(
        self, size: int, center_multiplier: float
    ) -> Self:
        dataset = deepcopy(self)
        if size < self.dataframe[self.label_column_name].nunique():
            raise ValueError(
                "The sample size must be at least the number of present classes."
            )

        class_sample_count = int(
            np.ceil(size / dataset.dataframe[self.label_column_name].nunique())
        )
        dataset.dataframe = dataset.dataframe.groupby(
            self.label_column_name, group_keys=False, observed=True
        ).apply(
            lambda group: systematic_sample(
                group,
                (
                    int(class_sample_count * center_multiplier)
                    if self.has_center_leaning_class()
                    and (group["leaning"].eq("center").all())
                    else class_sample_count
                ),
            )
        )

        return dataset


def get_datasets(directory: str, cls: Type[T]) -> Generator[T, None, None]:
    for filename in sorted(
        filter(
            lambda filename: filename.endswith(".parquet"),
            os.listdir(datasets_directory / directory / "preprocessed"),
        )
    ):
        with open(
            os.path.join(datasets_directory / directory / "preprocessed", filename),
            "rb",
        ) as file:
            yield cls(os.path.splitext(filename)[0], pd.read_parquet(file))


def get_politicalness_datasets() -> Generator[PoliticalnessDataset, None, None]:
    return get_datasets("politicalness", PoliticalnessDataset)


def get_politicalness_datasets_from_leaning_datasets() -> (
    Generator[PoliticalnessDataset, None, None]
):
    return get_datasets("political_leaning", PoliticalnessDataset)


def get_politicalness_datasets_from_leaning_datasets_for_leave_one_out_benchmark() -> (
    Generator[PoliticalnessDataset, None, None]
):
    yield from filter(
        lambda dataset: dataset.name
        not in LEANING_LEAVE_ONE_OUT_BENCHMARK_EXCLUDED_NAMES,
        get_politicalness_datasets_from_leaning_datasets(),
    )


def get_leaning_datasets() -> Generator[PoliticalLeaningDataset, None, None]:
    return get_datasets("political_leaning", PoliticalLeaningDataset)


def get_leaning_datasets_for_leave_one_out_benchmark() -> (
    Generator[PoliticalLeaningDataset, None, None]
):
    yield from filter(
        lambda dataset: dataset.name
        not in LEANING_LEAVE_ONE_OUT_BENCHMARK_EXCLUDED_NAMES,
        get_leaning_datasets(),
    )


def systematic_sample(dataframe, size: int):
    if size <= 0:
        raise ValueError("The sample size must be positive.")
    if size >= len(dataframe):
        return dataframe
    indexes = list(range(0, len(dataframe), max(1, len(dataframe) // size)))[:size]
    return dataframe.iloc[indexes]


def get_leave_one_out_datasets(
    whole_datasets: List[Dataset],
    training_political_leaning: bool,
    test_dataset_sample_fraction: float,
    eval_dataset_sample_size: int,
    train_dataset_sample_size: int,
    balance_center_leaning_class: bool,
    center_leaning_class_train_size_multipliers: dict[str, float] | None,
    center_leaning_class_train_size_multiplier_default: float | None,
):
    for dataset in whole_datasets:
        test_dataset = dataset.take_even_class_sample_by_fraction(
            test_dataset_sample_fraction
        )
        # Remove the test sample from the source dataframe.
        dataset.dataframe = dataset.dataframe.loc[
            ~dataset.dataframe.index.isin(test_dataset.dataframe.index)
        ]

    eval_datasets = []
    for dataset in whole_datasets:
        dataset = dataset.take_even_class_sample_by_size(eval_dataset_sample_size)
        dataset = dataset.transform_for_inference(
            leaning_with_center_label_mapping if training_political_leaning else None
        )
        eval_datasets.append(dataset.to_huggingface())

    def get_train_dataset(left_out_dataset: dataset_utils.Dataset) -> datasets.Dataset:
        train_datasets_separate = []

        for dataset in filter(
            lambda dataset: dataset.name != left_out_dataset.name,
            whole_datasets,
        ):
            if training_political_leaning:
                if balance_center_leaning_class:
                    dataset = dataset.take_balanced_class_sample_by_size(
                        train_dataset_sample_size,
                        (
                            center_leaning_class_train_size_multipliers[
                                left_out_dataset.name
                            ]
                            if left_out_dataset.name
                            in center_leaning_class_train_size_multipliers.keys()
                            else center_leaning_class_train_size_multiplier_default
                        ),
                    ).transform_for_inference()
                else:
                    dataset = dataset.take_even_class_sample_by_size(
                        train_dataset_sample_size
                    ).transform_for_inference(leaning_with_center_label_mapping)
            else:
                dataset = dataset.take_even_class_sample_by_size(
                    train_dataset_sample_size
                ).transform_for_inference()

            train_datasets_separate.append(dataset.to_huggingface())

        dataset = concatenate_datasets(
            train_datasets_separate,
            info=DatasetInfo(dataset_name=left_out_dataset.name),
        )
        print(left_out_dataset.name)
        print(dataset.to_pandas().groupby("label").count())
        return dataset

    train_datasets = [
        get_train_dataset(left_out_dataset) for left_out_dataset in whole_datasets
    ]

    del whole_datasets

    return train_datasets, eval_datasets

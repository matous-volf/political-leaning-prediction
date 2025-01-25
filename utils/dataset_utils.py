import os
from copy import deepcopy
from typing import Generator

import datasets
import numpy as np
import pandas as pd

from utils.base_directory import BASE_DIRECTORY


class Dataset:
    def __init__(self, name: str, dataframe: pd.DataFrame) -> None:
        self.name = name
        self.dataframe = dataframe
        self.has_title = self.dataframe.get("title") is not None
        self.has_center_leaning_class = len(self.dataframe["leaning"].unique()) == 3

    def to_huggingface(self):
        return datasets.Dataset.from_pandas(
            self.dataframe, info=datasets.DatasetInfo(dataset_name=self.name)
        )


DATASETS_DIRECTORY = BASE_DIRECTORY / "political_leaning" / "datasets" / "preprocessed"
LEAVE_ONE_OUT_BENCHMARK_EXCLUDED_NAMES = [
    "webis_bias_flipper_18",
    "webis_news_bias_20",
]


def get_datasets() -> Generator[Dataset, None, None]:
    for filename in sorted(
        filter(
            lambda filename: filename.endswith(".parquet"),
            os.listdir(DATASETS_DIRECTORY),
        )
    ):
        with open(os.path.join(DATASETS_DIRECTORY, filename), "rb") as file:
            yield Dataset(os.path.splitext(filename)[0], pd.read_parquet(file))


def get_datasets_for_leave_one_out_benchmark() -> Generator[Dataset, None, None]:
    yield from filter(
        lambda dataset: dataset.name not in LEAVE_ONE_OUT_BENCHMARK_EXCLUDED_NAMES,
        get_datasets(),
    )


def systematic_sample(group, size):
    if size <= 0:
        raise ValueError("The sample size must be positive.")
    if size >= len(group):
        return group
    indexes = list(range(0, len(group), max(1, len(group) // size)))[:size]
    return group.iloc[indexes]


def take_even_class_distribution_sample(dataset: Dataset, size: int) -> Dataset:
    dataset = deepcopy(dataset)

    if size == 0:
        dataset.dataframe = dataset.dataframe[0:0]
    else:
        class_sample_count = int(np.ceil(size / dataset.dataframe["leaning"].nunique()))
        dataset.dataframe = (
            dataset.dataframe.groupby("leaning", group_keys=False, observed=True)
            .apply(lambda group: systematic_sample(group, class_sample_count))
            .head(size)
        )

    return dataset


def transform_train_texts(dataset: Dataset) -> Dataset:
    dataset = deepcopy(dataset)
    if dataset.has_title:
        dataset.dataframe["text"] = (
            dataset.dataframe["title"].fillna("")
            + "\n\n"
            + dataset.dataframe["body"].fillna("")
        ).str.strip()
    else:
        dataset.dataframe["text"] = dataset.dataframe["body"]
    return dataset


def transform_train_labels(dataset: Dataset, label_mapping: dict[str, int]) -> Dataset:
    dataset = deepcopy(dataset)
    dataset.dataframe["label"] = dataset.dataframe["leaning"].cat.rename_categories(
        label_mapping
    )
    return dataset


def transform_for_inference(dataset: Dataset, label_mapping: dict[str, int]) -> Dataset:
    dataset = deepcopy(dataset)
    dataset = transform_train_texts(dataset)
    dataset = transform_train_labels(dataset, label_mapping)
    dataset.dataframe = dataset.dataframe[["text", "label"]]
    return dataset

import os
from typing import Generator

import numpy as np
import pandas as pd
from pandas import DataFrame

from utils.base_directory import BASE_DIRECTORY


class Dataset:
    def __init__(self, name: str, dataframe: pd.DataFrame) -> None:
        self.name = name
        self.dataframe = dataframe


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


def take_even_class_distribution_sample(dataframe: DataFrame, size: int) -> DataFrame:
    if size == 0:
        return dataframe[0:0]

    class_sample_count = int(np.ceil(size / dataframe["leaning"].nunique()))
    return (
        dataframe.groupby("leaning", group_keys=False, observed=True)[
            ["body", "leaning"]
        ]
        .apply(lambda group: systematic_sample(group, class_sample_count))
        .head(size)
    )


def transform_train_labels(
    dataframe: DataFrame, label_mapping: dict[str, int]
) -> DataFrame:
    dataframe = dataframe.rename(columns={"leaning": "label"})
    dataframe["label"] = dataframe["label"].cat.rename_categories(label_mapping)
    return dataframe

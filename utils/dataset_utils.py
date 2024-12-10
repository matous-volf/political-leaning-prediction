import os
from typing import Generator

import pandas as pd

from utils.base_directory import BASE_DIRECTORY


class Dataset:
    def __init__(self, name: str, dataframe: pd.DataFrame) -> None:
        self.name = name
        self.dataframe = dataframe


DATASETS_DIRECTORY = BASE_DIRECTORY / "datasets" / "preprocessed"
LEAVE_ONE_OUT_BENCHMARK_EXCLUDED_NAMES = [
    "polistance_issue_tweets",
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

import os
from typing import Generator

import pandas as pd

from utils.base_directory import BASE_DIRECTORY


class Dataset:
    def __init__(self, name: str, dataframe: pd.DataFrame) -> None:
        self.name = name
        self.dataframe = dataframe


DATASETS_DIRECTORY = BASE_DIRECTORY / "datasets" / "preprocessed"


def get_datasets() -> Generator[Dataset, None, None]:
    for filename in sorted(
        filter(lambda f: f.endswith(".parquet"), os.listdir(DATASETS_DIRECTORY))
    ):
        with open(os.path.join(DATASETS_DIRECTORY, filename), "rb") as file:
            yield Dataset(os.path.splitext(filename)[0], pd.read_parquet(file))


def systematic_sample(group, size):
    if size <= 0:
        raise ValueError("The sample size must be positive.")
    if size >= len(group):
        return group
    indexes = list(range(0, len(group), max(1, len(group) // size)))[:size]
    return group.iloc[indexes]

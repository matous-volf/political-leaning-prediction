import os
from typing import List

import pandas as pd


class Dataset:
    def __init__(self, name: str, dataframe: pd.DataFrame) -> None:
        self.name = name
        self.dataframe = dataframe


DATASETS_DIRECTORY = "../datasets/preprocessed"


def get_datasets() -> List[Dataset]:
    datasets = []
    for filename in filter(
        lambda f: f.endswith(".parquet"), os.listdir(DATASETS_DIRECTORY)
    ):
        with open(os.path.join(DATASETS_DIRECTORY, filename), "rb") as file:
            dataset = Dataset(os.path.splitext(filename)[0], pd.read_parquet(file))
            datasets.append(dataset)
    return sorted(datasets, key=lambda dataset: -len(dataset.dataframe))

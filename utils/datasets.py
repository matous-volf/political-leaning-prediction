import os
from typing import List

import pandas as pd


class Dataset:
    def __init__(self, name: str, dataframe: pd.DataFrame):
        self.name = name
        self.dataframe = dataframe


DATASETS_DIRECTORY = "../datasets/preprocessed"


def get_datasets() -> List[Dataset]:
    return sorted(map(
        lambda filename: Dataset(
            os.path.splitext(filename)[0],
            pd.read_parquet(open(os.path.join(DATASETS_DIRECTORY, filename), "rb"))
        ),
        filter(lambda filename: filename.endswith(".parquet"), os.listdir(DATASETS_DIRECTORY))
    ), key=lambda dataset: dataset.name)

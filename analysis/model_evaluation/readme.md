# Model evaluation

This document describes the methodology of evaluating the performance of a model on the available datasets.

The datasets can be sampled to a variable number of articles (`DATASET_SAMPLE_SIZE`) using systematic sampling (taking
rows at a regular interval).

If a model does not support the center leaning class, it is only tested on left or right leaning articles. To avoid
misinterpreting the resulting accuracy, models with different number of classes should be compared separately.

The evaluations can be replicated using [this notebook](politicalness/notebook.ipynb).

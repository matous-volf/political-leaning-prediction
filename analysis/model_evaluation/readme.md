# Model evaluation

This document describes the methodology of evaluating the performance of a model on the available datasets.

The datasets can be sampled to a variable number of articles (`DATASET_SAMPLE_SIZE`) using systematic sampling (taking
rows at a regular interval).

The models have a maximum length of tokens passed in. For this reason, tokenizer truncation is also configurable through
`TRUNCATE_TOKENS`. It enables the models to process texts longer than this limit (or at least a part of the text).
Disabling the truncation may result in some of the article bodies being too long to pass into some of the models, and so
getting skipped.

The evaluations can be replicated using [this notebook](notebook.ipynb).

# Leave-one-out dataset benchmark

## Methodology

If two datasets intersect with each other (as measured [here](/docs/dataset_intersection)) by a large amount,
the smaller dataset is not a part of this benchmark to avoid spillover. This applies for two political leaning datasets:
Webis bias flipper 18 and Webis news bias 20, which intersect significantly with each other and with the Article bias
prediction. The politicalness Medium post titles dataset intersects with the Political or not dataset as well, but that
is caused by the large number of very short (one or two words) bodies, that have a high probability of being present in
another body.

From each dataset, a sample of 1 000 rows (or less if the dataset is smaller) has been taken while ensuring an equal
distribution of classes and systematically sampling by the body length in each class. Several models have been
fine-tuned separately, each on a concatenation of all but one (the left-out dataset) of these samples. This has been
repeated, leaving out a different one dataset at a time.

The fine-tuned models can be reproduced
using [this notebook](/analysis/dataset_benchmark/leave_one_out/notebook.ipynb).

Then the models have been evaluated using the methodology prescribed in [this document](/docs/model_evaluation), while
the datasets have been sampled to 1 000 rows each. In the results, rows are the models and columns are the datasets. The
heading of the row means the left-out dataset (the only one that the model has not been fine-tuned on), while the
heading of the column is the dataset being evaluated on.

## Results

- [Politicalness](politicalness)
- [Political leaning](political_leaning)

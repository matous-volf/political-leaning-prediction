# Model evaluation

## Methodology

The datasets can be sampled to a variable number of rows (`DATASET_SAMPLE_SIZE`). The sampling ensures an even
distribution of the present classes, and it is systematic (taking rows at regular intervals) per each class.

If a political leaning model does not support the center leaning class, it is only tested on left or right leaning rows.
To avoid misinterpreting the resulting accuracies, models with different number of classes should be compared
separately.

The evaluations can be replicated using the notebooks in [this directory](/analysis/model_evaluation).

## Results

### Existing models

- [Politicalness](existing/politicalness)
- [Political leaning](existing/political_leaning)

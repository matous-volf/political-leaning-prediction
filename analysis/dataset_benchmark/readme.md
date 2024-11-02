# Dataset benchmark

From each dataset, a sample of 1 000 articles (except for the GPT-4 political bias dataset, which is smaller) has been
taken while ensuring an equal distribution of leaning and systematically sampling by the body length. Several models
have been fine-tuned separately on each of these samples to compare the suitability of the datasets for training.

The fine-tuned models are stored in [this directory](/models_custom/dataset_benchmark) and can be reproduced using
[this notebook](notebook.ipynb).

Then the models have been evaluated using the methodology prescribed in [this document](../model_evaluation) while the
datasets have been sampled to 1 000 articles each. The resulting accuracies are recorded in the tables below, rows being
models and columns being datasets. The heading of the row means the dataset the model has been fine-tuned on while the
heading of the column is the dataset being evaluated on.

The results on the dataset each model has been fine-tuned on (the diagonal) should be taken with a grain of salt, as the
fine-tuning sample (1 000 articles) is a different portion of each dataset. That said, smaller datasets have a greater
chance of the same articles appearing both in fine-tuning and in evaluation, making the prediction easier for the model.

## BERT base model (cased)

<table>
    <tr>
        <th></th>
        <th>CommonCrawl news articles</th>
        <th>Article bias prediction</th>
        <th>Qbias</th>
        <th>Webis-News-Bias-20</th>
        <th>Webis-Bias-Flipper-18</th>
        <th>GPT-4 political bias</th>
    </tr>
    <tr>
        <th>CommonCrawl news articles</th>
        <td>695/1000 (69.5 %)</td>
        <td>400/1000 (40.0 %)</td>
        <td>396/1000 (39.6 %)</td>
        <td>482/1000 (48.2 %)</td>
        <td>389/1000 (38.9 %)</td>
        <td>264/612 (43.14 %)</td>
    </tr>
    <tr>
        <th>Article bias prediction</th>
        <td>544/1000 (54.4 %)</td>
        <td>592/1000 (59.2 %)</td>
        <td>405/1000 (40.5 %)</td>
        <td>500/1000 (50.0 %)</td>
        <td>389/1000 (38.9 %)</td>
        <td>226/612 (36.93 %)</td>
    </tr>
    <tr>
        <th>Qbias</th>
        <td>430/1000 (43.0 %)</td>
        <td>530/1000 (53.0 %)</td>
        <td>483/1000 (48.3 %)</td>
        <td>466/1000 (46.6 %)</td>
        <td>395/1000 (39.5 %)</td>
        <td>256/612 (41.83 %)</td>
    </tr>
    <tr>
        <th>Webis-News-Bias-20</th>
        <td>513/1000 (51.3 %)</td>
        <td>546/1000 (54.6 %)</td>
        <td>447/1000 (44.7 %)</td>
        <td>718/1000 (71.8 %)</td>
        <td>521/1000 (52.1 %)</td>
        <td>264/612 (43.14 %)</td>
    </tr>
    <tr>
        <th>Webis-Bias-Flipper-18</th>
        <td>505/1000 (50.5 %)</td>
        <td>485/1000 (48.5 %)</td>
        <td>466/1000 (46.6 %)</td>
        <td>618/1000 (61.8 %)</td>
        <td>745/1000 (74.5 %)</td>
        <td>277/612 (45.26 %)</td>
    </tr>
    <tr>
        <th>GPT-4 political bias</th>
        <td>557/1000 (55.7 %)</td>
        <td>493/1000 (49.3 %)</td>
        <td>397/1000 (39.7 %)</td>
        <td>636/1000 (63.6 %)</td>
        <td>760/1000 (76.0 %)</td>
        <td>576/612 (94.12 %)</td>
    </tr>
</table>

## RoBERTa base

<table>
    <tr>
        <th></th>
        <th>CommonCrawl news articles</th>
        <th>Article bias prediction</th>
        <th>Qbias</th>
        <th>Webis-News-Bias-20</th>
        <th>Webis-Bias-Flipper-18</th>
        <th>GPT-4 political bias</th>
    </tr>
    <tr>
        <th>CommonCrawl news articles</th>
        <td>767/1000 (76.7 %)</td>
        <td>479/1000 (47.9 %)</td>
        <td>408/1000 (40.8 %)</td>
        <td>529/1000 (52.9 %)</td>
        <td>464/1000 (46.4 %)</td>
        <td>182/612 (29.74 %)</td>
    </tr>
    <tr>
        <th>Article bias prediction</th>
        <td>693/1000 (69.3 %)</td>
        <td>593/1000 (59.3 %)</td>
        <td>382/1000 (38.2 %)</td>
        <td>558/1000 (55.8 %)</td>
        <td>465/1000 (46.5 %)</td>
        <td>125/612 (20.42 %)</td>
    </tr>
    <tr>
        <th>Qbias</th>
        <td>313/1000 (31.3 %)</td>
        <td>349/1000 (34.9 %)</td>
        <td>328/1000 (32.8 %)</td>
        <td>392/1000 (39.2 %)</td>
        <td>432/1000 (43.2 %)</td>
        <td>250/612 (40.85 %)</td>
    </tr>
    <tr>
        <th>Webis-News-Bias-20</th>
        <td>510/1000 (51.0 %)</td>
        <td>497/1000 (49.7 %)</td>
        <td>341/1000 (34.1 %)</td>
        <td>612/1000 (61.2 %)</td>
        <td>463/1000 (46.3 %)</td>
        <td>238/612 (38.89 %)</td>
    </tr>
    <tr>
        <th>Webis-Bias-Flipper-18</th>
        <td>511/1000 (51.1 %)</td>
        <td>424/1000 (42.4 %)</td>
        <td>444/1000 (44.4 %)</td>
        <td>478/1000 (47.8 %)</td>
        <td>691/1000 (69.1 %)</td>
        <td>182/612 (29.74 %)</td>
    </tr>
    <tr>
        <th>GPT-4 political bias</th>
        <td>351/1000 (35.1 %)</td>
        <td>360/1000 (36.0 %)</td>
        <td>355/1000 (35.5 %)</td>
        <td>446/1000 (44.6 %)</td>
        <td>666/1000 (66.6 %)</td>
        <td>524/612 (85.62 %)</td>
    </tr>
</table>

## DeBERTa V3 base

<table>
    <tr>
        <th></th>
        <th>CommonCrawl news articles</th>
        <th>Article bias prediction</th>
        <th>Qbias</th>
        <th>Webis-News-Bias-20</th>
        <th>Webis-Bias-Flipper-18</th>
        <th>GPT-4 political bias</th>
    </tr>
    <tr>
        <th>CommonCrawl news articles</th>
        <td>123/1000 (12.3 %)</td>
        <td>297/1000 (29.7 %)</td>
        <td>198/1000 (19.8 %)</td>
        <td>170/1000 (17.0 %)</td>
        <td>204/1000 (20.4 %)</td>
        <td>178/612 (29.08 %)</td>
    </tr>
    <tr>
        <th>Article bias prediction</th>
        <td>123/1000 (12.3 %)</td>
        <td>297/1000 (29.7 %)</td>
        <td>198/1000 (19.8 %)</td>
        <td>170/1000 (17.0 %)</td>
        <td>204/1000 (20.4 %)</td>
        <td>178/612 (29.08 %)</td>
    </tr>
    <tr>
        <th>Qbias</th>
        <td>310/1000 (31.0 %)</td>
        <td>349/1000 (34.9 %)</td>
        <td>328/1000 (32.8 %)</td>
        <td>392/1000 (39.2 %)</td>
        <td>432/1000 (43.2 %)</td>
        <td>250/612 (40.85 %)</td>
    </tr>
    <tr>
        <th>Webis-News-Bias-20</th>
        <td>123/1000 (12.3 %)</td>
        <td>297/1000 (29.7 %)</td>
        <td>198/1000 (19.8 %)</td>
        <td>170/1000 (17.0 %)</td>
        <td>204/1000 (20.4 %)</td>
        <td>178/612 (29.08 %)</td>
    </tr>
    <tr>
        <th>Webis-Bias-Flipper-18</th>
        <td>123/1000 (12.3 %)</td>
        <td>297/1000 (29.7 %)</td>
        <td>198/1000 (19.8 %)</td>
        <td>170/1000 (17.0 %)</td>
        <td>204/1000 (20.4 %)</td>
        <td>178/612 (29.08 %)</td>
    </tr>
    <tr>
        <th>GPT-4 political bias</th>
        <td>310/1000 (31.0 %)</td>
        <td>349/1000 (34.9 %)</td>
        <td>328/1000 (32.8 %)</td>
        <td>392/1000 (39.2 %)</td>
        <td>432/1000 (43.2 %)</td>
        <td>250/612 (40.85 %)</td>
    </tr>
</table>

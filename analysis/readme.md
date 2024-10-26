# Analysis

## Dataset intersection

The intersections of articles between the datasets have been measured by comparing the article titles. If two articles
have the same title (trimmed of leading and trailing whitespace), they are considered the same.

An exception is the CommonCrawl dataset, which doesn't have a title column. So it is necessary to compare the bodies in
some way. A primitive char-to-char string comparison does not serve this purpose, because different article scrapers
include different parts of the page, for instance the title of the comment section. Sophisticated string similarity
algorithms (e.g. the Levenstein distance) are not a viable option, since they have relatively high time complexities. A
simpler algorithm has been chosen: slicing a middle part (e.g. 50 characters) out of one article and testing, whether
the second article contains it. Slicing the middle is considered optimal, as that is the part with the least probability
of a scraping mismatch. Still, this method only gives a rough estimate of the true intersection – for example, there are
instances of false positive matches caused by two articles both citing one politician's statement in their middle.

Beforehand, both the titles and the bodies are stripped of any non-letter characters (even whitespace), so
that irrelevant text discrepancies don't manifest.

The results are shown in the table:

<table>
  <tr>
    <th></th>
    <th>CommonCrawl news articles</th>
    <th>Article bias prediction</th>
    <th>Qbias</th>
    <th>Webis-News-Bias-20</th>
    <th>Webis-Bias-Flipper-18</th>
  </tr>
  <tr>
    <th>CommonCrawl news articles</th>
    <td>389471 (100.0 %)</td>
    <td>2514 (0.6 %)</td>
    <td>77 (0.0 %)</td>
    <td>611 (0.2 %)</td>
    <td>610 (0.2 %)</td>
  </tr>
  <tr>
    <th>Article bias prediction</th>
    <td>2514 (6.7 %)</td>
    <td>37490 (100.0 %)</td>
    <td>66 (0.2 %)</td>
    <td>3618 (9.7 %)</td>
    <td>2679 (7.1 %)</td>
  </tr>
  <tr>
    <th>Qbias</th>
    <td>77 (0.4 %)</td>
    <td>66 (0.3 %)</td>
    <td>21533 (100.0 %)</td>
    <td>28 (0.1 %)</td>
    <td>21 (0.1 %)</td>
  </tr>
  <tr>
    <th>Webis-News-Bias-20</th>
    <td>611 (8.1 %)</td>
    <td>3618 (48.2 %)</td>
    <td>28 (0.4 %)</td>
    <td>7514 (100.0 %)</td>
    <td>4831 (64.3 %)</td>
  </tr>
  <tr>
    <th>Webis-Bias-Flipper-18</th>
    <td>610 (9.8 %)</td>
    <td>2679 (43.0 %)</td>
    <td>21 (0.3 %)</td>
    <td>4831 (77.5 %)</td>
    <td>6237 (100.0 %)</td>
  </tr>
</table>

The percentages in each row mean the portion of the intersection over all the articles in the dataset in the
corresponding row. For example, the CommonCrawl news articles dataset has an intersection of 2514 articles with the
Article bias prediction dataset, which is 0.6 % of the CommonCrawl dataset. In the Article bias detection dataset row,
the intersection size is the same number (2514), but that equals to 6.7 % of that dataset.

The measurement can be replicated using [this notebook](dataset_intersection.ipynb).

## Model evaluation

The DistilBertPoliticalBias model is in fact trained to predict conservative vs. liberal leaning. That output has been
mapped to right vs. left respectively. Moreover, it uses a 5-level spectrum, which has been reduced to a 3-level one.

The BertPoliticalBiasFinetune model does not support a center leaning class, and so has been only tested on left or
right leaning articles. To avoid misinterpreting the resulting accuracy (when comparing to the other models), it is
included in a separate table.

According to their description on Hugging Face, PoliticalBiasPredictionAllsidesDeberta and (probably) PoliticalBiasBert
have been trained on the Article bias prediction dataset. This get reflected by the results: it is on this dataset that
PoliticalBiasBert scores the best (67.6 %). PoliticalBiasPredictionAllsidesDeberta scores the best on the
Webis-News-Bias-20 dataset which contains 48.2 % of the Article bias prediction dataset (as measured in the intersection
analysis).

The datasets have been downsampled to 1 000 articles each using systematic sampling (taking rows at a regular interval).

The models have a maximum length of tokens passed in. For this reason, two measurements have been conducted. Their
resulting accuracies are shown in the two tables below and can be replicated
using [this notebook](model_evaluation.ipynb).

### 1. With tokenizer truncation enabled

Tokenizer truncation enables the models to process texts longer than the limit (or at least a part of the text).

<table>
  <tr>
    <th></th>
    <th>CommonCrawl news articles</th>
    <th>Article bias prediction</th>
    <th>Qbias</th>
    <th>Webis-News-Bias-20</th>
    <th>Webis-Bias-Flipper-18</th>
  </tr>
  <tr>
    <th>PoliticalBiasBert</th>
    <td>194/1000 (19.4 %)</td>
    <td>676/1000 (67.6 %)</td>
    <td>399/1000 (39.9 %)</td>
    <td>530/1000 (53.0 %)</td>
    <td>449/1000 (44.9 %)</td>
  </tr>
  <tr>
    <th>PoliticalBiasPredictionAllsidesDeberta</th>
    <td>624/1000 (62.4 %)</td>
    <td>695/1000 (69.5 %)</td>
    <td>528/1000 (52.8 %)</td>
    <td>772/1000 (77.2 %)</td>
    <td>659/1000 (65.9 %)</td>
  </tr>
  <tr>
    <th>DistilBertPoliticalBias</th>
    <td>295/1000 (29.5 %)</td>
    <td>364/1000 (36.4 %)</td>
    <td>318/1000 (31.8 %)</td>
    <td>390/1000 (39.0 %)</td>
    <td>387/1000 (38.7 %)</td>
  </tr>
  <tr>
    <th>DistilBertPoliticalFinetune</th>
    <td>403/1000 (40.3 %)</td>
    <td>339/1000 (33.9 %)</td>
    <td>460/1000 (46.0 %)</td>
    <td>430/1000 (43.0 %)</td>
    <td>367/1000 (36.7 %)</td>
  </tr>
</table>

<table>
  <tr>
    <th></th>
    <th>CommonCrawl news articles</th>
    <th>Article bias prediction</th>
    <th>Qbias</th>
    <th>Webis-News-Bias-20</th>
    <th>Webis-Bias-Flipper-18</th>
  </tr>
  <tr>
    <th>BertPoliticalBiasFinetune</th>
    <td>581/1000 (58.1 %)</td>
    <td>477/1000 (47.7 %)</td>
    <td>558/1000 (55.8 %)</td>
    <td>561/1000 (56.1 %)</td>
    <td>411/1000 (41.1 %)</td>
  </tr>
</table>

### 2. With tokenizer truncation disabled

Disabling the truncation results in some of the article bodies being too long to pass into some of the models, and so
getting skipped.

<table>
  <tr>
    <th></th>
    <th>CommonCrawl news articles</th>
    <th>Article bias prediction</th>
    <th>Qbias</th>
    <th>Webis-News-Bias-20</th>
    <th>Webis-Bias-Flipper-18</th>
  </tr>
  <tr>
    <th>PoliticalBiasBert</th>
    <td>97/346 (28.03 %)</td>
    <td>69/102 (67.65 %)</td>
    <td>420/1000 (42.0 %)</td>
    <td>89/180 (49.44 %)</td>
    <td>102/185 (55.14 %)</td>
  </tr>
  <tr>
    <th>PoliticalBiasPredictionAllsidesDeberta</th>
    <td>613/1000 (61.3 %)</td>
    <td>684/1000 (68.4 %)</td>
    <td>535/1000 (53.5 %)</td>
    <td>764/1000 (76.4 %)</td>
    <td>678/1000 (67.8 %)</td>
  </tr>
  <tr>
    <th>DistilBertPoliticalBias</th>
    <td>107/378 (28.31 %)</td>
    <td>56/118 (47.46 %)</td>
    <td>357/1000 (35.7 %)</td>
    <td>110/191 (57.59 %)</td>
    <td>113/206 (54.85 %)</td>
  </tr>
  <tr>
    <th>DistilBertPoliticalFinetune</th>
    <td>137/377 (36.34 %)</td>
    <td>33/117 (28.21 %)</td>
    <td>446/1000 (44.6 %)</td>
    <td>50/189 (26.46 %)</td>
    <td>54/194 (27.84 %)</td>
  </tr>
</table>

<table>
  <tr>
    <th></th>
    <th>CommonCrawl news articles</th>
    <th>Article bias prediction</th>
    <th>Qbias</th>
    <th>Webis-News-Bias-20</th>
    <th>Webis-Bias-Flipper-18</th>
  </tr>
  <tr>
    <th>BertPoliticalBiasFinetune</th>
    <td>178/337 (52.82 %)</td>
    <td>49/131 (37.4 %)</td>
    <td>557/1000 (55.7 %)</td>
    <td>67/183 (36.61 %)</td>
    <td>95/247 (38.46 %)</td>
  </tr>
</table>

# Evaluation of existing models

DistilBertPoliticalBias is in fact trained to predict conservative vs. liberal leaning. That output has been mapped to
right vs. left respectively. Moreover, it uses a 5-level spectrum, which has been reduced to a 3-level one.

BertPoliticalBiasFinetune does not support the center leaning class, and so has only been tested on left or right
leaning articles. To avoid misinterpreting the resulting accuracy (when comparing to the other models), it is included
in a separate table.

According to their description on Hugging Face, PoliticalBiasPredictionAllsidesDeberta and (probably) PoliticalBiasBert
have been trained on the Article bias prediction dataset. This gets reflected by the results: it is on this dataset that
PoliticalBiasBert scores the best (69 %). PoliticalBiasPredictionAllsidesDeberta scores the second best on the
Webis-News-Bias-20 dataset, which is partly (47.7 %) made up of articles from the Article bias prediction dataset (as
measured in the [intersection analysis](../dataset_intersection)).

The measurements have been conducted using the methodology prescribed in [this document](../model_evaluation) while the
datasets have been sampled to 1 000 articles each.

The resulting accuracies are recorded in the two tables below.

## 1. With tokenizer truncation enabled

<table>
<tr>
    <th></th>
    <th>Article bias prediction</th>
    <th>CommonCrawl news articles</th>
    <th>Dem., rep. party platform topics</th>
    <th>GPT-4 political bias</th>
    <th>GPT-4 political ideologies</th>
    <th>Media political stance</th>
    <th>Parliament speeches 2024</th>
    <th>PoliStance issue tweets</th>
    <th>Political tweets</th>
    <th>Qbias</th>
    <th>Webis bias flipper 18</th>
    <th>Webis news bias 20</th>
    <th>average</th>
</tr>
<tr>
    <th>PoliticalBiasBert</th>
    <td>693 / 1000 (69 %)</td>
    <td>497 / 1000 (50 %)</td>
    <td>441 / 1000 (44 %)</td>
    <td>190 / 612 (31 %)</td>
    <td>425 / 1000 (42 %)</td>
    <td>379 / 1000 (38 %)</td>
    <td>423 / 1000 (42 %)</td>
    <td>400 / 1000 (40 %)</td>
    <td>456 / 1000 (46 %)</td>
    <td>399 / 1000 (40 %)</td>
    <td>458 / 1000 (46 %)</td>
    <td>543 / 1000 (54 %)</td>
    <td>5304 / 11612 (46 %)</td>
</tr>
<tr>
    <th>PoliticalBiasPredictionAllsidesDeberta</th>
    <td>644 / 1000 (64 %)</td>
    <td>640 / 1000 (64 %)</td>
    <td>607 / 1000 (61 %)</td>
    <td>188 / 612 (31 %)</td>
    <td>759 / 1000 (76 %)</td>
    <td>671 / 1000 (67 %)</td>
    <td>468 / 1000 (47 %)</td>
    <td>567 / 1000 (57 %)</td>
    <td>585 / 1000 (58 %)</td>
    <td>521 / 1000 (52 %)</td>
    <td>685 / 1000 (68 %)</td>
    <td>756 / 1000 (76 %)</td>
    <td>7091 / 11612 (61 %)</td>
</tr>
<tr>
    <th>DistilBertPoliticalBias</th>
    <td>348 / 1000 (35 %)</td>
    <td>312 / 1000 (31 %)</td>
    <td>504 / 1000 (50 %)</td>
    <td>502 / 612 (82 %)</td>
    <td>582 / 1000 (58 %)</td>
    <td>391 / 1000 (39 %)</td>
    <td>513 / 1000 (51 %)</td>
    <td>479 / 1000 (48 %)</td>
    <td>440 / 1000 (44 %)</td>
    <td>340 / 1000 (34 %)</td>
    <td>427 / 1000 (43 %)</td>
    <td>386 / 1000 (39 %)</td>
    <td>5224 / 11612 (45 %)</td>
</tr>
<tr>
    <th>DistilBertPoliticalFinetune</th>
    <td>345 / 1000 (34 %)</td>
    <td>403 / 1000 (40 %)</td>
    <td>404 / 1000 (40 %)</td>
    <td>271 / 612 (44 %)</td>
    <td>579 / 1000 (58 %)</td>
    <td>469 / 1000 (47 %)</td>
    <td>409 / 1000 (41 %)</td>
    <td>446 / 1000 (45 %)</td>
    <td>492 / 1000 (49 %)</td>
    <td>454 / 1000 (45 %)</td>
    <td>356 / 1000 (36 %)</td>
    <td>383 / 1000 (38 %)</td>
    <td>5011 / 11612 (43 %)</td>
</tr>
</table>

<table>
<tr>
    <th></th>
    <th>Article bias prediction</th>
    <th>CommonCrawl news articles</th>
    <th>Dem., rep. party platform topics</th>
    <th>GPT-4 political bias</th>
    <th>GPT-4 political ideologies</th>
    <th>Media political stance</th>
    <th>Parliament speeches 2024</th>
    <th>PoliStance issue tweets</th>
    <th>Political tweets</th>
    <th>Qbias</th>
    <th>Webis bias flipper 18</th>
    <th>Webis news bias 20</th>
    <th>average</th>
</tr>
<tr>
    <th>BertPoliticalBiasFinetune</th>
    <td>487 / 1000 (49 %)</td>
    <td>602 / 1000 (60 %)</td>
    <td>492 / 1000 (49 %)</td>
    <td>185 / 434 (43 %)</td>
    <td>502 / 1000 (50 %)</td>
    <td>597 / 1000 (60 %)</td>
    <td>483 / 1000 (48 %)</td>
    <td>471 / 1000 (47 %)</td>
    <td>499 / 1000 (50 %)</td>
    <td>557 / 1000 (56 %)</td>
    <td>438 / 1000 (44 %)</td>
    <td>545 / 1000 (55 %)</td>
    <td>5858 / 11434 (51 %)</td>
</tr>
</table>

## 2. With tokenizer truncation disabled

<table>
<tr>
    <th></th>
    <th>Article bias prediction</th>
    <th>CommonCrawl news articles</th>
    <th>Dem., rep. party platform topics</th>
    <th>GPT-4 political bias</th>
    <th>GPT-4 political ideologies</th>
    <th>Media political stance</th>
    <th>Parliament speeches 2024</th>
    <th>PoliStance issue tweets</th>
    <th>Political tweets</th>
    <th>Qbias</th>
    <th>Webis bias flipper 18</th>
    <th>Webis news bias 20</th>
    <th>average</th>
</tr>
<tr>
    <th>PoliticalBiasBert</th>
    <td>74 / 106 (70 %)</td>
    <td>198 / 375 (53 %)</td>
    <td>441 / 1000 (44 %)</td>
    <td>190 / 612 (31 %)</td>
    <td>425 / 1000 (42 %)</td>
    <td>92 / 247 (37 %)</td>
    <td>264 / 632 (42 %)</td>
    <td>400 / 1000 (40 %)</td>
    <td>456 / 1000 (46 %)</td>
    <td>399 / 1000 (40 %)</td>
    <td>100 / 205 (49 %)</td>
    <td>101 / 204 (50 %)</td>
    <td>3140 / 7381 (43 %)</td>
</tr>
<tr>
    <th>PoliticalBiasPredictionAllsidesDeberta</th>
    <td>644 / 1000 (64 %)</td>
    <td>640 / 1000 (64 %)</td>
    <td>607 / 1000 (61 %)</td>
    <td>188 / 612 (31 %)</td>
    <td>759 / 1000 (76 %)</td>
    <td>671 / 1000 (67 %)</td>
    <td>468 / 1000 (47 %)</td>
    <td>567 / 1000 (57 %)</td>
    <td>585 / 1000 (58 %)</td>
    <td>521 / 1000 (52 %)</td>
    <td>685 / 1000 (68 %)</td>
    <td>756 / 1000 (76 %)</td>
    <td>7091 / 11612 (61 %)</td>
</tr>
<tr>
    <th>DistilBertPoliticalBias</th>
    <td>50 / 127 (39 %)</td>
    <td>111 / 388 (29 %)</td>
    <td>504 / 1000 (50 %)</td>
    <td>502 / 612 (82 %)</td>
    <td>582 / 1000 (58 %)</td>
    <td>112 / 259 (43 %)</td>
    <td>329 / 641 (51 %)</td>
    <td>479 / 1000 (48 %)</td>
    <td>440 / 1000 (44 %)</td>
    <td>340 / 1000 (34 %)</td>
    <td>117 / 225 (52 %)</td>
    <td>108 / 221 (49 %)</td>
    <td>3674 / 7473 (49 %)</td>
</tr>
<tr>
    <th>DistilBertPoliticalFinetune</th>
    <td>36 / 119 (30 %)</td>
    <td>159 / 393 (40 %)</td>
    <td>404 / 1000 (40 %)</td>
    <td>271 / 612 (44 %)</td>
    <td>579 / 1000 (58 %)</td>
    <td>121 / 256 (47 %)</td>
    <td>251 / 639 (39 %)</td>
    <td>446 / 1000 (45 %)</td>
    <td>492 / 1000 (49 %)</td>
    <td>454 / 1000 (45 %)</td>
    <td>61 / 212 (29 %)</td>
    <td>66 / 215 (31 %)</td>
    <td>3340 / 7446 (45 %)</td>
</tr>
</table>

<table>
<tr>
    <th></th>
    <th>Article bias prediction</th>
    <th>CommonCrawl news articles</th>
    <th>Dem., rep. party platform topics</th>
    <th>GPT-4 political bias</th>
    <th>GPT-4 political ideologies</th>
    <th>Media political stance</th>
    <th>Parliament speeches 2024</th>
    <th>PoliStance issue tweets</th>
    <th>Political tweets</th>
    <th>Qbias</th>
    <th>Webis bias flipper 18</th>
    <th>Webis news bias 20</th>
    <th>average</th>
</tr>
<tr>
    <th>BertPoliticalBiasFinetune</th>
    <td>57 / 131 (44 %)</td>
    <td>187 / 355 (53 %)</td>
    <td>492 / 1000 (49 %)</td>
    <td>185 / 434 (43 %)</td>
    <td>502 / 1000 (50 %)</td>
    <td>133 / 256 (52 %)</td>
    <td>308 / 639 (48 %)</td>
    <td>471 / 1000 (47 %)</td>
    <td>499 / 1000 (50 %)</td>
    <td>557 / 1000 (56 %)</td>
    <td>105 / 276 (38 %)</td>
    <td>88 / 212 (42 %)</td>
    <td>3584 / 7303 (49 %)</td>
</tr>
</table>

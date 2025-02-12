# Evaluation of existing political leaning classification models

DistilBertPoliticalBias and PoliticalIdeologiesRobertaFinetuned are in fact trained to predict conservative vs. liberal
leaning. That output has been mapped to right vs. left respectively. The same applies for DistilBertPoliticalTweets,
which is trained to predict republican vs. democratic leaning.

DistilBertPoliticalBias uses a 5-level spectrum, which has been reduced to a 3-level one by mapping both highly and
mildly left-leaning to the left-leaning class and the same for right-leaning.

PoliticalDebateLarge is an NLI classifier and has been supplied a simple zero-shot hypothesis `This text supports {left
/ center / right} political leaning.`, which may not be optimal, as no rigorous testing has been done beforehand.

According to their Hugging Face model cards, some models have been trained on some of the collected datasets. These
relationships are shown in the following table.

<table>
<tr>
    <th>model</th>
    <th>trained on</th>
</tr>
<tr>
    <td>PoliticalBiasBert</td>
    <td>Article bias prediction</td>
</tr>
<tr>
    <td>PoliticalBiasPredictionAllsidesDeberta</td>
    <td>Article bias prediction</td>
</tr>
<tr>
    <td>PoliticalIdeologiesRobertaFinetuned</td>
    <td>GPT-4 political ideologies</td>
</tr>
<tr>
    <td>DebertaPoliticalClassification</td>
    <td>Parliament speeches 2024</td>
</tr>
<tr>
    <td>DistilBertPoliticalTweets</td>
    <td>a subset of Political tweets</td>
</tr>
</table>

This gets reflected in the accuracy results: the models score very high on the datasets they've been trained on.

The measurements have been conducted using the methodology prescribed in [this document](/docs/model_evaluation) while
the datasets have been sampled to 1 000 rows each.

The resulting accuracies are stored in files

- [with center leaning class](results_with_center_leaning_class.csv),
- [without center leaning class](results_without_center_leaning_class.csv)

and are recorded in the two tables below.

## with the center leaning class

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
    <th>Political podcasts</th>
    <th>Political tweets</th>
    <th>Qbias</th>
    <th>Webis bias flipper 18</th>
    <th>Webis news bias 20</th>
    <th>average</th>
</tr>
<tr>
    <th style="white-space: nowrap;">PoliticalBiasBert</th>
    <td style="white-space: nowrap;">693 / 1000 (69 %)</td>
    <td style="white-space: nowrap;">497 / 1000 (50 %)</td>
    <td style="white-space: nowrap;">441 / 1000 (44 %)</td>
    <td style="white-space: nowrap;">190 / 612 (31 %)</td>
    <td style="white-space: nowrap;">425 / 1000 (42 %)</td>
    <td style="white-space: nowrap;">379 / 1000 (38 %)</td>
    <td style="white-space: nowrap;">423 / 1000 (42 %)</td>
    <td style="white-space: nowrap;">428 / 1000 (43 %)</td>
    <td style="white-space: nowrap;">456 / 1000 (46 %)</td>
    <td style="white-space: nowrap;">399 / 1000 (40 %)</td>
    <td style="white-space: nowrap;">458 / 1000 (46 %)</td>
    <td style="white-space: nowrap;">543 / 1000 (54 %)</td>
    <td style="white-space: nowrap;">5332 / 11612 (46 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">PoliticalBiasPredictionAllsidesDeberta</th>
    <td style="white-space: nowrap;">644 / 1000 (64 %)</td>
    <td style="white-space: nowrap;">640 / 1000 (64 %)</td>
    <td style="white-space: nowrap;">607 / 1000 (61 %)</td>
    <td style="white-space: nowrap;">188 / 612 (31 %)</td>
    <td style="white-space: nowrap;">759 / 1000 (76 %)</td>
    <td style="white-space: nowrap;">671 / 1000 (67 %)</td>
    <td style="white-space: nowrap;">468 / 1000 (47 %)</td>
    <td style="white-space: nowrap;">758 / 1000 (76 %)</td>
    <td style="white-space: nowrap;">585 / 1000 (58 %)</td>
    <td style="white-space: nowrap;">521 / 1000 (52 %)</td>
    <td style="white-space: nowrap;">685 / 1000 (68 %)</td>
    <td style="white-space: nowrap;">756 / 1000 (76 %)</td>
    <td style="white-space: nowrap;">7282 / 11612 (63 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">DistilBertPoliticalBias</th>
    <td style="white-space: nowrap;">348 / 1000 (35 %)</td>
    <td style="white-space: nowrap;">312 / 1000 (31 %)</td>
    <td style="white-space: nowrap;">504 / 1000 (50 %)</td>
    <td style="white-space: nowrap;">502 / 612 (82 %)</td>
    <td style="white-space: nowrap;">582 / 1000 (58 %)</td>
    <td style="white-space: nowrap;">391 / 1000 (39 %)</td>
    <td style="white-space: nowrap;">513 / 1000 (51 %)</td>
    <td style="white-space: nowrap;">497 / 1000 (50 %)</td>
    <td style="white-space: nowrap;">440 / 1000 (44 %)</td>
    <td style="white-space: nowrap;">340 / 1000 (34 %)</td>
    <td style="white-space: nowrap;">427 / 1000 (43 %)</td>
    <td style="white-space: nowrap;">386 / 1000 (39 %)</td>
    <td style="white-space: nowrap;">5242 / 11612 (45 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">DistilBertPoliticalFinetune</th>
    <td style="white-space: nowrap;">345 / 1000 (34 %)</td>
    <td style="white-space: nowrap;">403 / 1000 (40 %)</td>
    <td style="white-space: nowrap;">404 / 1000 (40 %)</td>
    <td style="white-space: nowrap;">271 / 612 (44 %)</td>
    <td style="white-space: nowrap;">579 / 1000 (58 %)</td>
    <td style="white-space: nowrap;">469 / 1000 (47 %)</td>
    <td style="white-space: nowrap;">409 / 1000 (41 %)</td>
    <td style="white-space: nowrap;">444 / 1000 (44 %)</td>
    <td style="white-space: nowrap;">492 / 1000 (49 %)</td>
    <td style="white-space: nowrap;">454 / 1000 (45 %)</td>
    <td style="white-space: nowrap;">356 / 1000 (36 %)</td>
    <td style="white-space: nowrap;">383 / 1000 (38 %)</td>
    <td style="white-space: nowrap;">5009 / 11612 (43 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">PoliticalDebateLarge</th>
    <td style="white-space: nowrap;">473 / 1000 (47 %)</td>
    <td style="white-space: nowrap;">368 / 1000 (37 %)</td>
    <td style="white-space: nowrap;">492 / 1000 (49 %)</td>
    <td style="white-space: nowrap;">367 / 612 (60 %)</td>
    <td style="white-space: nowrap;">737 / 1000 (74 %)</td>
    <td style="white-space: nowrap;">391 / 1000 (39 %)</td>
    <td style="white-space: nowrap;">283 / 1000 (28 %)</td>
    <td style="white-space: nowrap;">526 / 1000 (53 %)</td>
    <td style="white-space: nowrap;">476 / 1000 (48 %)</td>
    <td style="white-space: nowrap;">363 / 1000 (36 %)</td>
    <td style="white-space: nowrap;">397 / 1000 (40 %)</td>
    <td style="white-space: nowrap;">394 / 1000 (39 %)</td>
    <td style="white-space: nowrap;">5267 / 11612 (45 %)</td>
</tr>
</table>

## without the center leaning class

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
    <th>Political podcasts</th>
    <th>Political tweets</th>
    <th>Qbias</th>
    <th>Webis bias flipper 18</th>
    <th>Webis news bias 20</th>
    <th>average</th>
</tr>
<tr>
    <th style="white-space: nowrap;">BertPoliticalBiasFinetune</th>
    <td style="white-space: nowrap;">487 / 1000 (49 %)</td>
    <td style="white-space: nowrap;">602 / 1000 (60 %)</td>
    <td style="white-space: nowrap;">492 / 1000 (49 %)</td>
    <td style="white-space: nowrap;">185 / 434 (43 %)</td>
    <td style="white-space: nowrap;">502 / 1000 (50 %)</td>
    <td style="white-space: nowrap;">597 / 1000 (60 %)</td>
    <td style="white-space: nowrap;">483 / 1000 (48 %)</td>
    <td style="white-space: nowrap;">494 / 1000 (49 %)</td>
    <td style="white-space: nowrap;">499 / 1000 (50 %)</td>
    <td style="white-space: nowrap;">557 / 1000 (56 %)</td>
    <td style="white-space: nowrap;">438 / 1000 (44 %)</td>
    <td style="white-space: nowrap;">545 / 1000 (55 %)</td>
    <td style="white-space: nowrap;">5881 / 11434 (51 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">PoliticalIdeologiesRobertaFinetuned</th>
    <td style="white-space: nowrap;">526 / 1000 (53 %)</td>
    <td style="white-space: nowrap;">397 / 1000 (40 %)</td>
    <td style="white-space: nowrap;">628 / 1000 (63 %)</td>
    <td style="white-space: nowrap;">352 / 434 (81 %)</td>
    <td style="white-space: nowrap;">991 / 1000 (99 %)</td>
    <td style="white-space: nowrap;">476 / 1000 (48 %)</td>
    <td style="white-space: nowrap;">553 / 1000 (55 %)</td>
    <td style="white-space: nowrap;">590 / 1000 (59 %)</td>
    <td style="white-space: nowrap;">628 / 1000 (63 %)</td>
    <td style="white-space: nowrap;">494 / 1000 (49 %)</td>
    <td style="white-space: nowrap;">543 / 1000 (54 %)</td>
    <td style="white-space: nowrap;">512 / 1000 (51 %)</td>
    <td style="white-space: nowrap;">6690 / 11434 (59 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">DebertaPoliticalClassification</th>
    <td style="white-space: nowrap;">659 / 1000 (66 %)</td>
    <td style="white-space: nowrap;">552 / 1000 (55 %)</td>
    <td style="white-space: nowrap;">624 / 1000 (62 %)</td>
    <td style="white-space: nowrap;">253 / 434 (58 %)</td>
    <td style="white-space: nowrap;">692 / 1000 (69 %)</td>
    <td style="white-space: nowrap;">640 / 1000 (64 %)</td>
    <td style="white-space: nowrap;">980 / 1000 (98 %)</td>
    <td style="white-space: nowrap;">749 / 1000 (75 %)</td>
    <td style="white-space: nowrap;">554 / 1000 (55 %)</td>
    <td style="white-space: nowrap;">512 / 1000 (51 %)</td>
    <td style="white-space: nowrap;">570 / 1000 (57 %)</td>
    <td style="white-space: nowrap;">635 / 1000 (64 %)</td>
    <td style="white-space: nowrap;">7420 / 11434 (65 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">DistilBertPoliticalTweets</th>
    <td style="white-space: nowrap;">569 / 1000 (57 %)</td>
    <td style="white-space: nowrap;">647 / 1000 (65 %)</td>
    <td style="white-space: nowrap;">623 / 1000 (62 %)</td>
    <td style="white-space: nowrap;">326 / 434 (75 %)</td>
    <td style="white-space: nowrap;">822 / 1000 (82 %)</td>
    <td style="white-space: nowrap;">592 / 1000 (59 %)</td>
    <td style="white-space: nowrap;">457 / 1000 (46 %)</td>
    <td style="white-space: nowrap;">664 / 1000 (66 %)</td>
    <td style="white-space: nowrap;">844 / 1000 (84 %)</td>
    <td style="white-space: nowrap;">516 / 1000 (52 %)</td>
    <td style="white-space: nowrap;">521 / 1000 (52 %)</td>
    <td style="white-space: nowrap;">546 / 1000 (55 %)</td>
    <td style="white-space: nowrap;">7127 / 11434 (62 %)</td>
</tr>
</table>

# Evaluation of existing models

DistilBertPoliticalBias and PoliticalIdeologiesRobertaFinetuned are in fact trained to predict conservative vs. liberal
leaning. That output has been mapped to right vs. left respectively. The same applies for DistilBertPoliticalTweets,
which is trained to predict republican vs. democratic.

DistilBertPoliticalBias uses a 5-level spectrum, which has been reduced to a 3-level one.

PoliticalDebateLarge is an NLI classifier and has been supplied a simple hypothesis "This text supports {} political
leaning.", which may not be optimal, because no rigorous testing has been done beforehand.

According to their Hugging Face model cards, some models have been trained on some of the collected datasets. These
relationships are shown in the following table.

<table>
<tr>
    <th>model</th>
    <th>trained on</th>
</tr>
<tr>
    <td>PoliticalBiasBert</td>
    <td>(probably) Article bias prediction</td>
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

This gets reflected by the accuracy results: the models score very high on the datasets they've been trained on.

The measurements have been conducted using the methodology prescribed in [this document](../../analysis/model_evaluation) while the
datasets have been sampled to 1 000 articles each.

The resulting accuracies are recorded in the two tables below.

## With a center leaning class

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
    <th>PoliticalBiasBert</th>
    <td>693 / 1000 (69 %)</td>
    <td>497 / 1000 (50 %)</td>
    <td>441 / 1000 (44 %)</td>
    <td>190 / 612 (31 %)</td>
    <td>425 / 1000 (42 %)</td>
    <td>379 / 1000 (38 %)</td>
    <td>423 / 1000 (42 %)</td>
    <td>428 / 1000 (43 %)</td>
    <td>456 / 1000 (46 %)</td>
    <td>399 / 1000 (40 %)</td>
    <td>458 / 1000 (46 %)</td>
    <td>543 / 1000 (54 %)</td>
    <td>5332 / 11612 (46 %)</td>
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
    <td>758 / 1000 (76 %)</td>
    <td>585 / 1000 (58 %)</td>
    <td>521 / 1000 (52 %)</td>
    <td>685 / 1000 (68 %)</td>
    <td>756 / 1000 (76 %)</td>
    <td>7282 / 11612 (63 %)</td>
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
    <td>497 / 1000 (50 %)</td>
    <td>440 / 1000 (44 %)</td>
    <td>340 / 1000 (34 %)</td>
    <td>427 / 1000 (43 %)</td>
    <td>386 / 1000 (39 %)</td>
    <td>5242 / 11612 (45 %)</td>
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
    <td>444 / 1000 (44 %)</td>
    <td>492 / 1000 (49 %)</td>
    <td>454 / 1000 (45 %)</td>
    <td>356 / 1000 (36 %)</td>
    <td>383 / 1000 (38 %)</td>
    <td>5009 / 11612 (43 %)</td>
</tr>
<tr>
    <th>PoliticalDebateLarge</th>
    <td>473 / 1000 (47 %)</td>
    <td>368 / 1000 (37 %)</td>
    <td>492 / 1000 (49 %)</td>
    <td>367 / 612 (60 %)</td>
    <td>737 / 1000 (74 %)</td>
    <td>391 / 1000 (39 %)</td>
    <td>283 / 1000 (28 %)</td>
    <td>526 / 1000 (53 %)</td>
    <td>476 / 1000 (48 %)</td>
    <td>363 / 1000 (36 %)</td>
    <td>397 / 1000 (40 %)</td>
    <td>394 / 1000 (39 %)</td>
    <td>5267 / 11612 (45 %)</td>
</tr>
</table>

## Without a center leaning class

<table>
<tr>
    <th>BertPoliticalBiasFinetune</th>
    <td>487 / 1000 (49 %)</td>
    <td>602 / 1000 (60 %)</td>
    <td>492 / 1000 (49 %)</td>
    <td>185 / 434 (43 %)</td>
    <td>502 / 1000 (50 %)</td>
    <td>597 / 1000 (60 %)</td>
    <td>483 / 1000 (48 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>499 / 1000 (50 %)</td>
    <td>557 / 1000 (56 %)</td>
    <td>438 / 1000 (44 %)</td>
    <td>545 / 1000 (55 %)</td>
    <td>5881 / 11434 (51 %)</td>
</tr>
<tr>
    <th>PoliticalIdeologiesRobertaFinetuned</th>
    <td>526 / 1000 (53 %)</td>
    <td>397 / 1000 (40 %)</td>
    <td>628 / 1000 (63 %)</td>
    <td>352 / 434 (81 %)</td>
    <td>991 / 1000 (99 %)</td>
    <td>476 / 1000 (48 %)</td>
    <td>553 / 1000 (55 %)</td>
    <td>590 / 1000 (59 %)</td>
    <td>628 / 1000 (63 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>543 / 1000 (54 %)</td>
    <td>512 / 1000 (51 %)</td>
    <td>6690 / 11434 (59 %)</td>
</tr>
<tr>
    <th>DebertaPoliticalClassification</th>
    <td>659 / 1000 (66 %)</td>
    <td>552 / 1000 (55 %)</td>
    <td>624 / 1000 (62 %)</td>
    <td>253 / 434 (58 %)</td>
    <td>692 / 1000 (69 %)</td>
    <td>640 / 1000 (64 %)</td>
    <td>980 / 1000 (98 %)</td>
    <td>749 / 1000 (75 %)</td>
    <td>554 / 1000 (55 %)</td>
    <td>512 / 1000 (51 %)</td>
    <td>570 / 1000 (57 %)</td>
    <td>635 / 1000 (64 %)</td>
    <td>7420 / 11434 (65 %)</td>
</tr>
<tr>
    <th>DistilBertPoliticalTweets</th>
    <td>569 / 1000 (57 %)</td>
    <td>647 / 1000 (65 %)</td>
    <td>623 / 1000 (62 %)</td>
    <td>326 / 434 (75 %)</td>
    <td>822 / 1000 (82 %)</td>
    <td>592 / 1000 (59 %)</td>
    <td>457 / 1000 (46 %)</td>
    <td>664 / 1000 (66 %)</td>
    <td>844 / 1000 (84 %)</td>
    <td>516 / 1000 (52 %)</td>
    <td>521 / 1000 (52 %)</td>
    <td>546 / 1000 (55 %)</td>
    <td>7127 / 11434 (62 %)</td>
</tr>
</table>

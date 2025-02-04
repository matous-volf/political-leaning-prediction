# Leave-one-in dataset benchmark

From each dataset, a sample of 1 000 rows (or less if the dataset is smaller) has been taken while ensuring an equal
distribution of leaning and systematically sampling by the body length. Several models have been fine-tuned separately
on each of these samples to compare the suitability of the datasets for training.

The fine-tuned models can be reproduced using [this notebook](../../../analysis/dataset_benchmark/leave_one_in/notebook.ipynb).

Then the models have been evaluated using the methodology prescribed in [this document](../../../analysis/model_evaluation), while
the datasets have been sampled to 1 000 rows each. The resulting accuracies are recorded in the tables below, rows
being models and columns being datasets. The heading of the row means the dataset the model has been fine-tuned on,
while the heading of the column is the dataset being evaluated on.

The average accuracy does not include the resulting accuracy on the dataset the model has been fine-tuned on (the
diagonal), as that may be misleading. Models fine-tuned on datasets containing only left and right classes are moved
into a separate table, since their accuracy is probabilistically higher.

## BERT base (cased)

### With a center leaning class

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
    <th>Article bias prediction</th>
    <td>534 / 1000 (53 %)</td>
    <td>475 / 1000 (48 %)</td>
    <td>490 / 1000 (49 %)</td>
    <td>190 / 612 (31 %)</td>
    <td>521 / 1000 (52 %)</td>
    <td>426 / 1000 (43 %)</td>
    <td>481 / 1000 (48 %)</td>
    <td>511 / 1000 (51 %)</td>
    <td>502 / 1000 (50 %)</td>
    <td>364 / 1000 (36 %)</td>
    <td>426 / 1000 (43 %)</td>
    <td>505 / 1000 (50 %)</td>
    <td>4891 / 10612 (46 %)</td>
</tr>
<tr>
    <th>CommonCrawl news articles</th>
    <td>349 / 1000 (35 %)</td>
    <td>652 / 1000 (65 %)</td>
    <td>90 / 1000 (9 %)</td>
    <td>178 / 612 (29 %)</td>
    <td>166 / 1000 (17 %)</td>
    <td>426 / 1000 (43 %)</td>
    <td>250 / 1000 (25 %)</td>
    <td>400 / 1000 (40 %)</td>
    <td>353 / 1000 (35 %)</td>
    <td>271 / 1000 (27 %)</td>
    <td>386 / 1000 (39 %)</td>
    <td>457 / 1000 (46 %)</td>
    <td>3326 / 10612 (31 %)</td>
</tr>
<tr>
    <th>GPT-4 political bias</th>
    <td>340 / 1000 (34 %)</td>
    <td>321 / 1000 (32 %)</td>
    <td>438 / 1000 (44 %)</td>
    <td>587 / 612 (96 %)</td>
    <td>457 / 1000 (46 %)</td>
    <td>379 / 1000 (38 %)</td>
    <td>269 / 1000 (27 %)</td>
    <td>343 / 1000 (34 %)</td>
    <td>447 / 1000 (45 %)</td>
    <td>329 / 1000 (33 %)</td>
    <td>415 / 1000 (42 %)</td>
    <td>369 / 1000 (37 %)</td>
    <td>4107 / 11000 (37 %)</td>
</tr>
<tr>
    <th>Qbias</th>
    <td>370 / 1000 (37 %)</td>
    <td>321 / 1000 (32 %)</td>
    <td>530 / 1000 (53 %)</td>
    <td>175 / 612 (29 %)</td>
    <td>481 / 1000 (48 %)</td>
    <td>213 / 1000 (21 %)</td>
    <td>359 / 1000 (36 %)</td>
    <td>409 / 1000 (41 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>416 / 1000 (42 %)</td>
    <td>369 / 1000 (37 %)</td>
    <td>369 / 1000 (37 %)</td>
    <td>4090 / 10612 (39 %)</td>
</tr>
<tr>
    <th>Webis bias flipper 18</th>
    <td>375 / 1000 (38 %)</td>
    <td>435 / 1000 (44 %)</td>
    <td>481 / 1000 (48 %)</td>
    <td>228 / 612 (37 %)</td>
    <td>501 / 1000 (50 %)</td>
    <td>498 / 1000 (50 %)</td>
    <td>458 / 1000 (46 %)</td>
    <td>286 / 1000 (29 %)</td>
    <td>526 / 1000 (53 %)</td>
    <td>429 / 1000 (43 %)</td>
    <td>729 / 1000 (73 %)</td>
    <td>490 / 1000 (49 %)</td>
    <td>4707 / 10612 (44 %)</td>
</tr>
<tr>
    <th>Webis news bias 20</th>
    <td>428 / 1000 (43 %)</td>
    <td>415 / 1000 (42 %)</td>
    <td>496 / 1000 (50 %)</td>
    <td>249 / 612 (41 %)</td>
    <td>492 / 1000 (49 %)</td>
    <td>340 / 1000 (34 %)</td>
    <td>491 / 1000 (49 %)</td>
    <td>479 / 1000 (48 %)</td>
    <td>467 / 1000 (47 %)</td>
    <td>298 / 1000 (30 %)</td>
    <td>401 / 1000 (40 %)</td>
    <td>565 / 1000 (56 %)</td>
    <td>4556 / 10612 (43 %)</td>
</tr>
</table>

### Without a center leaning class

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
    <th>Dem., rep. party platform topics</th>
    <td>487 / 1000 (49 %)</td>
    <td>613 / 1000 (61 %)</td>
    <td>735 / 1000 (74 %)</td>
    <td>282 / 434 (65 %)</td>
    <td>659 / 1000 (66 %)</td>
    <td>597 / 1000 (60 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>509 / 1000 (51 %)</td>
    <td>565 / 1000 (56 %)</td>
    <td>528 / 1000 (53 %)</td>
    <td>438 / 1000 (44 %)</td>
    <td>533 / 1000 (53 %)</td>
    <td>5705 / 10434 (55 %)</td>
</tr>
<tr>
    <th>GPT-4 political ideologies</th>
    <td>530 / 1000 (53 %)</td>
    <td>408 / 1000 (41 %)</td>
    <td>601 / 1000 (60 %)</td>
    <td>322 / 434 (74 %)</td>
    <td>979 / 1000 (98 %)</td>
    <td>467 / 1000 (47 %)</td>
    <td>556 / 1000 (56 %)</td>
    <td>519 / 1000 (52 %)</td>
    <td>594 / 1000 (59 %)</td>
    <td>465 / 1000 (46 %)</td>
    <td>523 / 1000 (52 %)</td>
    <td>497 / 1000 (50 %)</td>
    <td>5482 / 10434 (53 %)</td>
</tr>
<tr>
    <th>Media political stance</th>
    <td>598 / 1000 (60 %)</td>
    <td>549 / 1000 (55 %)</td>
    <td>521 / 1000 (52 %)</td>
    <td>241 / 434 (56 %)</td>
    <td>489 / 1000 (49 %)</td>
    <td>776 / 1000 (78 %)</td>
    <td>517 / 1000 (52 %)</td>
    <td>572 / 1000 (57 %)</td>
    <td>469 / 1000 (47 %)</td>
    <td>558 / 1000 (56 %)</td>
    <td>574 / 1000 (57 %)</td>
    <td>575 / 1000 (57 %)</td>
    <td>5663 / 10434 (54 %)</td>
</tr>
<tr>
    <th>Parliament speeches 2024</th>
    <td>486 / 1000 (49 %)</td>
    <td>593 / 1000 (59 %)</td>
    <td>507 / 1000 (51 %)</td>
    <td>199 / 434 (46 %)</td>
    <td>521 / 1000 (52 %)</td>
    <td>600 / 1000 (60 %)</td>
    <td>701 / 1000 (70 %)</td>
    <td>524 / 1000 (52 %)</td>
    <td>435 / 1000 (44 %)</td>
    <td>558 / 1000 (56 %)</td>
    <td>437 / 1000 (44 %)</td>
    <td>537 / 1000 (54 %)</td>
    <td>5397 / 10434 (52 %)</td>
</tr>
<tr>
    <th>Political podcasts</th>
    <td>553 / 1000 (55 %)</td>
    <td>498 / 1000 (50 %)</td>
    <td>516 / 1000 (52 %)</td>
    <td>250 / 434 (58 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>545 / 1000 (55 %)</td>
    <td>514 / 1000 (51 %)</td>
    <td>978 / 1000 (98 %)</td>
    <td>469 / 1000 (47 %)</td>
    <td>460 / 1000 (46 %)</td>
    <td>476 / 1000 (48 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>5281 / 10434 (51 %)</td>
</tr>
<tr>
    <th>Political tweets</th>
    <td>505 / 1000 (50 %)</td>
    <td>546 / 1000 (55 %)</td>
    <td>551 / 1000 (55 %)</td>
    <td>304 / 434 (70 %)</td>
    <td>621 / 1000 (62 %)</td>
    <td>499 / 1000 (50 %)</td>
    <td>457 / 1000 (46 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>689 / 1000 (69 %)</td>
    <td>486 / 1000 (49 %)</td>
    <td>541 / 1000 (54 %)</td>
    <td>505 / 1000 (50 %)</td>
    <td>5521 / 10434 (53 %)</td>
</tr>
</table>

## RoBERTa base

### With a center leaning class

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
    <th>Article bias prediction</th>
    <td>354 / 1000 (35 %)</td>
    <td>525 / 1000 (52 %)</td>
    <td>484 / 1000 (48 %)</td>
    <td>184 / 612 (30 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>607 / 1000 (61 %)</td>
    <td>487 / 1000 (49 %)</td>
    <td>489 / 1000 (49 %)</td>
    <td>530 / 1000 (53 %)</td>
    <td>474 / 1000 (47 %)</td>
    <td>365 / 1000 (36 %)</td>
    <td>438 / 1000 (44 %)</td>
    <td>5089 / 10612 (48 %)</td>
</tr>
<tr>
    <th>CommonCrawl news articles</th>
    <td>472 / 1000 (47 %)</td>
    <td>760 / 1000 (76 %)</td>
    <td>208 / 1000 (21 %)</td>
    <td>181 / 612 (30 %)</td>
    <td>307 / 1000 (31 %)</td>
    <td>464 / 1000 (46 %)</td>
    <td>314 / 1000 (31 %)</td>
    <td>532 / 1000 (53 %)</td>
    <td>483 / 1000 (48 %)</td>
    <td>307 / 1000 (31 %)</td>
    <td>393 / 1000 (39 %)</td>
    <td>559 / 1000 (56 %)</td>
    <td>4220 / 10612 (40 %)</td>
</tr>
<tr>
    <th>GPT-4 political bias</th>
    <td>353 / 1000 (35 %)</td>
    <td>334 / 1000 (33 %)</td>
    <td>456 / 1000 (46 %)</td>
    <td>581 / 612 (95 %)</td>
    <td>594 / 1000 (59 %)</td>
    <td>434 / 1000 (43 %)</td>
    <td>181 / 1000 (18 %)</td>
    <td>521 / 1000 (52 %)</td>
    <td>604 / 1000 (60 %)</td>
    <td>358 / 1000 (36 %)</td>
    <td>420 / 1000 (42 %)</td>
    <td>393 / 1000 (39 %)</td>
    <td>4648 / 11000 (42 %)</td>
</tr>
<tr>
    <th>Qbias</th>
    <td>354 / 1000 (35 %)</td>
    <td>505 / 1000 (50 %)</td>
    <td>484 / 1000 (48 %)</td>
    <td>184 / 612 (30 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>606 / 1000 (61 %)</td>
    <td>486 / 1000 (49 %)</td>
    <td>491 / 1000 (49 %)</td>
    <td>526 / 1000 (53 %)</td>
    <td>474 / 1000 (47 %)</td>
    <td>365 / 1000 (36 %)</td>
    <td>437 / 1000 (44 %)</td>
    <td>4944 / 10612 (47 %)</td>
</tr>
<tr>
    <th>Webis bias flipper 18</th>
    <td>459 / 1000 (46 %)</td>
    <td>414 / 1000 (41 %)</td>
    <td>456 / 1000 (46 %)</td>
    <td>189 / 612 (31 %)</td>
    <td>536 / 1000 (54 %)</td>
    <td>529 / 1000 (53 %)</td>
    <td>452 / 1000 (45 %)</td>
    <td>608 / 1000 (61 %)</td>
    <td>480 / 1000 (48 %)</td>
    <td>426 / 1000 (43 %)</td>
    <td>794 / 1000 (79 %)</td>
    <td>582 / 1000 (58 %)</td>
    <td>5131 / 10612 (48 %)</td>
</tr>
<tr>
    <th>Webis news bias 20</th>
    <td>457 / 1000 (46 %)</td>
    <td>514 / 1000 (51 %)</td>
    <td>223 / 1000 (22 %)</td>
    <td>174 / 612 (28 %)</td>
    <td>8 / 1000 (1 %)</td>
    <td>432 / 1000 (43 %)</td>
    <td>466 / 1000 (47 %)</td>
    <td>511 / 1000 (51 %)</td>
    <td>431 / 1000 (43 %)</td>
    <td>357 / 1000 (36 %)</td>
    <td>524 / 1000 (52 %)</td>
    <td>775 / 1000 (78 %)</td>
    <td>4097 / 10612 (39 %)</td>
</tr>
</table>

### Without a center leaning class

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
    <th>Dem., rep. party platform topics</th>
    <td>498 / 1000 (50 %)</td>
    <td>618 / 1000 (62 %)</td>
    <td>719 / 1000 (72 %)</td>
    <td>330 / 434 (76 %)</td>
    <td>805 / 1000 (80 %)</td>
    <td>596 / 1000 (60 %)</td>
    <td>491 / 1000 (49 %)</td>
    <td>557 / 1000 (56 %)</td>
    <td>605 / 1000 (60 %)</td>
    <td>525 / 1000 (52 %)</td>
    <td>451 / 1000 (45 %)</td>
    <td>544 / 1000 (54 %)</td>
    <td>6020 / 10434 (58 %)</td>
</tr>
<tr>
    <th>GPT-4 political ideologies</th>
    <td>528 / 1000 (53 %)</td>
    <td>371 / 1000 (37 %)</td>
    <td>616 / 1000 (62 %)</td>
    <td>352 / 434 (81 %)</td>
    <td>981 / 1000 (98 %)</td>
    <td>448 / 1000 (45 %)</td>
    <td>565 / 1000 (56 %)</td>
    <td>577 / 1000 (58 %)</td>
    <td>624 / 1000 (62 %)</td>
    <td>454 / 1000 (45 %)</td>
    <td>548 / 1000 (55 %)</td>
    <td>492 / 1000 (49 %)</td>
    <td>5575 / 10434 (53 %)</td>
</tr>
<tr>
    <th>Media political stance</th>
    <td>656 / 1000 (66 %)</td>
    <td>620 / 1000 (62 %)</td>
    <td>531 / 1000 (53 %)</td>
    <td>186 / 434 (43 %)</td>
    <td>557 / 1000 (56 %)</td>
    <td>837 / 1000 (84 %)</td>
    <td>510 / 1000 (51 %)</td>
    <td>623 / 1000 (62 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>608 / 1000 (61 %)</td>
    <td>616 / 1000 (62 %)</td>
    <td>594 / 1000 (59 %)</td>
    <td>5995 / 10434 (57 %)</td>
</tr>
<tr>
    <th>Parliament speeches 2024</th>
    <td>485 / 1000 (48 %)</td>
    <td>634 / 1000 (63 %)</td>
    <td>484 / 1000 (48 %)</td>
    <td>184 / 434 (42 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>605 / 1000 (60 %)</td>
    <td>585 / 1000 (58 %)</td>
    <td>487 / 1000 (49 %)</td>
    <td>530 / 1000 (53 %)</td>
    <td>565 / 1000 (56 %)</td>
    <td>436 / 1000 (44 %)</td>
    <td>536 / 1000 (54 %)</td>
    <td>5452 / 10434 (52 %)</td>
</tr>
<tr>
    <th>Political podcasts</th>
    <td>572 / 1000 (57 %)</td>
    <td>608 / 1000 (61 %)</td>
    <td>520 / 1000 (52 %)</td>
    <td>248 / 434 (57 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>623 / 1000 (62 %)</td>
    <td>512 / 1000 (51 %)</td>
    <td>989 / 1000 (99 %)</td>
    <td>472 / 1000 (47 %)</td>
    <td>548 / 1000 (55 %)</td>
    <td>470 / 1000 (47 %)</td>
    <td>540 / 1000 (54 %)</td>
    <td>5607 / 10434 (54 %)</td>
</tr>
<tr>
    <th>Political tweets</th>
    <td>535 / 1000 (54 %)</td>
    <td>529 / 1000 (53 %)</td>
    <td>522 / 1000 (52 %)</td>
    <td>198 / 434 (46 %)</td>
    <td>519 / 1000 (52 %)</td>
    <td>497 / 1000 (50 %)</td>
    <td>468 / 1000 (47 %)</td>
    <td>571 / 1000 (57 %)</td>
    <td>681 / 1000 (68 %)</td>
    <td>489 / 1000 (49 %)</td>
    <td>523 / 1000 (52 %)</td>
    <td>523 / 1000 (52 %)</td>
    <td>5374 / 10434 (52 %)</td>
</tr>
</table>

## POLITICS

### With a center leaning class

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
    <th>Article bias prediction</th>
    <td>765 / 1000 (76 %)</td>
    <td>548 / 1000 (55 %)</td>
    <td>529 / 1000 (53 %)</td>
    <td>173 / 612 (28 %)</td>
    <td>501 / 1000 (50 %)</td>
    <td>505 / 1000 (50 %)</td>
    <td>472 / 1000 (47 %)</td>
    <td>534 / 1000 (53 %)</td>
    <td>505 / 1000 (50 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>652 / 1000 (65 %)</td>
    <td>743 / 1000 (74 %)</td>
    <td>5656 / 10612 (53 %)</td>
</tr>
<tr>
    <th>CommonCrawl news articles</th>
    <td>493 / 1000 (49 %)</td>
    <td>771 / 1000 (77 %)</td>
    <td>67 / 1000 (7 %)</td>
    <td>172 / 612 (28 %)</td>
    <td>234 / 1000 (23 %)</td>
    <td>441 / 1000 (44 %)</td>
    <td>174 / 1000 (17 %)</td>
    <td>626 / 1000 (63 %)</td>
    <td>473 / 1000 (47 %)</td>
    <td>349 / 1000 (35 %)</td>
    <td>502 / 1000 (50 %)</td>
    <td>610 / 1000 (61 %)</td>
    <td>4141 / 10612 (39 %)</td>
</tr>
<tr>
    <th>GPT-4 political bias</th>
    <td>373 / 1000 (37 %)</td>
    <td>382 / 1000 (38 %)</td>
    <td>575 / 1000 (57 %)</td>
    <td>596 / 612 (97 %)</td>
    <td>733 / 1000 (73 %)</td>
    <td>435 / 1000 (44 %)</td>
    <td>242 / 1000 (24 %)</td>
    <td>579 / 1000 (58 %)</td>
    <td>601 / 1000 (60 %)</td>
    <td>373 / 1000 (37 %)</td>
    <td>429 / 1000 (43 %)</td>
    <td>405 / 1000 (40 %)</td>
    <td>5127 / 11000 (47 %)</td>
</tr>
<tr>
    <th>Qbias</th>
    <td>510 / 1000 (51 %)</td>
    <td>372 / 1000 (37 %)</td>
    <td>324 / 1000 (32 %)</td>
    <td>195 / 612 (32 %)</td>
    <td>315 / 1000 (32 %)</td>
    <td>329 / 1000 (33 %)</td>
    <td>54 / 1000 (5 %)</td>
    <td>449 / 1000 (45 %)</td>
    <td>375 / 1000 (38 %)</td>
    <td>508 / 1000 (51 %)</td>
    <td>632 / 1000 (63 %)</td>
    <td>635 / 1000 (64 %)</td>
    <td>4190 / 10612 (39 %)</td>
</tr>
<tr>
    <th>Webis bias flipper 18</th>
    <td>516 / 1000 (52 %)</td>
    <td>539 / 1000 (54 %)</td>
    <td>467 / 1000 (47 %)</td>
    <td>184 / 612 (30 %)</td>
    <td>538 / 1000 (54 %)</td>
    <td>498 / 1000 (50 %)</td>
    <td>360 / 1000 (36 %)</td>
    <td>538 / 1000 (54 %)</td>
    <td>537 / 1000 (54 %)</td>
    <td>510 / 1000 (51 %)</td>
    <td>880 / 1000 (88 %)</td>
    <td>650 / 1000 (65 %)</td>
    <td>5337 / 10612 (50 %)</td>
</tr>
<tr>
    <th>Webis news bias 20</th>
    <td>507 / 1000 (51 %)</td>
    <td>361 / 1000 (36 %)</td>
    <td>385 / 1000 (38 %)</td>
    <td>90 / 612 (15 %)</td>
    <td>348 / 1000 (35 %)</td>
    <td>487 / 1000 (49 %)</td>
    <td>307 / 1000 (31 %)</td>
    <td>586 / 1000 (59 %)</td>
    <td>424 / 1000 (42 %)</td>
    <td>451 / 1000 (45 %)</td>
    <td>633 / 1000 (63 %)</td>
    <td>822 / 1000 (82 %)</td>
    <td>4579 / 10612 (43 %)</td>
</tr>
</table>

### Without a center leaning class

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
    <th>Dem., rep. party platform topics</th>
    <td>545 / 1000 (55 %)</td>
    <td>640 / 1000 (64 %)</td>
    <td>762 / 1000 (76 %)</td>
    <td>344 / 434 (79 %)</td>
    <td>833 / 1000 (83 %)</td>
    <td>614 / 1000 (61 %)</td>
    <td>498 / 1000 (50 %)</td>
    <td>701 / 1000 (70 %)</td>
    <td>623 / 1000 (62 %)</td>
    <td>559 / 1000 (56 %)</td>
    <td>595 / 1000 (60 %)</td>
    <td>625 / 1000 (62 %)</td>
    <td>6577 / 10434 (63 %)</td>
</tr>
<tr>
    <th>GPT-4 political ideologies</th>
    <td>574 / 1000 (57 %)</td>
    <td>528 / 1000 (53 %)</td>
    <td>603 / 1000 (60 %)</td>
    <td>355 / 434 (82 %)</td>
    <td>985 / 1000 (98 %)</td>
    <td>537 / 1000 (54 %)</td>
    <td>541 / 1000 (54 %)</td>
    <td>699 / 1000 (70 %)</td>
    <td>652 / 1000 (65 %)</td>
    <td>488 / 1000 (49 %)</td>
    <td>606 / 1000 (61 %)</td>
    <td>553 / 1000 (55 %)</td>
    <td>6136 / 10434 (59 %)</td>
</tr>
<tr>
    <th>Media political stance</th>
    <td>737 / 1000 (74 %)</td>
    <td>740 / 1000 (74 %)</td>
    <td>535 / 1000 (54 %)</td>
    <td>198 / 434 (46 %)</td>
    <td>737 / 1000 (74 %)</td>
    <td>902 / 1000 (90 %)</td>
    <td>504 / 1000 (50 %)</td>
    <td>781 / 1000 (78 %)</td>
    <td>614 / 1000 (61 %)</td>
    <td>660 / 1000 (66 %)</td>
    <td>815 / 1000 (82 %)</td>
    <td>786 / 1000 (79 %)</td>
    <td>7107 / 10434 (68 %)</td>
</tr>
<tr>
    <th>Parliament speeches 2024</th>
    <td>512 / 1000 (51 %)</td>
    <td>517 / 1000 (52 %)</td>
    <td>511 / 1000 (51 %)</td>
    <td>250 / 434 (58 %)</td>
    <td>538 / 1000 (54 %)</td>
    <td>550 / 1000 (55 %)</td>
    <td>754 / 1000 (75 %)</td>
    <td>521 / 1000 (52 %)</td>
    <td>422 / 1000 (42 %)</td>
    <td>528 / 1000 (53 %)</td>
    <td>525 / 1000 (52 %)</td>
    <td>578 / 1000 (58 %)</td>
    <td>5452 / 10434 (52 %)</td>
</tr>
<tr>
    <th>Political podcasts</th>
    <td>656 / 1000 (66 %)</td>
    <td>668 / 1000 (67 %)</td>
    <td>523 / 1000 (52 %)</td>
    <td>254 / 434 (59 %)</td>
    <td>524 / 1000 (52 %)</td>
    <td>713 / 1000 (71 %)</td>
    <td>522 / 1000 (52 %)</td>
    <td>994 / 1000 (99 %)</td>
    <td>503 / 1000 (50 %)</td>
    <td>606 / 1000 (61 %)</td>
    <td>708 / 1000 (71 %)</td>
    <td>721 / 1000 (72 %)</td>
    <td>6398 / 10434 (61 %)</td>
</tr>
<tr>
    <th>Political tweets</th>
    <td>669 / 1000 (67 %)</td>
    <td>704 / 1000 (70 %)</td>
    <td>585 / 1000 (58 %)</td>
    <td>311 / 434 (72 %)</td>
    <td>735 / 1000 (74 %)</td>
    <td>649 / 1000 (65 %)</td>
    <td>467 / 1000 (47 %)</td>
    <td>729 / 1000 (73 %)</td>
    <td>751 / 1000 (75 %)</td>
    <td>580 / 1000 (58 %)</td>
    <td>729 / 1000 (73 %)</td>
    <td>715 / 1000 (72 %)</td>
    <td>6873 / 10434 (66 %)</td>
</tr>
</table>

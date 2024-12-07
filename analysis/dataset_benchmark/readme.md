# Dataset benchmark

From each dataset, a sample of 1 000 articles (or less if the dataset is smaller) has been taken while ensuring an equal
distribution of leaning and systematically sampling by the body length. Several models have been fine-tuned separately
on each of these samples to compare the suitability of the datasets for training.

The fine-tuned models can be reproduced using [this notebook](notebook.ipynb).

Then the models have been evaluated using the methodology prescribed in [this document](../model_evaluation), while the
datasets have been sampled to 1 000 articles each. The resulting accuracies are recorded in the tables below, rows being
models and columns being datasets. The heading of the row means the dataset the model has been fine-tuned on, while the
heading of the column is the dataset being evaluated on.

The average accuracy does not include the resulting accuracy on the dataset the model has been fine-tuned on, as that
may be misleading. Models fine-tuned on datasets containing only left and right classes are moved into a separate table,
since their accuracy is probabilistically higher.

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
    <th>PoliStance issue tweets</th>
    <th>Political tweets</th>
    <th>Qbias</th>
    <th>Webis bias flipper 18</th>
    <th>Webis news bias 20</th>
    <th>average</th>
</tr>
<tr>
    <th>Article bias prediction</th>
    <td>346 / 1000 (35 %)</td>
    <td>338 / 1000 (34 %)</td>
    <td>457 / 1000 (46 %)</td>
    <td>185 / 612 (30 %)</td>
    <td>507 / 1000 (51 %)</td>
    <td>168 / 1000 (17 %)</td>
    <td>217 / 1000 (22 %)</td>
    <td>537 / 1000 (54 %)</td>
    <td>496 / 1000 (50 %)</td>
    <td>415 / 1000 (42 %)</td>
    <td>265 / 1000 (26 %)</td>
    <td>245 / 1000 (24 %)</td>
    <td>3830 / 10612 (36 %)</td>
</tr>
<tr>
    <th>CommonCrawl news articles</th>
    <td>381 / 1000 (38 %)</td>
    <td>512 / 1000 (51 %)</td>
    <td>48 / 1000 (5 %)</td>
    <td>181 / 612 (30 %)</td>
    <td>2 / 1000 (0 %)</td>
    <td>410 / 1000 (41 %)</td>
    <td>126 / 1000 (13 %)</td>
    <td>224 / 1000 (22 %)</td>
    <td>261 / 1000 (26 %)</td>
    <td>230 / 1000 (23 %)</td>
    <td>350 / 1000 (35 %)</td>
    <td>389 / 1000 (39 %)</td>
    <td>2602 / 10612 (25 %)</td>
</tr>
<tr>
    <th>GPT-4 political bias</th>
    <td>357 / 1000 (36 %)</td>
    <td>497 / 1000 (50 %)</td>
    <td>202 / 1000 (20 %)</td>
    <td>449 / 612 (73 %)</td>
    <td>64 / 1000 (6 %)</td>
    <td>580 / 1000 (58 %)</td>
    <td>133 / 1000 (13 %)</td>
    <td>529 / 1000 (53 %)</td>
    <td>496 / 1000 (50 %)</td>
    <td>464 / 1000 (46 %)</td>
    <td>353 / 1000 (35 %)</td>
    <td>413 / 1000 (41 %)</td>
    <td>4088 / 11000 (37 %)</td>
</tr>
<tr>
    <th>Qbias</th>
    <td>350 / 1000 (35 %)</td>
    <td>457 / 1000 (46 %)</td>
    <td>503 / 1000 (50 %)</td>
    <td>227 / 612 (37 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>572 / 1000 (57 %)</td>
    <td>525 / 1000 (52 %)</td>
    <td>530 / 1000 (53 %)</td>
    <td>488 / 1000 (49 %)</td>
    <td>344 / 1000 (34 %)</td>
    <td>400 / 1000 (40 %)</td>
    <td>441 / 1000 (44 %)</td>
    <td>4987 / 10612 (47 %)</td>
</tr>
<tr>
    <th>Webis bias flipper 18</th>
    <td>408 / 1000 (41 %)</td>
    <td>420 / 1000 (42 %)</td>
    <td>503 / 1000 (50 %)</td>
    <td>238 / 612 (39 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>415 / 1000 (42 %)</td>
    <td>522 / 1000 (52 %)</td>
    <td>476 / 1000 (48 %)</td>
    <td>455 / 1000 (46 %)</td>
    <td>380 / 1000 (38 %)</td>
    <td>475 / 1000 (48 %)</td>
    <td>386 / 1000 (39 %)</td>
    <td>4697 / 10612 (44 %)</td>
</tr>
<tr>
    <th>Webis news bias 20</th>
    <td>380 / 1000 (38 %)</td>
    <td>434 / 1000 (43 %)</td>
    <td>484 / 1000 (48 %)</td>
    <td>184 / 612 (30 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>374 / 1000 (37 %)</td>
    <td>512 / 1000 (51 %)</td>
    <td>565 / 1000 (56 %)</td>
    <td>512 / 1000 (51 %)</td>
    <td>406 / 1000 (41 %)</td>
    <td>333 / 1000 (33 %)</td>
    <td>350 / 1000 (35 %)</td>
    <td>4690 / 10612 (44 %)</td>
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
    <th>PoliStance issue tweets</th>
    <th>Political tweets</th>
    <th>Qbias</th>
    <th>Webis bias flipper 18</th>
    <th>Webis news bias 20</th>
    <th>average</th>
</tr>
<tr>
    <th>Dem., rep. party platform topics</th>
    <td>498 / 1000 (50 %)</td>
    <td>367 / 1000 (37 %)</td>
    <td>538 / 1000 (54 %)</td>
    <td>250 / 434 (58 %)</td>
    <td>587 / 1000 (59 %)</td>
    <td>432 / 1000 (43 %)</td>
    <td>465 / 1000 (46 %)</td>
    <td>423 / 1000 (42 %)</td>
    <td>473 / 1000 (47 %)</td>
    <td>432 / 1000 (43 %)</td>
    <td>532 / 1000 (53 %)</td>
    <td>453 / 1000 (45 %)</td>
    <td>4912 / 10434 (47 %)</td>
</tr>
<tr>
    <th>GPT-4 political ideologies</th>
    <td>499 / 1000 (50 %)</td>
    <td>417 / 1000 (42 %)</td>
    <td>527 / 1000 (53 %)</td>
    <td>322 / 434 (74 %)</td>
    <td>858 / 1000 (86 %)</td>
    <td>451 / 1000 (45 %)</td>
    <td>520 / 1000 (52 %)</td>
    <td>579 / 1000 (58 %)</td>
    <td>537 / 1000 (54 %)</td>
    <td>566 / 1000 (57 %)</td>
    <td>525 / 1000 (52 %)</td>
    <td>501 / 1000 (50 %)</td>
    <td>5444 / 10434 (52 %)</td>
</tr>
<tr>
    <th>Media political stance</th>
    <td>505 / 1000 (50 %)</td>
    <td>477 / 1000 (48 %)</td>
    <td>529 / 1000 (53 %)</td>
    <td>248 / 434 (57 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>591 / 1000 (59 %)</td>
    <td>507 / 1000 (51 %)</td>
    <td>512 / 1000 (51 %)</td>
    <td>499 / 1000 (50 %)</td>
    <td>543 / 1000 (54 %)</td>
    <td>479 / 1000 (48 %)</td>
    <td>515 / 1000 (52 %)</td>
    <td>5308 / 10434 (51 %)</td>
</tr>
<tr>
    <th>Parliament speeches 2024</th>
    <td>511 / 1000 (51 %)</td>
    <td>519 / 1000 (52 %)</td>
    <td>507 / 1000 (51 %)</td>
    <td>184 / 434 (42 %)</td>
    <td>489 / 1000 (49 %)</td>
    <td>582 / 1000 (58 %)</td>
    <td>611 / 1000 (61 %)</td>
    <td>534 / 1000 (53 %)</td>
    <td>473 / 1000 (47 %)</td>
    <td>541 / 1000 (54 %)</td>
    <td>498 / 1000 (50 %)</td>
    <td>435 / 1000 (44 %)</td>
    <td>5273 / 10434 (51 %)</td>
</tr>
<tr>
    <th>PoliStance issue tweets</th>
    <td>512 / 1000 (51 %)</td>
    <td>386 / 1000 (39 %)</td>
    <td>550 / 1000 (55 %)</td>
    <td>186 / 434 (43 %)</td>
    <td>509 / 1000 (51 %)</td>
    <td>422 / 1000 (42 %)</td>
    <td>521 / 1000 (52 %)</td>
    <td>593 / 1000 (59 %)</td>
    <td>534 / 1000 (53 %)</td>
    <td>480 / 1000 (48 %)</td>
    <td>564 / 1000 (56 %)</td>
    <td>464 / 1000 (46 %)</td>
    <td>5128 / 10434 (49 %)</td>
</tr>
<tr>
    <th>Political tweets</th>
    <td>486 / 1000 (49 %)</td>
    <td>627 / 1000 (63 %)</td>
    <td>484 / 1000 (48 %)</td>
    <td>185 / 434 (43 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>608 / 1000 (61 %)</td>
    <td>487 / 1000 (49 %)</td>
    <td>556 / 1000 (56 %)</td>
    <td>533 / 1000 (53 %)</td>
    <td>559 / 1000 (56 %)</td>
    <td>440 / 1000 (44 %)</td>
    <td>537 / 1000 (54 %)</td>
    <td>5475 / 10434 (52 %)</td>
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
    <th>PoliStance issue tweets</th>
    <th>Political tweets</th>
    <th>Qbias</th>
    <th>Webis bias flipper 18</th>
    <th>Webis news bias 20</th>
    <th>average</th>
</tr>
<tr>
    <th>Article bias prediction</th>
    <td>331 / 1000 (33 %)</td>
    <td>367 / 1000 (37 %)</td>
    <td>479 / 1000 (48 %)</td>
    <td>184 / 612 (30 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>434 / 1000 (43 %)</td>
    <td>508 / 1000 (51 %)</td>
    <td>536 / 1000 (54 %)</td>
    <td>549 / 1000 (55 %)</td>
    <td>470 / 1000 (47 %)</td>
    <td>420 / 1000 (42 %)</td>
    <td>385 / 1000 (38 %)</td>
    <td>4838 / 10612 (46 %)</td>
</tr>
<tr>
    <th>CommonCrawl news articles</th>
    <td>367 / 1000 (37 %)</td>
    <td>585 / 1000 (58 %)</td>
    <td>313 / 1000 (31 %)</td>
    <td>192 / 612 (31 %)</td>
    <td>280 / 1000 (28 %)</td>
    <td>478 / 1000 (48 %)</td>
    <td>279 / 1000 (28 %)</td>
    <td>449 / 1000 (45 %)</td>
    <td>477 / 1000 (48 %)</td>
    <td>343 / 1000 (34 %)</td>
    <td>427 / 1000 (43 %)</td>
    <td>405 / 1000 (40 %)</td>
    <td>4010 / 10612 (38 %)</td>
</tr>
<tr>
    <th>GPT-4 political bias</th>
    <td>297 / 1000 (30 %)</td>
    <td>403 / 1000 (40 %)</td>
    <td>537 / 1000 (54 %)</td>
    <td>483 / 612 (79 %)</td>
    <td>750 / 1000 (75 %)</td>
    <td>480 / 1000 (48 %)</td>
    <td>270 / 1000 (27 %)</td>
    <td>749 / 1000 (75 %)</td>
    <td>569 / 1000 (57 %)</td>
    <td>432 / 1000 (43 %)</td>
    <td>364 / 1000 (36 %)</td>
    <td>403 / 1000 (40 %)</td>
    <td>5254 / 11000 (48 %)</td>
</tr>
<tr>
    <th>Qbias</th>
    <td>356 / 1000 (36 %)</td>
    <td>541 / 1000 (54 %)</td>
    <td>483 / 1000 (48 %)</td>
    <td>184 / 612 (30 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>611 / 1000 (61 %)</td>
    <td>486 / 1000 (49 %)</td>
    <td>589 / 1000 (59 %)</td>
    <td>525 / 1000 (52 %)</td>
    <td>472 / 1000 (47 %)</td>
    <td>365 / 1000 (36 %)</td>
    <td>444 / 1000 (44 %)</td>
    <td>5090 / 10612 (48 %)</td>
</tr>
<tr>
    <th>Webis bias flipper 18</th>
    <td>364 / 1000 (36 %)</td>
    <td>436 / 1000 (44 %)</td>
    <td>437 / 1000 (44 %)</td>
    <td>184 / 612 (30 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>574 / 1000 (57 %)</td>
    <td>483 / 1000 (48 %)</td>
    <td>534 / 1000 (53 %)</td>
    <td>490 / 1000 (49 %)</td>
    <td>468 / 1000 (47 %)</td>
    <td>419 / 1000 (42 %)</td>
    <td>434 / 1000 (43 %)</td>
    <td>4910 / 10612 (46 %)</td>
</tr>
<tr>
    <th>Webis news bias 20</th>
    <td>370 / 1000 (37 %)</td>
    <td>525 / 1000 (52 %)</td>
    <td>484 / 1000 (48 %)</td>
    <td>184 / 612 (30 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>607 / 1000 (61 %)</td>
    <td>487 / 1000 (49 %)</td>
    <td>582 / 1000 (58 %)</td>
    <td>532 / 1000 (53 %)</td>
    <td>474 / 1000 (47 %)</td>
    <td>371 / 1000 (37 %)</td>
    <td>488 / 1000 (49 %)</td>
    <td>5122 / 10612 (48 %)</td>
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
    <th>PoliStance issue tweets</th>
    <th>Political tweets</th>
    <th>Qbias</th>
    <th>Webis bias flipper 18</th>
    <th>Webis news bias 20</th>
    <th>average</th>
</tr>
<tr>
    <th>Dem., rep. party platform topics</th>
    <td>486 / 1000 (49 %)</td>
    <td>628 / 1000 (63 %)</td>
    <td>486 / 1000 (49 %)</td>
    <td>184 / 434 (42 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>551 / 1000 (55 %)</td>
    <td>491 / 1000 (49 %)</td>
    <td>580 / 1000 (58 %)</td>
    <td>530 / 1000 (53 %)</td>
    <td>554 / 1000 (55 %)</td>
    <td>439 / 1000 (44 %)</td>
    <td>466 / 1000 (47 %)</td>
    <td>5415 / 10434 (52 %)</td>
</tr>
<tr>
    <th>GPT-4 political ideologies</th>
    <td>492 / 1000 (49 %)</td>
    <td>410 / 1000 (41 %)</td>
    <td>554 / 1000 (55 %)</td>
    <td>328 / 434 (76 %)</td>
    <td>897 / 1000 (90 %)</td>
    <td>515 / 1000 (52 %)</td>
    <td>543 / 1000 (54 %)</td>
    <td>592 / 1000 (59 %)</td>
    <td>558 / 1000 (56 %)</td>
    <td>547 / 1000 (55 %)</td>
    <td>474 / 1000 (47 %)</td>
    <td>498 / 1000 (50 %)</td>
    <td>5511 / 10434 (53 %)</td>
</tr>
<tr>
    <th>Media political stance</th>
    <td>498 / 1000 (50 %)</td>
    <td>444 / 1000 (44 %)</td>
    <td>551 / 1000 (55 %)</td>
    <td>191 / 434 (44 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>573 / 1000 (57 %)</td>
    <td>488 / 1000 (49 %)</td>
    <td>507 / 1000 (51 %)</td>
    <td>493 / 1000 (49 %)</td>
    <td>565 / 1000 (56 %)</td>
    <td>498 / 1000 (50 %)</td>
    <td>509 / 1000 (51 %)</td>
    <td>5238 / 10434 (50 %)</td>
</tr>
<tr>
    <th>Parliament speeches 2024</th>
    <td>485 / 1000 (48 %)</td>
    <td>631 / 1000 (63 %)</td>
    <td>485 / 1000 (48 %)</td>
    <td>184 / 434 (42 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>607 / 1000 (61 %)</td>
    <td>508 / 1000 (51 %)</td>
    <td>580 / 1000 (58 %)</td>
    <td>530 / 1000 (53 %)</td>
    <td>565 / 1000 (56 %)</td>
    <td>438 / 1000 (44 %)</td>
    <td>534 / 1000 (53 %)</td>
    <td>5545 / 10434 (53 %)</td>
</tr>
<tr>
    <th>PoliStance issue tweets</th>
    <td>509 / 1000 (51 %)</td>
    <td>432 / 1000 (43 %)</td>
    <td>543 / 1000 (54 %)</td>
    <td>276 / 434 (64 %)</td>
    <td>603 / 1000 (60 %)</td>
    <td>501 / 1000 (50 %)</td>
    <td>556 / 1000 (56 %)</td>
    <td>865 / 1000 (86 %)</td>
    <td>508 / 1000 (51 %)</td>
    <td>513 / 1000 (51 %)</td>
    <td>509 / 1000 (51 %)</td>
    <td>488 / 1000 (49 %)</td>
    <td>5438 / 10434 (52 %)</td>
</tr>
<tr>
    <th>Political tweets</th>
    <td>486 / 1000 (49 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>484 / 1000 (48 %)</td>
    <td>188 / 434 (43 %)</td>
    <td>507 / 1000 (51 %)</td>
    <td>471 / 1000 (47 %)</td>
    <td>473 / 1000 (47 %)</td>
    <td>589 / 1000 (59 %)</td>
    <td>554 / 1000 (55 %)</td>
    <td>493 / 1000 (49 %)</td>
    <td>498 / 1000 (50 %)</td>
    <td>518 / 1000 (52 %)</td>
    <td>5213 / 10434 (50 %)</td>
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
    <th>PoliStance issue tweets</th>
    <th>Political tweets</th>
    <th>Qbias</th>
    <th>Webis bias flipper 18</th>
    <th>Webis news bias 20</th>
    <th>average</th>
</tr>
<tr>
    <td>Article bias prediction</td>
    <td>483 / 1000 (48 %)</td>
    <td>398 / 1000 (40 %)</td>
    <td>518 / 1000 (52 %)</td>
    <td>186 / 612 (30 %)</td>
    <td>548 / 1000 (55 %)</td>
    <td>458 / 1000 (46 %)</td>
    <td>538 / 1000 (54 %)</td>
    <td>520 / 1000 (52 %)</td>
    <td>495 / 1000 (50 %)</td>
    <td>424 / 1000 (42 %)</td>
    <td>486 / 1000 (49 %)</td>
    <td>460 / 1000 (46 %)</td>
    <td>5031 / 10612 (47 %)</td>
</tr>
<tr>
    <td>CommonCrawl news articles</td>
    <td>381 / 1000 (38 %)</td>
    <td>531 / 1000 (53 %)</td>
    <td>271 / 1000 (27 %)</td>
    <td>214 / 612 (35 %)</td>
    <td>398 / 1000 (40 %)</td>
    <td>375 / 1000 (38 %)</td>
    <td>106 / 1000 (11 %)</td>
    <td>445 / 1000 (44 %)</td>
    <td>436 / 1000 (44 %)</td>
    <td>331 / 1000 (33 %)</td>
    <td>392 / 1000 (39 %)</td>
    <td>376 / 1000 (38 %)</td>
    <td>3725 / 10612 (35 %)</td>
</tr>
<tr>
    <td>GPT-4 political bias</td>
    <td>335 / 1000 (34 %)</td>
    <td>371 / 1000 (37 %)</td>
    <td>376 / 1000 (38 %)</td>
    <td>511 / 612 (83 %)</td>
    <td>500 / 1000 (50 %)</td>
    <td>296 / 1000 (30 %)</td>
    <td>48 / 1000 (5 %)</td>
    <td>454 / 1000 (45 %)</td>
    <td>413 / 1000 (41 %)</td>
    <td>300 / 1000 (30 %)</td>
    <td>250 / 1000 (25 %)</td>
    <td>264 / 1000 (26 %)</td>
    <td>3607 / 11000 (33 %)</td>
</tr>
<tr>
    <td>Qbias</td>
    <td>422 / 1000 (42 %)</td>
    <td>496 / 1000 (50 %)</td>
    <td>475 / 1000 (48 %)</td>
    <td>161 / 612 (26 %)</td>
    <td>489 / 1000 (49 %)</td>
    <td>528 / 1000 (53 %)</td>
    <td>153 / 1000 (15 %)</td>
    <td>457 / 1000 (46 %)</td>
    <td>446 / 1000 (45 %)</td>
    <td>425 / 1000 (42 %)</td>
    <td>476 / 1000 (48 %)</td>
    <td>484 / 1000 (48 %)</td>
    <td>4587 / 10612 (43 %)</td>
</tr>
<tr>
    <td>Webis bias flipper 18</td>
    <td>464 / 1000 (46 %)</td>
    <td>470 / 1000 (47 %)</td>
    <td>451 / 1000 (45 %)</td>
    <td>213 / 612 (35 %)</td>
    <td>553 / 1000 (55 %)</td>
    <td>492 / 1000 (49 %)</td>
    <td>232 / 1000 (23 %)</td>
    <td>342 / 1000 (34 %)</td>
    <td>242 / 1000 (24 %)</td>
    <td>535 / 1000 (54 %)</td>
    <td>728 / 1000 (73 %)</td>
    <td>638 / 1000 (64 %)</td>
    <td>4632 / 10612 (44 %)</td>
</tr>
<tr>
    <td>Webis news bias 20</td>
    <td>466 / 1000 (47 %)</td>
    <td>546 / 1000 (55 %)</td>
    <td>516 / 1000 (52 %)</td>
    <td>214 / 612 (35 %)</td>
    <td>591 / 1000 (59 %)</td>
    <td>535 / 1000 (54 %)</td>
    <td>502 / 1000 (50 %)</td>
    <td>632 / 1000 (63 %)</td>
    <td>540 / 1000 (54 %)</td>
    <td>435 / 1000 (44 %)</td>
    <td>598 / 1000 (60 %)</td>
    <td>620 / 1000 (62 %)</td>
    <td>5575 / 10612 (53 %)</td>
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
  <th>PoliStance issue tweets</th>
  <th>Political tweets</th>
  <th>Qbias</th>
  <th>Webis bias flipper 18</th>
  <th>Webis news bias 20</th>
  <th>average</th>
</tr>
<tr>
    <td>Dem., rep. party platform topics</td>
    <td>498 / 1000 (50 %)</td>
    <td>563 / 1000 (56 %)</td>
    <td>609 / 1000 (61 %)</td>
    <td>235 / 434 (54 %)</td>
    <td>684 / 1000 (68 %)</td>
    <td>485 / 1000 (48 %)</td>
    <td>491 / 1000 (49 %)</td>
    <td>568 / 1000 (57 %)</td>
    <td>516 / 1000 (52 %)</td>
    <td>508 / 1000 (51 %)</td>
    <td>509 / 1000 (51 %)</td>
    <td>503 / 1000 (50 %)</td>
    <td>5560 / 10434 (53 %)</td>
</tr>
<tr>
    <td>GPT-4 political ideologies</td>
    <td>656 / 1000 (66 %)</td>
    <td>563 / 1000 (56 %)</td>
    <td>602 / 1000 (60 %)</td>
    <td>351 / 434 (81 %)</td>
    <td>937 / 1000 (94 %)</td>
    <td>577 / 1000 (58 %)</td>
    <td>553 / 1000 (55 %)</td>
    <td>657 / 1000 (66 %)</td>
    <td>652 / 1000 (65 %)</td>
    <td>526 / 1000 (53 %)</td>
    <td>711 / 1000 (71 %)</td>
    <td>685 / 1000 (68 %)</td>
    <td>6533 / 10434 (63 %)</td>
</tr>
<tr>
    <td>Media political stance</td>
    <td>672 / 1000 (67 %)</td>
    <td>763 / 1000 (76 %)</td>
    <td>522 / 1000 (52 %)</td>
    <td>187 / 434 (43 %)</td>
    <td>723 / 1000 (72 %)</td>
    <td>798 / 1000 (80 %)</td>
    <td>478 / 1000 (48 %)</td>
    <td>630 / 1000 (63 %)</td>
    <td>605 / 1000 (60 %)</td>
    <td>613 / 1000 (61 %)</td>
    <td>818 / 1000 (82 %)</td>
    <td>796 / 1000 (80 %)</td>
    <td>6807 / 10434 (65 %)</td>
</tr>
<tr>
    <td>Parliament speeches 2024</td>
    <td>550 / 1000 (55 %)</td>
    <td>537 / 1000 (54 %)</td>
    <td>524 / 1000 (52 %)</td>
    <td>240 / 434 (55 %)</td>
    <td>589 / 1000 (59 %)</td>
    <td>548 / 1000 (55 %)</td>
    <td>547 / 1000 (55 %)</td>
    <td>503 / 1000 (50 %)</td>
    <td>510 / 1000 (51 %)</td>
    <td>535 / 1000 (54 %)</td>
    <td>628 / 1000 (63 %)</td>
    <td>616 / 1000 (62 %)</td>
    <td>5780 / 10434 (55 %)</td>
</tr>
<tr>
    <td>PoliStance issue tweets</td>
    <td>569 / 1000 (57 %)</td>
    <td>482 / 1000 (48 %)</td>
    <td>555 / 1000 (56 %)</td>
    <td>280 / 434 (65 %)</td>
    <td>629 / 1000 (63 %)</td>
    <td>542 / 1000 (54 %)</td>
    <td>519 / 1000 (52 %)</td>
    <td>858 / 1000 (86 %)</td>
    <td>525 / 1000 (52 %)</td>
    <td>520 / 1000 (52 %)</td>
    <td>607 / 1000 (61 %)</td>
    <td>582 / 1000 (58 %)</td>
    <td>5810 / 10434 (56 %)</td>
</tr>
<tr>
    <td>Political tweets</td>
    <td>728 / 1000 (73 %)</td>
    <td>685 / 1000 (68 %)</td>
    <td>532 / 1000 (53 %)</td>
    <td>262 / 434 (60 %)</td>
    <td>591 / 1000 (59 %)</td>
    <td>643 / 1000 (64 %)</td>
    <td>432 / 1000 (43 %)</td>
    <td>637 / 1000 (64 %)</td>
    <td>677 / 1000 (68 %)</td>
    <td>594 / 1000 (59 %)</td>
    <td>778 / 1000 (78 %)</td>
    <td>792 / 1000 (79 %)</td>
    <td>6674 / 10434 (64 %)</td>
</tr>
</table>

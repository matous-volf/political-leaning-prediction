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
    <td>596 / 1000 (60 %)</td>
    <td>450 / 1000 (45 %)</td>
    <td>434 / 1000 (43 %)</td>
    <td>222 / 612 (36 %)</td>
    <td>468 / 1000 (47 %)</td>
    <td>320 / 1000 (32 %)</td>
    <td>453 / 1000 (45 %)</td>
    <td>479 / 1000 (48 %)</td>
    <td>464 / 1000 (46 %)</td>
    <td>363 / 1000 (36 %)</td>
    <td>360 / 1000 (36 %)</td>
    <td>452 / 1000 (45 %)</td>
    <td>4465 / 10612 (42 %)</td>
</tr>
<tr>
    <th>CommonCrawl news articles</th>
    <td>413 / 1000 (41 %)</td>
    <td>690 / 1000 (69 %)</td>
    <td>291 / 1000 (29 %)</td>
    <td>186 / 612 (30 %)</td>
    <td>469 / 1000 (47 %)</td>
    <td>427 / 1000 (43 %)</td>
    <td>383 / 1000 (38 %)</td>
    <td>364 / 1000 (36 %)</td>
    <td>422 / 1000 (42 %)</td>
    <td>332 / 1000 (33 %)</td>
    <td>415 / 1000 (42 %)</td>
    <td>489 / 1000 (49 %)</td>
    <td>4191 / 10612 (39 %)</td>
</tr>
<tr>
    <th>Dem., rep. party platform topics</th>
    <td>481 / 1000 (48 %)</td>
    <td>635 / 1000 (64 %)</td>
    <td>747 / 1000 (75 %)</td>
    <td>291 / 434 (67 %)</td>
    <td>652 / 1000 (65 %)</td>
    <td>598 / 1000 (60 %)</td>
    <td>487 / 1000 (49 %)</td>
    <td>582 / 1000 (58 %)</td>
    <td>562 / 1000 (56 %)</td>
    <td>537 / 1000 (54 %)</td>
    <td>441 / 1000 (44 %)</td>
    <td>532 / 1000 (53 %)</td>
    <td>5798 / 10434 (56 %)</td>
</tr>
<tr>
    <th>GPT-4 political bias</th>
    <td>346 / 1000 (35 %)</td>
    <td>324 / 1000 (32 %)</td>
    <td>565 / 1000 (56 %)</td>
    <td>569 / 612 (93 %)</td>
    <td>656 / 1000 (66 %)</td>
    <td>410 / 1000 (41 %)</td>
    <td>517 / 1000 (52 %)</td>
    <td>473 / 1000 (47 %)</td>
    <td>520 / 1000 (52 %)</td>
    <td>347 / 1000 (35 %)</td>
    <td>428 / 1000 (43 %)</td>
    <td>401 / 1000 (40 %)</td>
    <td>4987 / 11000 (45 %)</td>
</tr>
<tr>
    <th>GPT-4 political ideologies</th>
    <td>530 / 1000 (53 %)</td>
    <td>372 / 1000 (37 %)</td>
    <td>591 / 1000 (59 %)</td>
    <td>331 / 434 (76 %)</td>
    <td>980 / 1000 (98 %)</td>
    <td>451 / 1000 (45 %)</td>
    <td>551 / 1000 (55 %)</td>
    <td>603 / 1000 (60 %)</td>
    <td>562 / 1000 (56 %)</td>
    <td>482 / 1000 (48 %)</td>
    <td>570 / 1000 (57 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>5537 / 10434 (53 %)</td>
</tr>
<tr>
    <th>Media political stance</th>
    <td>560 / 1000 (56 %)</td>
    <td>574 / 1000 (57 %)</td>
    <td>537 / 1000 (54 %)</td>
    <td>185 / 434 (43 %)</td>
    <td>516 / 1000 (52 %)</td>
    <td>790 / 1000 (79 %)</td>
    <td>517 / 1000 (52 %)</td>
    <td>439 / 1000 (44 %)</td>
    <td>474 / 1000 (47 %)</td>
    <td>554 / 1000 (55 %)</td>
    <td>528 / 1000 (53 %)</td>
    <td>537 / 1000 (54 %)</td>
    <td>5421 / 10434 (52 %)</td>
</tr>
<tr>
    <th>Parliament speeches 2024</th>
    <td>490 / 1000 (49 %)</td>
    <td>564 / 1000 (56 %)</td>
    <td>544 / 1000 (54 %)</td>
    <td>185 / 434 (43 %)</td>
    <td>496 / 1000 (50 %)</td>
    <td>596 / 1000 (60 %)</td>
    <td>708 / 1000 (71 %)</td>
    <td>415 / 1000 (42 %)</td>
    <td>420 / 1000 (42 %)</td>
    <td>560 / 1000 (56 %)</td>
    <td>440 / 1000 (44 %)</td>
    <td>537 / 1000 (54 %)</td>
    <td>5247 / 10434 (50 %)</td>
</tr>
<tr>
    <th>PoliStance issue tweets</th>
    <td>504 / 1000 (50 %)</td>
    <td>451 / 1000 (45 %)</td>
    <td>556 / 1000 (56 %)</td>
    <td>310 / 434 (71 %)</td>
    <td>619 / 1000 (62 %)</td>
    <td>515 / 1000 (52 %)</td>
    <td>511 / 1000 (51 %)</td>
    <td>954 / 1000 (95 %)</td>
    <td>545 / 1000 (55 %)</td>
    <td>505 / 1000 (50 %)</td>
    <td>482 / 1000 (48 %)</td>
    <td>480 / 1000 (48 %)</td>
    <td>5478 / 10434 (53 %)</td>
</tr>
<tr>
    <th>Political tweets</th>
    <td>506 / 1000 (51 %)</td>
    <td>513 / 1000 (51 %)</td>
    <td>516 / 1000 (52 %)</td>
    <td>289 / 434 (67 %)</td>
    <td>550 / 1000 (55 %)</td>
    <td>479 / 1000 (48 %)</td>
    <td>438 / 1000 (44 %)</td>
    <td>602 / 1000 (60 %)</td>
    <td>692 / 1000 (69 %)</td>
    <td>472 / 1000 (47 %)</td>
    <td>569 / 1000 (57 %)</td>
    <td>492 / 1000 (49 %)</td>
    <td>5426 / 10434 (52 %)</td>
</tr>
<tr>
    <th>Qbias</th>
    <td>412 / 1000 (41 %)</td>
    <td>323 / 1000 (32 %)</td>
    <td>336 / 1000 (34 %)</td>
    <td>165 / 612 (27 %)</td>
    <td>330 / 1000 (33 %)</td>
    <td>197 / 1000 (20 %)</td>
    <td>366 / 1000 (37 %)</td>
    <td>433 / 1000 (43 %)</td>
    <td>419 / 1000 (42 %)</td>
    <td>462 / 1000 (46 %)</td>
    <td>410 / 1000 (41 %)</td>
    <td>447 / 1000 (45 %)</td>
    <td>3838 / 10612 (36 %)</td>
</tr>
<tr>
    <th>Webis bias flipper 18</th>
    <td>392 / 1000 (39 %)</td>
    <td>522 / 1000 (52 %)</td>
    <td>422 / 1000 (42 %)</td>
    <td>252 / 612 (41 %)</td>
    <td>503 / 1000 (50 %)</td>
    <td>479 / 1000 (48 %)</td>
    <td>475 / 1000 (48 %)</td>
    <td>533 / 1000 (53 %)</td>
    <td>488 / 1000 (49 %)</td>
    <td>439 / 1000 (44 %)</td>
    <td>761 / 1000 (76 %)</td>
    <td>514 / 1000 (51 %)</td>
    <td>5019 / 10612 (47 %)</td>
</tr>
<tr>
    <th>Webis news bias 20</th>
    <td>485 / 1000 (48 %)</td>
    <td>498 / 1000 (50 %)</td>
    <td>490 / 1000 (49 %)</td>
    <td>184 / 612 (30 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>421 / 1000 (42 %)</td>
    <td>487 / 1000 (49 %)</td>
    <td>528 / 1000 (53 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>468 / 1000 (47 %)</td>
    <td>447 / 1000 (45 %)</td>
    <td>720 / 1000 (72 %)</td>
    <td>5020 / 10612 (47 %)</td>
</tr>
</table>

## RoBERTa base

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
    <td>349 / 1000 (35 %)</td>
    <td>312 / 1000 (31 %)</td>
    <td>516 / 1000 (52 %)</td>
    <td>250 / 612 (41 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>393 / 1000 (39 %)</td>
    <td>513 / 1000 (51 %)</td>
    <td>420 / 1000 (42 %)</td>
    <td>470 / 1000 (47 %)</td>
    <td>328 / 1000 (33 %)</td>
    <td>429 / 1000 (43 %)</td>
    <td>392 / 1000 (39 %)</td>
    <td>4517 / 10612 (43 %)</td>
</tr>
<tr>
    <th>CommonCrawl news articles</th>
    <td>441 / 1000 (44 %)</td>
    <td>729 / 1000 (73 %)</td>
    <td>190 / 1000 (19 %)</td>
    <td>185 / 612 (30 %)</td>
    <td>320 / 1000 (32 %)</td>
    <td>489 / 1000 (49 %)</td>
    <td>314 / 1000 (31 %)</td>
    <td>343 / 1000 (34 %)</td>
    <td>416 / 1000 (42 %)</td>
    <td>297 / 1000 (30 %)</td>
    <td>456 / 1000 (46 %)</td>
    <td>557 / 1000 (56 %)</td>
    <td>4008 / 10612 (38 %)</td>
</tr>
<tr>
    <th>Dem., rep. party platform topics</th>
    <td>485 / 1000 (48 %)</td>
    <td>633 / 1000 (63 %)</td>
    <td>503 / 1000 (50 %)</td>
    <td>184 / 434 (42 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>611 / 1000 (61 %)</td>
    <td>487 / 1000 (49 %)</td>
    <td>580 / 1000 (58 %)</td>
    <td>530 / 1000 (53 %)</td>
    <td>565 / 1000 (56 %)</td>
    <td>441 / 1000 (44 %)</td>
    <td>536 / 1000 (54 %)</td>
    <td>5558 / 10434 (53 %)</td>
</tr>
<tr>
    <th>GPT-4 political bias</th>
    <td>351 / 1000 (35 %)</td>
    <td>390 / 1000 (39 %)</td>
    <td>560 / 1000 (56 %)</td>
    <td>589 / 612 (96 %)</td>
    <td>728 / 1000 (73 %)</td>
    <td>481 / 1000 (48 %)</td>
    <td>505 / 1000 (50 %)</td>
    <td>615 / 1000 (62 %)</td>
    <td>628 / 1000 (63 %)</td>
    <td>385 / 1000 (38 %)</td>
    <td>419 / 1000 (42 %)</td>
    <td>412 / 1000 (41 %)</td>
    <td>5474 / 11000 (50 %)</td>
</tr>
<tr>
    <th>GPT-4 political ideologies</th>
    <td>532 / 1000 (53 %)</td>
    <td>450 / 1000 (45 %)</td>
    <td>592 / 1000 (59 %)</td>
    <td>348 / 434 (80 %)</td>
    <td>967 / 1000 (97 %)</td>
    <td>519 / 1000 (52 %)</td>
    <td>555 / 1000 (56 %)</td>
    <td>680 / 1000 (68 %)</td>
    <td>602 / 1000 (60 %)</td>
    <td>473 / 1000 (47 %)</td>
    <td>510 / 1000 (51 %)</td>
    <td>551 / 1000 (55 %)</td>
    <td>5812 / 10434 (56 %)</td>
</tr>
<tr>
    <th>Media political stance</th>
    <td>528 / 1000 (53 %)</td>
    <td>627 / 1000 (63 %)</td>
    <td>484 / 1000 (48 %)</td>
    <td>184 / 434 (42 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>595 / 1000 (60 %)</td>
    <td>502 / 1000 (50 %)</td>
    <td>580 / 1000 (58 %)</td>
    <td>530 / 1000 (53 %)</td>
    <td>565 / 1000 (56 %)</td>
    <td>488 / 1000 (49 %)</td>
    <td>488 / 1000 (49 %)</td>
    <td>5482 / 10434 (53 %)</td>
</tr>
<tr>
    <th>Parliament speeches 2024</th>
    <td>488 / 1000 (49 %)</td>
    <td>554 / 1000 (55 %)</td>
    <td>498 / 1000 (50 %)</td>
    <td>248 / 434 (57 %)</td>
    <td>495 / 1000 (50 %)</td>
    <td>580 / 1000 (58 %)</td>
    <td>737 / 1000 (74 %)</td>
    <td>454 / 1000 (45 %)</td>
    <td>413 / 1000 (41 %)</td>
    <td>547 / 1000 (55 %)</td>
    <td>438 / 1000 (44 %)</td>
    <td>536 / 1000 (54 %)</td>
    <td>5251 / 10434 (50 %)</td>
</tr>
<tr>
    <th>PoliStance issue tweets</th>
    <td>505 / 1000 (50 %)</td>
    <td>406 / 1000 (41 %)</td>
    <td>550 / 1000 (55 %)</td>
    <td>294 / 434 (68 %)</td>
    <td>566 / 1000 (57 %)</td>
    <td>493 / 1000 (49 %)</td>
    <td>508 / 1000 (51 %)</td>
    <td>946 / 1000 (95 %)</td>
    <td>535 / 1000 (54 %)</td>
    <td>495 / 1000 (50 %)</td>
    <td>500 / 1000 (50 %)</td>
    <td>492 / 1000 (49 %)</td>
    <td>5344 / 10434 (51 %)</td>
</tr>
<tr>
    <th>Political tweets</th>
    <td>516 / 1000 (52 %)</td>
    <td>424 / 1000 (42 %)</td>
    <td>610 / 1000 (61 %)</td>
    <td>301 / 434 (69 %)</td>
    <td>649 / 1000 (65 %)</td>
    <td>446 / 1000 (45 %)</td>
    <td>495 / 1000 (50 %)</td>
    <td>617 / 1000 (62 %)</td>
    <td>709 / 1000 (71 %)</td>
    <td>451 / 1000 (45 %)</td>
    <td>555 / 1000 (56 %)</td>
    <td>475 / 1000 (48 %)</td>
    <td>5539 / 10434 (53 %)</td>
</tr>
<tr>
    <th>Qbias</th>
    <td>422 / 1000 (42 %)</td>
    <td>460 / 1000 (46 %)</td>
    <td>482 / 1000 (48 %)</td>
    <td>184 / 612 (30 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>440 / 1000 (44 %)</td>
    <td>473 / 1000 (47 %)</td>
    <td>510 / 1000 (51 %)</td>
    <td>505 / 1000 (50 %)</td>
    <td>439 / 1000 (44 %)</td>
    <td>475 / 1000 (48 %)</td>
    <td>465 / 1000 (46 %)</td>
    <td>4922 / 10612 (46 %)</td>
</tr>
<tr>
    <th>Webis bias flipper 18</th>
    <td>447 / 1000 (45 %)</td>
    <td>433 / 1000 (43 %)</td>
    <td>485 / 1000 (48 %)</td>
    <td>184 / 612 (30 %)</td>
    <td>507 / 1000 (51 %)</td>
    <td>453 / 1000 (45 %)</td>
    <td>475 / 1000 (48 %)</td>
    <td>457 / 1000 (46 %)</td>
    <td>492 / 1000 (49 %)</td>
    <td>474 / 1000 (47 %)</td>
    <td>784 / 1000 (78 %)</td>
    <td>568 / 1000 (57 %)</td>
    <td>4975 / 10612 (47 %)</td>
</tr>
<tr>
    <th>Webis news bias 20</th>
    <td>437 / 1000 (44 %)</td>
    <td>384 / 1000 (38 %)</td>
    <td>482 / 1000 (48 %)</td>
    <td>250 / 612 (41 %)</td>
    <td>487 / 1000 (49 %)</td>
    <td>429 / 1000 (43 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>419 / 1000 (42 %)</td>
    <td>470 / 1000 (47 %)</td>
    <td>332 / 1000 (33 %)</td>
    <td>529 / 1000 (53 %)</td>
    <td>770 / 1000 (77 %)</td>
    <td>4713 / 10612 (44 %)</td>
</tr>
</table>

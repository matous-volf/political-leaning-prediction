# Leave-one-out dataset benchmark

If two datasets intersect with each other (as measured [here](/analysis/dataset_intersection)) by more than 10 %, the
smaller dataset is not a part of this benchmark to avoid spillover.

From each dataset, a sample of 1 000 articles (or less if the dataset is smaller) has been taken while ensuring an equal
distribution of leaning and systematically sampling by the body length. Several models have been fine-tuned separately,
each on a concatenation of all but one (the left-out dataset) of these samples. This has been repeated, leaving out a
different one dataset at a time.

The fine-tuned models can be reproduced using [this notebook](notebook.ipynb).

Then the models have been evaluated using the methodology prescribed in [this document](../../model_evaluation), while
the datasets have been sampled to 1 000 articles each. The resulting accuracies are recorded in the tables below, rows
being models and columns being datasets. The heading of the row means the left-out dataset (the only one, which the
model has not been fine-tuned on), while the heading of the column is the dataset being evaluated on.

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
    <th>Political podcasts</th>
    <th>Political tweets</th>
    <th>Qbias</th>
</tr>
<tr>
    <th>Article bias prediction</th>
    <td>467 / 1000 (47 %)</td>
    <td>674 / 1000 (67 %)</td>
    <td>715 / 1000 (72 %)</td>
    <td>589 / 612 (96 %)</td>
    <td>979 / 1000 (98 %)</td>
    <td>761 / 1000 (76 %)</td>
    <td>669 / 1000 (67 %)</td>
    <td>976 / 1000 (98 %)</td>
    <td>667 / 1000 (67 %)</td>
    <td>446 / 1000 (45 %)</td>
</tr>
<tr>
    <th>CommonCrawl news articles</th>
    <td>606 / 1000 (61 %)</td>
    <td>555 / 1000 (56 %)</td>
    <td>758 / 1000 (76 %)</td>
    <td>597 / 612 (98 %)</td>
    <td>979 / 1000 (98 %)</td>
    <td>777 / 1000 (78 %)</td>
    <td>692 / 1000 (69 %)</td>
    <td>979 / 1000 (98 %)</td>
    <td>659 / 1000 (66 %)</td>
    <td>409 / 1000 (41 %)</td>
</tr>
<tr>
    <th>Dem., rep. party platform topics</th>
    <td>624 / 1000 (62 %)</td>
    <td>700 / 1000 (70 %)</td>
    <td>604 / 1000 (60 %)</td>
    <td>590 / 612 (96 %)</td>
    <td>986 / 1000 (99 %)</td>
    <td>770 / 1000 (77 %)</td>
    <td>695 / 1000 (70 %)</td>
    <td>971 / 1000 (97 %)</td>
    <td>660 / 1000 (66 %)</td>
    <td>457 / 1000 (46 %)</td>
</tr>
<tr>
    <th>GPT-4 political bias</th>
    <td>619 / 1000 (62 %)</td>
    <td>680 / 1000 (68 %)</td>
    <td>736 / 1000 (74 %)</td>
    <td>340 / 612 (56 %)</td>
    <td>969 / 1000 (97 %)</td>
    <td>768 / 1000 (77 %)</td>
    <td>693 / 1000 (69 %)</td>
    <td>974 / 1000 (97 %)</td>
    <td>675 / 1000 (68 %)</td>
    <td>463 / 1000 (46 %)</td>
</tr>
<tr>
    <th>GPT-4 political ideologies</th>
    <td>613 / 1000 (61 %)</td>
    <td>684 / 1000 (68 %)</td>
    <td>728 / 1000 (73 %)</td>
    <td>590 / 612 (96 %)</td>
    <td>750 / 1000 (75 %)</td>
    <td>794 / 1000 (79 %)</td>
    <td>697 / 1000 (70 %)</td>
    <td>978 / 1000 (98 %)</td>
    <td>678 / 1000 (68 %)</td>
    <td>442 / 1000 (44 %)</td>
</tr>
<tr>
    <th>Media political stance</th>
    <td>563 / 1000 (56 %)</td>
    <td>641 / 1000 (64 %)</td>
    <td>752 / 1000 (75 %)</td>
    <td>585 / 612 (96 %)</td>
    <td>970 / 1000 (97 %)</td>
    <td>470 / 1000 (47 %)</td>
    <td>679 / 1000 (68 %)</td>
    <td>970 / 1000 (97 %)</td>
    <td>666 / 1000 (67 %)</td>
    <td>431 / 1000 (43 %)</td>
</tr>
<tr>
    <th>Parliament speeches 2024</th>
    <td>607 / 1000 (61 %)</td>
    <td>665 / 1000 (66 %)</td>
    <td>751 / 1000 (75 %)</td>
    <td>591 / 612 (97 %)</td>
    <td>984 / 1000 (98 %)</td>
    <td>774 / 1000 (77 %)</td>
    <td>475 / 1000 (48 %)</td>
    <td>976 / 1000 (98 %)</td>
    <td>693 / 1000 (69 %)</td>
    <td>466 / 1000 (47 %)</td>
</tr>
<tr>
    <th>Political podcasts</th>
    <td>622 / 1000 (62 %)</td>
    <td>687 / 1000 (69 %)</td>
    <td>741 / 1000 (74 %)</td>
    <td>593 / 612 (97 %)</td>
    <td>984 / 1000 (98 %)</td>
    <td>746 / 1000 (75 %)</td>
    <td>691 / 1000 (69 %)</td>
    <td>614 / 1000 (61 %)</td>
    <td>660 / 1000 (66 %)</td>
    <td>455 / 1000 (46 %)</td>
</tr>
<tr>
    <th>Political tweets</th>
    <td>635 / 1000 (64 %)</td>
    <td>708 / 1000 (71 %)</td>
    <td>771 / 1000 (77 %)</td>
    <td>594 / 612 (97 %)</td>
    <td>978 / 1000 (98 %)</td>
    <td>774 / 1000 (77 %)</td>
    <td>685 / 1000 (68 %)</td>
    <td>979 / 1000 (98 %)</td>
    <td>501 / 1000 (50 %)</td>
    <td>457 / 1000 (46 %)</td>
</tr>
<tr>
    <th>Qbias</th>
    <td>632 / 1000 (63 %)</td>
    <td>688 / 1000 (69 %)</td>
    <td>734 / 1000 (73 %)</td>
    <td>592 / 612 (97 %)</td>
    <td>977 / 1000 (98 %)</td>
    <td>779 / 1000 (78 %)</td>
    <td>670 / 1000 (67 %)</td>
    <td>971 / 1000 (97 %)</td>
    <td>671 / 1000 (67 %)</td>
    <td>416 / 1000 (42 %)</td>
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
    <th>Political podcasts</th>
    <th>Political tweets</th>
    <th>Qbias</th>
</tr>
<tr>
    <th>Article bias prediction</th>
    <td>378 / 1000 (38 %)</td>
    <td>545 / 1000 (55 %)</td>
    <td>513 / 1000 (51 %)</td>
    <td>370 / 612 (60 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>520 / 1000 (52 %)</td>
    <td>522 / 1000 (52 %)</td>
    <td>704 / 1000 (70 %)</td>
    <td>467 / 1000 (47 %)</td>
    <td>423 / 1000 (42 %)</td>
</tr>
<tr>
    <th>CommonCrawl news articles</th>
    <td>610 / 1000 (61 %)</td>
    <td>619 / 1000 (62 %)</td>
    <td>743 / 1000 (74 %)</td>
    <td>582 / 612 (95 %)</td>
    <td>979 / 1000 (98 %)</td>
    <td>833 / 1000 (83 %)</td>
    <td>678 / 1000 (68 %)</td>
    <td>977 / 1000 (98 %)</td>
    <td>690 / 1000 (69 %)</td>
    <td>399 / 1000 (40 %)</td>
</tr>
<tr>
    <th>Dem., rep. party platform topics</th>
    <td>634 / 1000 (63 %)</td>
    <td>717 / 1000 (72 %)</td>
    <td>620 / 1000 (62 %)</td>
    <td>570 / 612 (93 %)</td>
    <td>968 / 1000 (97 %)</td>
    <td>847 / 1000 (85 %)</td>
    <td>697 / 1000 (70 %)</td>
    <td>964 / 1000 (96 %)</td>
    <td>695 / 1000 (70 %)</td>
    <td>449 / 1000 (45 %)</td>
</tr>
<tr>
    <th>GPT-4 political bias</th>
    <td>681 / 1000 (68 %)</td>
    <td>731 / 1000 (73 %)</td>
    <td>753 / 1000 (75 %)</td>
    <td>352 / 612 (58 %)</td>
    <td>976 / 1000 (98 %)</td>
    <td>836 / 1000 (84 %)</td>
    <td>684 / 1000 (68 %)</td>
    <td>981 / 1000 (98 %)</td>
    <td>695 / 1000 (70 %)</td>
    <td>466 / 1000 (47 %)</td>
</tr>
<tr>
    <th>GPT-4 political ideologies</th>
    <td>358 / 1000 (36 %)</td>
    <td>437 / 1000 (44 %)</td>
    <td>487 / 1000 (49 %)</td>
    <td>357 / 612 (58 %)</td>
    <td>492 / 1000 (49 %)</td>
    <td>552 / 1000 (55 %)</td>
    <td>562 / 1000 (56 %)</td>
    <td>671 / 1000 (67 %)</td>
    <td>459 / 1000 (46 %)</td>
    <td>394 / 1000 (39 %)</td>
</tr>
<tr>
    <th>Media political stance</th>
    <td>349 / 1000 (35 %)</td>
    <td>313 / 1000 (31 %)</td>
    <td>516 / 1000 (52 %)</td>
    <td>250 / 612 (41 %)</td>
    <td>489 / 1000 (49 %)</td>
    <td>432 / 1000 (43 %)</td>
    <td>515 / 1000 (52 %)</td>
    <td>525 / 1000 (52 %)</td>
    <td>470 / 1000 (47 %)</td>
    <td>340 / 1000 (34 %)</td>
</tr>
<tr>
    <th>Parliament speeches 2024</th>
    <td>349 / 1000 (35 %)</td>
    <td>329 / 1000 (33 %)</td>
    <td>515 / 1000 (52 %)</td>
    <td>396 / 612 (65 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>393 / 1000 (39 %)</td>
    <td>513 / 1000 (51 %)</td>
    <td>511 / 1000 (51 %)</td>
    <td>470 / 1000 (47 %)</td>
    <td>328 / 1000 (33 %)</td>
</tr>
<tr>
    <th>Political podcasts</th>
    <td>595 / 1000 (60 %)</td>
    <td>670 / 1000 (67 %)</td>
    <td>701 / 1000 (70 %)</td>
    <td>551 / 612 (90 %)</td>
    <td>976 / 1000 (98 %)</td>
    <td>772 / 1000 (77 %)</td>
    <td>677 / 1000 (68 %)</td>
    <td>618 / 1000 (62 %)</td>
    <td>686 / 1000 (69 %)</td>
    <td>432 / 1000 (43 %)</td>
</tr>
<tr>
    <th>Political tweets</th>
    <td>349 / 1000 (35 %)</td>
    <td>312 / 1000 (31 %)</td>
    <td>516 / 1000 (52 %)</td>
    <td>250 / 612 (41 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>393 / 1000 (39 %)</td>
    <td>513 / 1000 (51 %)</td>
    <td>511 / 1000 (51 %)</td>
    <td>470 / 1000 (47 %)</td>
    <td>328 / 1000 (33 %)</td>
</tr>
<tr>
    <th>Qbias</th>
    <td>663 / 1000 (66 %)</td>
    <td>741 / 1000 (74 %)</td>
    <td>735 / 1000 (74 %)</td>
    <td>583 / 612 (95 %)</td>
    <td>972 / 1000 (97 %)</td>
    <td>850 / 1000 (85 %)</td>
    <td>702 / 1000 (70 %)</td>
    <td>981 / 1000 (98 %)</td>
    <td>678 / 1000 (68 %)</td>
    <td>444 / 1000 (44 %)</td>
</tr>
</table>

## POLITICS

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
</tr>
<tr>
    <th>Article bias prediction</th>
    <td>486 / 1000 (49 %)</td>
    <td>789 / 1000 (79 %)</td>
    <td>763 / 1000 (76 %)</td>
    <td>592 / 612 (97 %)</td>
    <td>975 / 1000 (98 %)</td>
    <td>886 / 1000 (89 %)</td>
    <td>723 / 1000 (72 %)</td>
    <td>986 / 1000 (99 %)</td>
    <td>716 / 1000 (72 %)</td>
    <td>561 / 1000 (56 %)</td>
</tr>
<tr>
    <th>CommonCrawl news articles</th>
    <td>765 / 1000 (76 %)</td>
    <td>639 / 1000 (64 %)</td>
    <td>776 / 1000 (78 %)</td>
    <td>594 / 612 (97 %)</td>
    <td>981 / 1000 (98 %)</td>
    <td>886 / 1000 (89 %)</td>
    <td>735 / 1000 (74 %)</td>
    <td>988 / 1000 (99 %)</td>
    <td>706 / 1000 (71 %)</td>
    <td>548 / 1000 (55 %)</td>
</tr>
<tr>
    <th>Dem., rep. party platform topics</th>
    <td>767 / 1000 (77 %)</td>
    <td>785 / 1000 (78 %)</td>
    <td>623 / 1000 (62 %)</td>
    <td>591 / 612 (97 %)</td>
    <td>983 / 1000 (98 %)</td>
    <td>901 / 1000 (90 %)</td>
    <td>739 / 1000 (74 %)</td>
    <td>992 / 1000 (99 %)</td>
    <td>737 / 1000 (74 %)</td>
    <td>573 / 1000 (57 %)</td>
</tr>
<tr>
    <th>GPT-4 political bias</th>
    <td>752 / 1000 (75 %)</td>
    <td>800 / 1000 (80 %)</td>
    <td>775 / 1000 (78 %)</td>
    <td>363 / 612 (59 %)</td>
    <td>985 / 1000 (98 %)</td>
    <td>870 / 1000 (87 %)</td>
    <td>737 / 1000 (74 %)</td>
    <td>990 / 1000 (99 %)</td>
    <td>735 / 1000 (74 %)</td>
    <td>568 / 1000 (57 %)</td>
</tr>
<tr>
    <th>GPT-4 political ideologies</th>
    <td>774 / 1000 (77 %)</td>
    <td>786 / 1000 (79 %)</td>
    <td>760 / 1000 (76 %)</td>
    <td>592 / 612 (97 %)</td>
    <td>819 / 1000 (82 %)</td>
    <td>878 / 1000 (88 %)</td>
    <td>727 / 1000 (73 %)</td>
    <td>987 / 1000 (99 %)</td>
    <td>731 / 1000 (73 %)</td>
    <td>544 / 1000 (54 %)</td>
</tr>
<tr>
    <th>Media political stance</th>
    <td>742 / 1000 (74 %)</td>
    <td>802 / 1000 (80 %)</td>
    <td>750 / 1000 (75 %)</td>
    <td>593 / 612 (97 %)</td>
    <td>973 / 1000 (97 %)</td>
    <td>578 / 1000 (58 %)</td>
    <td>723 / 1000 (72 %)</td>
    <td>987 / 1000 (99 %)</td>
    <td>741 / 1000 (74 %)</td>
    <td>542 / 1000 (54 %)</td>
</tr>
<tr>
    <th>Parliament speeches 2024</th>
    <td>771 / 1000 (77 %)</td>
    <td>804 / 1000 (80 %)</td>
    <td>760 / 1000 (76 %)</td>
    <td>591 / 612 (97 %)</td>
    <td>978 / 1000 (98 %)</td>
    <td>882 / 1000 (88 %)</td>
    <td>462 / 1000 (46 %)</td>
    <td>987 / 1000 (99 %)</td>
    <td>740 / 1000 (74 %)</td>
    <td>560 / 1000 (56 %)</td>
</tr>
<tr>
    <th>Political podcasts</th>
    <td>755 / 1000 (76 %)</td>
    <td>770 / 1000 (77 %)</td>
    <td>765 / 1000 (76 %)</td>
    <td>590 / 612 (96 %)</td>
    <td>979 / 1000 (98 %)</td>
    <td>887 / 1000 (89 %)</td>
    <td>722 / 1000 (72 %)</td>
    <td>672 / 1000 (67 %)</td>
    <td>728 / 1000 (73 %)</td>
    <td>569 / 1000 (57 %)</td>
</tr>
<tr>
    <th>Political tweets</th>
    <td>756 / 1000 (76 %)</td>
    <td>794 / 1000 (79 %)</td>
    <td>769 / 1000 (77 %)</td>
    <td>594 / 612 (97 %)</td>
    <td>972 / 1000 (97 %)</td>
    <td>870 / 1000 (87 %)</td>
    <td>751 / 1000 (75 %)</td>
    <td>990 / 1000 (99 %)</td>
    <td>580 / 1000 (58 %)</td>
    <td>585 / 1000 (58 %)</td>
</tr>
<tr>
    <th>Qbias</th>
    <td>772 / 1000 (77 %)</td>
    <td>808 / 1000 (81 %)</td>
    <td>771 / 1000 (77 %)</td>
    <td>586 / 612 (96 %)</td>
    <td>974 / 1000 (97 %)</td>
    <td>878 / 1000 (88 %)</td>
    <td>726 / 1000 (73 %)</td>
    <td>991 / 1000 (99 %)</td>
    <td>734 / 1000 (73 %)</td>
    <td>515 / 1000 (52 %)</td>
</tr>
</table>

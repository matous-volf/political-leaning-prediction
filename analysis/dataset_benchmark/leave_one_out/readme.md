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
    <th>Political tweets</th>
    <th>Qbias</th>
</tr>
<tr>
    <th>Article bias prediction</th>
    <td>487 / 1000 (49 %)</td>
    <td>682 / 1000 (68 %)</td>
    <td>734 / 1000 (73 %)</td>
    <td>585 / 612 (96 %)</td>
    <td>974 / 1000 (97 %)</td>
    <td>781 / 1000 (78 %)</td>
    <td>678 / 1000 (68 %)</td>
    <td>693 / 1000 (69 %)</td>
    <td>456 / 1000 (46 %)</td>
</tr>
<tr>
    <th>CommonCrawl news articles</th>
    <td>596 / 1000 (60 %)</td>
    <td>531 / 1000 (53 %)</td>
    <td>755 / 1000 (76 %)</td>
    <td>588 / 612 (96 %)</td>
    <td>974 / 1000 (97 %)</td>
    <td>781 / 1000 (78 %)</td>
    <td>660 / 1000 (66 %)</td>
    <td>687 / 1000 (69 %)</td>
    <td>472 / 1000 (47 %)</td>
</tr>
<tr>
    <th>Dem., rep. party platform topics</th>
    <td>599 / 1000 (60 %)</td>
    <td>703 / 1000 (70 %)</td>
    <td>610 / 1000 (61 %)</td>
    <td>594 / 612 (97 %)</td>
    <td>979 / 1000 (98 %)</td>
    <td>765 / 1000 (76 %)</td>
    <td>684 / 1000 (68 %)</td>
    <td>709 / 1000 (71 %)</td>
    <td>482 / 1000 (48 %)</td>
</tr>
<tr>
    <th>GPT-4 political bias</th>
    <td>616 / 1000 (62 %)</td>
    <td>687 / 1000 (69 %)</td>
    <td>740 / 1000 (74 %)</td>
    <td>325 / 612 (53 %)</td>
    <td>971 / 1000 (97 %)</td>
    <td>758 / 1000 (76 %)</td>
    <td>705 / 1000 (70 %)</td>
    <td>697 / 1000 (70 %)</td>
    <td>459 / 1000 (46 %)</td>
</tr>
<tr>
    <th>GPT-4 political ideologies</th>
    <td>616 / 1000 (62 %)</td>
    <td>675 / 1000 (68 %)</td>
    <td>733 / 1000 (73 %)</td>
    <td>586 / 612 (96 %)</td>
    <td>748 / 1000 (75 %)</td>
    <td>783 / 1000 (78 %)</td>
    <td>687 / 1000 (69 %)</td>
    <td>662 / 1000 (66 %)</td>
    <td>470 / 1000 (47 %)</td>
</tr>
<tr>
    <th>Media political stance</th>
    <td>606 / 1000 (61 %)</td>
    <td>685 / 1000 (68 %)</td>
    <td>754 / 1000 (75 %)</td>
    <td>588 / 612 (96 %)</td>
    <td>979 / 1000 (98 %)</td>
    <td>466 / 1000 (47 %)</td>
    <td>677 / 1000 (68 %)</td>
    <td>709 / 1000 (71 %)</td>
    <td>475 / 1000 (48 %)</td>
</tr>
<tr>
    <th>Parliament speeches 2024</th>
    <td>634 / 1000 (63 %)</td>
    <td>695 / 1000 (70 %)</td>
    <td>747 / 1000 (75 %)</td>
    <td>589 / 612 (96 %)</td>
    <td>980 / 1000 (98 %)</td>
    <td>808 / 1000 (81 %)</td>
    <td>445 / 1000 (44 %)</td>
    <td>708 / 1000 (71 %)</td>
    <td>469 / 1000 (47 %)</td>
</tr>
<tr>
    <th>Political tweets</th>
    <td>605 / 1000 (60 %)</td>
    <td>683 / 1000 (68 %)</td>
    <td>732 / 1000 (73 %)</td>
    <td>596 / 612 (97 %)</td>
    <td>975 / 1000 (98 %)</td>
    <td>773 / 1000 (77 %)</td>
    <td>675 / 1000 (68 %)</td>
    <td>565 / 1000 (56 %)</td>
    <td>466 / 1000 (47 %)</td>
</tr>
<tr>
    <th>Qbias</th>
    <td>641 / 1000 (64 %)</td>
    <td>698 / 1000 (70 %)</td>
    <td>738 / 1000 (74 %)</td>
    <td>579 / 612 (95 %)</td>
    <td>976 / 1000 (98 %)</td>
    <td>792 / 1000 (79 %)</td>
    <td>667 / 1000 (67 %)</td>
    <td>696 / 1000 (70 %)</td>
    <td>478 / 1000 (48 %)</td>
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
    <th>Political tweets</th>
    <th>Qbias</th>
</tr>
<tr>
    <th>Article bias prediction</th>
    <td>400 / 1000 (40 %)</td>
    <td>500 / 1000 (50 %)</td>
    <td>592 / 1000 (59 %)</td>
    <td>441 / 612 (72 %)</td>
    <td>893 / 1000 (89 %)</td>
    <td>614 / 1000 (61 %)</td>
    <td>585 / 1000 (58 %)</td>
    <td>580 / 1000 (58 %)</td>
    <td>345 / 1000 (34 %)</td>
</tr>
<tr>
    <th>CommonCrawl news articles</th>
    <td>627 / 1000 (63 %)</td>
    <td>636 / 1000 (64 %)</td>
    <td>727 / 1000 (73 %)</td>
    <td>571 / 612 (93 %)</td>
    <td>971 / 1000 (97 %)</td>
    <td>852 / 1000 (85 %)</td>
    <td>678 / 1000 (68 %)</td>
    <td>715 / 1000 (72 %)</td>
    <td>462 / 1000 (46 %)</td>
</tr>
<tr>
    <th>Dem., rep. party platform topics</th>
    <td>656 / 1000 (66 %)</td>
    <td>731 / 1000 (73 %)</td>
    <td>594 / 1000 (59 %)</td>
    <td>579 / 612 (95 %)</td>
    <td>967 / 1000 (97 %)</td>
    <td>839 / 1000 (84 %)</td>
    <td>701 / 1000 (70 %)</td>
    <td>696 / 1000 (70 %)</td>
    <td>482 / 1000 (48 %)</td>
</tr>
<tr>
    <th>GPT-4 political bias</th>
    <td>346 / 1000 (35 %)</td>
    <td>459 / 1000 (46 %)</td>
    <td>485 / 1000 (48 %)</td>
    <td>184 / 612 (30 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>570 / 1000 (57 %)</td>
    <td>486 / 1000 (49 %)</td>
    <td>537 / 1000 (54 %)</td>
    <td>365 / 1000 (36 %)</td>
</tr>
<tr>
    <th>GPT-4 political ideologies</th>
    <td>649 / 1000 (65 %)</td>
    <td>718 / 1000 (72 %)</td>
    <td>704 / 1000 (70 %)</td>
    <td>579 / 612 (95 %)</td>
    <td>809 / 1000 (81 %)</td>
    <td>812 / 1000 (81 %)</td>
    <td>653 / 1000 (65 %)</td>
    <td>678 / 1000 (68 %)</td>
    <td>459 / 1000 (46 %)</td>
</tr>
<tr>
    <th>Media political stance</th>
    <td>354 / 1000 (35 %)</td>
    <td>525 / 1000 (52 %)</td>
    <td>484 / 1000 (48 %)</td>
    <td>184 / 612 (30 %)</td>
    <td>506 / 1000 (51 %)</td>
    <td>607 / 1000 (61 %)</td>
    <td>487 / 1000 (49 %)</td>
    <td>530 / 1000 (53 %)</td>
    <td>474 / 1000 (47 %)</td>
</tr>
<tr>
    <th>Parliament speeches 2024</th>
    <td>694 / 1000 (69 %)</td>
    <td>723 / 1000 (72 %)</td>
    <td>730 / 1000 (73 %)</td>
    <td>582 / 612 (95 %)</td>
    <td>979 / 1000 (98 %)</td>
    <td>847 / 1000 (85 %)</td>
    <td>463 / 1000 (46 %)</td>
    <td>712 / 1000 (71 %)</td>
    <td>488 / 1000 (49 %)</td>
</tr>
<tr>
    <th>Political tweets</th>
    <td>414 / 1000 (41 %)</td>
    <td>496 / 1000 (50 %)</td>
    <td>525 / 1000 (52 %)</td>
    <td>329 / 612 (54 %)</td>
    <td>494 / 1000 (49 %)</td>
    <td>424 / 1000 (42 %)</td>
    <td>516 / 1000 (52 %)</td>
    <td>420 / 1000 (42 %)</td>
    <td>348 / 1000 (35 %)</td>
</tr>
<tr>
    <th>Qbias</th>
    <td>684 / 1000 (68 %)</td>
    <td>737 / 1000 (74 %)</td>
    <td>748 / 1000 (75 %)</td>
    <td>584 / 612 (95 %)</td>
    <td>972 / 1000 (97 %)</td>
    <td>841 / 1000 (84 %)</td>
    <td>702 / 1000 (70 %)</td>
    <td>719 / 1000 (72 %)</td>
    <td>450 / 1000 (45 %)</td>
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
    <th>Political tweets</th>
    <th>Qbias</th>
</tr>
<tr>
    <th>Article bias prediction</th>
    <td>553 / 1000 (55 %)</td>
    <td>802 / 1000 (80 %)</td>
    <td>756 / 1000 (76 %)</td>
    <td>595 / 612 (97 %)</td>
    <td>981 / 1000 (98 %)</td>
    <td>878 / 1000 (88 %)</td>
    <td>736 / 1000 (74 %)</td>
    <td>749 / 1000 (75 %)</td>
    <td>554 / 1000 (55 %)</td>
</tr>
<tr>
    <th>CommonCrawl news articles</th>
    <td>775 / 1000 (78 %)</td>
    <td>601 / 1000 (60 %)</td>
    <td>766 / 1000 (77 %)</td>
    <td>593 / 612 (97 %)</td>
    <td>981 / 1000 (98 %)</td>
    <td>895 / 1000 (90 %)</td>
    <td>737 / 1000 (74 %)</td>
    <td>747 / 1000 (75 %)</td>
    <td>561 / 1000 (56 %)</td>
</tr>
<tr>
    <th>Dem., rep. party platform topics</th>
    <td>766 / 1000 (77 %)</td>
    <td>780 / 1000 (78 %)</td>
    <td>624 / 1000 (62 %)</td>
    <td>592 / 612 (97 %)</td>
    <td>983 / 1000 (98 %)</td>
    <td>881 / 1000 (88 %)</td>
    <td>729 / 1000 (73 %)</td>
    <td>751 / 1000 (75 %)</td>
    <td>556 / 1000 (56 %)</td>
</tr>
<tr>
    <th>GPT-4 political bias</th>
    <td>768 / 1000 (77 %)</td>
    <td>785 / 1000 (78 %)</td>
    <td>756 / 1000 (76 %)</td>
    <td>335 / 612 (55 %)</td>
    <td>972 / 1000 (97 %)</td>
    <td>875 / 1000 (88 %)</td>
    <td>742 / 1000 (74 %)</td>
    <td>747 / 1000 (75 %)</td>
    <td>572 / 1000 (57 %)</td>
</tr>
<tr>
    <th>GPT-4 political ideologies</th>
    <td>757 / 1000 (76 %)</td>
    <td>780 / 1000 (78 %)</td>
    <td>767 / 1000 (77 %)</td>
    <td>592 / 612 (97 %)</td>
    <td>852 / 1000 (85 %)</td>
    <td>885 / 1000 (88 %)</td>
    <td>729 / 1000 (73 %)</td>
    <td>757 / 1000 (76 %)</td>
    <td>560 / 1000 (56 %)</td>
</tr>
<tr>
    <th>Media political stance</th>
    <td>764 / 1000 (76 %)</td>
    <td>764 / 1000 (76 %)</td>
    <td>768 / 1000 (77 %)</td>
    <td>597 / 612 (98 %)</td>
    <td>977 / 1000 (98 %)</td>
    <td>616 / 1000 (62 %)</td>
    <td>733 / 1000 (73 %)</td>
    <td>752 / 1000 (75 %)</td>
    <td>547 / 1000 (55 %)</td>
</tr>
<tr>
    <th>Parliament speeches 2024</th>
    <td>768 / 1000 (77 %)</td>
    <td>806 / 1000 (81 %)</td>
    <td>783 / 1000 (78 %)</td>
    <td>593 / 612 (97 %)</td>
    <td>981 / 1000 (98 %)</td>
    <td>885 / 1000 (88 %)</td>
    <td>463 / 1000 (46 %)</td>
    <td>752 / 1000 (75 %)</td>
    <td>567 / 1000 (57 %)</td>
</tr>
<tr>
    <th>Political tweets</th>
    <td>770 / 1000 (77 %)</td>
    <td>796 / 1000 (80 %)</td>
    <td>765 / 1000 (76 %)</td>
    <td>590 / 612 (96 %)</td>
    <td>973 / 1000 (97 %)</td>
    <td>884 / 1000 (88 %)</td>
    <td>744 / 1000 (74 %)</td>
    <td>626 / 1000 (63 %)</td>
    <td>555 / 1000 (56 %)</td>
</tr>
<tr>
    <th>Qbias</th>
    <td>781 / 1000 (78 %)</td>
    <td>798 / 1000 (80 %)</td>
    <td>774 / 1000 (77 %)</td>
    <td>593 / 612 (97 %)</td>
    <td>975 / 1000 (98 %)</td>
    <td>891 / 1000 (89 %)</td>
    <td>738 / 1000 (74 %)</td>
    <td>767 / 1000 (77 %)</td>
    <td>508 / 1000 (51 %)</td>
</tr>
</table>

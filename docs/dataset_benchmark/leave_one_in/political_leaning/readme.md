# Political leaning leave-one-in dataset benchmark

The resulting accuracies are stored in files

- [with center leaning class](results_with_center_leaning_class.csv),
- [without center leaning class](results_without_center_leaning_class.csv)

and are recorded in the two tables below.

## with the center leaning class

### POLITICS

<table>
<tr>
    <th></th>
    <th>article_bias_prediction</th>
    <th>commoncrawl_news_articles</th>
    <th>dem_rep_party_platform_topics</th>
    <th>gpt4_political_bias</th>
    <th>gpt4_political_ideologies</th>
    <th>media_political_stance</th>
    <th>parliament_speeches_2024</th>
    <th>political_podcasts</th>
    <th>political_tweets</th>
    <th>qbias</th>
    <th>webis_bias_flipper_18</th>
    <th>webis_news_bias_20</th>
    <th>average</th>
</tr>
<tr>
    <th style="white-space: nowrap;">article_bias_prediction</th>
    <td style="white-space: nowrap; text-align: right;">816 / 1000 (82 %)</td>
    <td style="white-space: nowrap; text-align: right;">520 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">307 / 1000 (31 %)</td>
    <td style="white-space: nowrap; text-align: right;">166 / 612 (27 %)</td>
    <td style="white-space: nowrap; text-align: right;">290 / 1000 (29 %)</td>
    <td style="white-space: nowrap; text-align: right;">507 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">66 / 1000 (7 %)</td>
    <td style="white-space: nowrap; text-align: right;">572 / 1000 (57 %)</td>
    <td style="white-space: nowrap; text-align: right;">426 / 1000 (43 %)</td>
    <td style="white-space: nowrap; text-align: right;">443 / 1000 (44 %)</td>
    <td style="white-space: nowrap; text-align: right;">672 / 1000 (67 %)</td>
    <td style="white-space: nowrap; text-align: right;">782 / 1000 (78 %)</td>
    <td style="white-space: nowrap; text-align: right;">4751 / 10612 (45 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">commoncrawl_news_articles</th>
    <td style="white-space: nowrap; text-align: right;">557 / 1000 (56 %)</td>
    <td style="white-space: nowrap; text-align: right;">835 / 1000 (84 %)</td>
    <td style="white-space: nowrap; text-align: right;">358 / 1000 (36 %)</td>
    <td style="white-space: nowrap; text-align: right;">139 / 612 (23 %)</td>
    <td style="white-space: nowrap; text-align: right;">450 / 1000 (45 %)</td>
    <td style="white-space: nowrap; text-align: right;">574 / 1000 (57 %)</td>
    <td style="white-space: nowrap; text-align: right;">428 / 1000 (43 %)</td>
    <td style="white-space: nowrap; text-align: right;">701 / 1000 (70 %)</td>
    <td style="white-space: nowrap; text-align: right;">428 / 1000 (43 %)</td>
    <td style="white-space: nowrap; text-align: right;">459 / 1000 (46 %)</td>
    <td style="white-space: nowrap; text-align: right;">537 / 1000 (54 %)</td>
    <td style="white-space: nowrap; text-align: right;">658 / 1000 (66 %)</td>
    <td style="white-space: nowrap; text-align: right;">5289 / 10612 (50 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">gpt4_political_bias</th>
    <td style="white-space: nowrap; text-align: right;">334 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">236 / 1000 (24 %)</td>
    <td style="white-space: nowrap; text-align: right;">458 / 1000 (46 %)</td>
    <td style="white-space: nowrap; text-align: right;">583 / 612 (95 %)</td>
    <td style="white-space: nowrap; text-align: right;">649 / 1000 (65 %)</td>
    <td style="white-space: nowrap; text-align: right;">134 / 1000 (13 %)</td>
    <td style="white-space: nowrap; text-align: right;">54 / 1000 (5 %)</td>
    <td style="white-space: nowrap; text-align: right;">325 / 1000 (32 %)</td>
    <td style="white-space: nowrap; text-align: right;">409 / 1000 (41 %)</td>
    <td style="white-space: nowrap; text-align: right;">323 / 1000 (32 %)</td>
    <td style="white-space: nowrap; text-align: right;">280 / 1000 (28 %)</td>
    <td style="white-space: nowrap; text-align: right;">326 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">3528 / 11000 (32 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">qbias</th>
    <td style="white-space: nowrap; text-align: right;">354 / 1000 (35 %)</td>
    <td style="white-space: nowrap; text-align: right;">395 / 1000 (40 %)</td>
    <td style="white-space: nowrap; text-align: right;">538 / 1000 (54 %)</td>
    <td style="white-space: nowrap; text-align: right;">317 / 612 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">645 / 1000 (64 %)</td>
    <td style="white-space: nowrap; text-align: right;">605 / 1000 (60 %)</td>
    <td style="white-space: nowrap; text-align: right;">510 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">574 / 1000 (57 %)</td>
    <td style="white-space: nowrap; text-align: right;">505 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">364 / 1000 (36 %)</td>
    <td style="white-space: nowrap; text-align: right;">511 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">512 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">5466 / 10612 (52 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">webis_bias_flipper_18</th>
    <td style="white-space: nowrap; text-align: right;">629 / 1000 (63 %)</td>
    <td style="white-space: nowrap; text-align: right;">569 / 1000 (57 %)</td>
    <td style="white-space: nowrap; text-align: right;">519 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">185 / 612 (30 %)</td>
    <td style="white-space: nowrap; text-align: right;">602 / 1000 (60 %)</td>
    <td style="white-space: nowrap; text-align: right;">480 / 1000 (48 %)</td>
    <td style="white-space: nowrap; text-align: right;">135 / 1000 (14 %)</td>
    <td style="white-space: nowrap; text-align: right;">596 / 1000 (60 %)</td>
    <td style="white-space: nowrap; text-align: right;">519 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">416 / 1000 (42 %)</td>
    <td style="white-space: nowrap; text-align: right;">892 / 1000 (89 %)</td>
    <td style="white-space: nowrap; text-align: right;">722 / 1000 (72 %)</td>
    <td style="white-space: nowrap; text-align: right;">5372 / 10612 (51 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">webis_news_bias_20</th>
    <td style="white-space: nowrap; text-align: right;">624 / 1000 (62 %)</td>
    <td style="white-space: nowrap; text-align: right;">510 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">411 / 1000 (41 %)</td>
    <td style="white-space: nowrap; text-align: right;">98 / 612 (16 %)</td>
    <td style="white-space: nowrap; text-align: right;">320 / 1000 (32 %)</td>
    <td style="white-space: nowrap; text-align: right;">474 / 1000 (47 %)</td>
    <td style="white-space: nowrap; text-align: right;">179 / 1000 (18 %)</td>
    <td style="white-space: nowrap; text-align: right;">559 / 1000 (56 %)</td>
    <td style="white-space: nowrap; text-align: right;">458 / 1000 (46 %)</td>
    <td style="white-space: nowrap; text-align: right;">445 / 1000 (44 %)</td>
    <td style="white-space: nowrap; text-align: right;">645 / 1000 (64 %)</td>
    <td style="white-space: nowrap; text-align: right;">886 / 1000 (89 %)</td>
    <td style="white-space: nowrap; text-align: right;">4723 / 10612 (45 %)</td>
</tr>
</table>

### BERT base (cased)

<table>
<tr>
    <th></th>
    <th>article_bias_prediction</th>
    <th>commoncrawl_news_articles</th>
    <th>dem_rep_party_platform_topics</th>
    <th>gpt4_political_bias</th>
    <th>gpt4_political_ideologies</th>
    <th>media_political_stance</th>
    <th>parliament_speeches_2024</th>
    <th>political_podcasts</th>
    <th>political_tweets</th>
    <th>qbias</th>
    <th>webis_bias_flipper_18</th>
    <th>webis_news_bias_20</th>
    <th>average</th>
</tr>
<tr>
    <th style="white-space: nowrap;">article_bias_prediction</th>
    <td style="white-space: nowrap; text-align: right;">332 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">332 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">501 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">250 / 612 (41 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">501 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">332 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">332 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">332 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">4580 / 10612 (43 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">commoncrawl_news_articles</th>
    <td style="white-space: nowrap; text-align: right;">361 / 1000 (36 %)</td>
    <td style="white-space: nowrap; text-align: right;">759 / 1000 (76 %)</td>
    <td style="white-space: nowrap; text-align: right;">170 / 1000 (17 %)</td>
    <td style="white-space: nowrap; text-align: right;">184 / 612 (30 %)</td>
    <td style="white-space: nowrap; text-align: right;">288 / 1000 (29 %)</td>
    <td style="white-space: nowrap; text-align: right;">485 / 1000 (48 %)</td>
    <td style="white-space: nowrap; text-align: right;">349 / 1000 (35 %)</td>
    <td style="white-space: nowrap; text-align: right;">436 / 1000 (44 %)</td>
    <td style="white-space: nowrap; text-align: right;">427 / 1000 (43 %)</td>
    <td style="white-space: nowrap; text-align: right;">354 / 1000 (35 %)</td>
    <td style="white-space: nowrap; text-align: right;">336 / 1000 (34 %)</td>
    <td style="white-space: nowrap; text-align: right;">456 / 1000 (46 %)</td>
    <td style="white-space: nowrap; text-align: right;">3846 / 10612 (36 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">gpt4_political_bias</th>
    <td style="white-space: nowrap; text-align: right;">332 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">331 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">551 / 1000 (55 %)</td>
    <td style="white-space: nowrap; text-align: right;">579 / 612 (95 %)</td>
    <td style="white-space: nowrap; text-align: right;">742 / 1000 (74 %)</td>
    <td style="white-space: nowrap; text-align: right;">475 / 1000 (48 %)</td>
    <td style="white-space: nowrap; text-align: right;">401 / 1000 (40 %)</td>
    <td style="white-space: nowrap; text-align: right;">490 / 1000 (49 %)</td>
    <td style="white-space: nowrap; text-align: right;">570 / 1000 (57 %)</td>
    <td style="white-space: nowrap; text-align: right;">329 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">326 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">313 / 1000 (31 %)</td>
    <td style="white-space: nowrap; text-align: right;">4860 / 11000 (44 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">qbias</th>
    <td style="white-space: nowrap; text-align: right;">328 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">391 / 1000 (39 %)</td>
    <td style="white-space: nowrap; text-align: right;">411 / 1000 (41 %)</td>
    <td style="white-space: nowrap; text-align: right;">231 / 612 (38 %)</td>
    <td style="white-space: nowrap; text-align: right;">486 / 1000 (49 %)</td>
    <td style="white-space: nowrap; text-align: right;">438 / 1000 (44 %)</td>
    <td style="white-space: nowrap; text-align: right;">248 / 1000 (25 %)</td>
    <td style="white-space: nowrap; text-align: right;">447 / 1000 (45 %)</td>
    <td style="white-space: nowrap; text-align: right;">490 / 1000 (49 %)</td>
    <td style="white-space: nowrap; text-align: right;">356 / 1000 (36 %)</td>
    <td style="white-space: nowrap; text-align: right;">388 / 1000 (39 %)</td>
    <td style="white-space: nowrap; text-align: right;">340 / 1000 (34 %)</td>
    <td style="white-space: nowrap; text-align: right;">4198 / 10612 (40 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">webis_bias_flipper_18</th>
    <td style="white-space: nowrap; text-align: right;">329 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">394 / 1000 (39 %)</td>
    <td style="white-space: nowrap; text-align: right;">45 / 1000 (4 %)</td>
    <td style="white-space: nowrap; text-align: right;">243 / 612 (40 %)</td>
    <td style="white-space: nowrap; text-align: right;">6 / 1000 (1 %)</td>
    <td style="white-space: nowrap; text-align: right;">255 / 1000 (26 %)</td>
    <td style="white-space: nowrap; text-align: right;">339 / 1000 (34 %)</td>
    <td style="white-space: nowrap; text-align: right;">149 / 1000 (15 %)</td>
    <td style="white-space: nowrap; text-align: right;">117 / 1000 (12 %)</td>
    <td style="white-space: nowrap; text-align: right;">325 / 1000 (32 %)</td>
    <td style="white-space: nowrap; text-align: right;">534 / 1000 (53 %)</td>
    <td style="white-space: nowrap; text-align: right;">362 / 1000 (36 %)</td>
    <td style="white-space: nowrap; text-align: right;">2564 / 10612 (24 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">webis_news_bias_20</th>
    <td style="white-space: nowrap; text-align: right;">334 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">355 / 1000 (36 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">250 / 612 (41 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">522 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">495 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">474 / 1000 (47 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">332 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">328 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">332 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">4590 / 10612 (43 %)</td>
</tr>
</table>

### RoBERTa base

<table>
<tr>
    <th></th>
    <th>article_bias_prediction</th>
    <th>commoncrawl_news_articles</th>
    <th>dem_rep_party_platform_topics</th>
    <th>gpt4_political_bias</th>
    <th>gpt4_political_ideologies</th>
    <th>media_political_stance</th>
    <th>parliament_speeches_2024</th>
    <th>political_podcasts</th>
    <th>political_tweets</th>
    <th>qbias</th>
    <th>webis_bias_flipper_18</th>
    <th>webis_news_bias_20</th>
    <th>average</th>
</tr>
<tr>
    <th style="white-space: nowrap;">article_bias_prediction</th>
    <td style="white-space: nowrap; text-align: right;">609 / 1000 (61 %)</td>
    <td style="white-space: nowrap; text-align: right;">451 / 1000 (45 %)</td>
    <td style="white-space: nowrap; text-align: right;">393 / 1000 (39 %)</td>
    <td style="white-space: nowrap; text-align: right;">173 / 612 (28 %)</td>
    <td style="white-space: nowrap; text-align: right;">345 / 1000 (34 %)</td>
    <td style="white-space: nowrap; text-align: right;">435 / 1000 (44 %)</td>
    <td style="white-space: nowrap; text-align: right;">481 / 1000 (48 %)</td>
    <td style="white-space: nowrap; text-align: right;">211 / 1000 (21 %)</td>
    <td style="white-space: nowrap; text-align: right;">479 / 1000 (48 %)</td>
    <td style="white-space: nowrap; text-align: right;">381 / 1000 (38 %)</td>
    <td style="white-space: nowrap; text-align: right;">370 / 1000 (37 %)</td>
    <td style="white-space: nowrap; text-align: right;">521 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">4240 / 10612 (40 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">commoncrawl_news_articles</th>
    <td style="white-space: nowrap; text-align: right;">432 / 1000 (43 %)</td>
    <td style="white-space: nowrap; text-align: right;">810 / 1000 (81 %)</td>
    <td style="white-space: nowrap; text-align: right;">255 / 1000 (26 %)</td>
    <td style="white-space: nowrap; text-align: right;">173 / 612 (28 %)</td>
    <td style="white-space: nowrap; text-align: right;">424 / 1000 (42 %)</td>
    <td style="white-space: nowrap; text-align: right;">574 / 1000 (57 %)</td>
    <td style="white-space: nowrap; text-align: right;">390 / 1000 (39 %)</td>
    <td style="white-space: nowrap; text-align: right;">591 / 1000 (59 %)</td>
    <td style="white-space: nowrap; text-align: right;">469 / 1000 (47 %)</td>
    <td style="white-space: nowrap; text-align: right;">379 / 1000 (38 %)</td>
    <td style="white-space: nowrap; text-align: right;">433 / 1000 (43 %)</td>
    <td style="white-space: nowrap; text-align: right;">542 / 1000 (54 %)</td>
    <td style="white-space: nowrap; text-align: right;">4662 / 10612 (44 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">gpt4_political_bias</th>
    <td style="white-space: nowrap; text-align: right;">334 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">333 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">517 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">576 / 612 (94 %)</td>
    <td style="white-space: nowrap; text-align: right;">652 / 1000 (65 %)</td>
    <td style="white-space: nowrap; text-align: right;">493 / 1000 (49 %)</td>
    <td style="white-space: nowrap; text-align: right;">407 / 1000 (41 %)</td>
    <td style="white-space: nowrap; text-align: right;">493 / 1000 (49 %)</td>
    <td style="white-space: nowrap; text-align: right;">597 / 1000 (60 %)</td>
    <td style="white-space: nowrap; text-align: right;">334 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">331 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">331 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">4822 / 11000 (44 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">qbias</th>
    <td style="white-space: nowrap; text-align: right;">332 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">332 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">250 / 612 (41 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">332 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">332 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">332 / 1000 (33 %)</td>
    <td style="white-space: nowrap; text-align: right;">4578 / 10612 (43 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">webis_bias_flipper_18</th>
    <td style="white-space: nowrap; text-align: right;">443 / 1000 (44 %)</td>
    <td style="white-space: nowrap; text-align: right;">516 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">493 / 1000 (49 %)</td>
    <td style="white-space: nowrap; text-align: right;">252 / 612 (41 %)</td>
    <td style="white-space: nowrap; text-align: right;">499 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">444 / 1000 (44 %)</td>
    <td style="white-space: nowrap; text-align: right;">347 / 1000 (35 %)</td>
    <td style="white-space: nowrap; text-align: right;">506 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">506 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">357 / 1000 (36 %)</td>
    <td style="white-space: nowrap; text-align: right;">761 / 1000 (76 %)</td>
    <td style="white-space: nowrap; text-align: right;">576 / 1000 (58 %)</td>
    <td style="white-space: nowrap; text-align: right;">4939 / 10612 (47 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">webis_news_bias_20</th>
    <td style="white-space: nowrap; text-align: right;">550 / 1000 (55 %)</td>
    <td style="white-space: nowrap; text-align: right;">478 / 1000 (48 %)</td>
    <td style="white-space: nowrap; text-align: right;">85 / 1000 (8 %)</td>
    <td style="white-space: nowrap; text-align: right;">178 / 612 (29 %)</td>
    <td style="white-space: nowrap; text-align: right;">3 / 1000 (0 %)</td>
    <td style="white-space: nowrap; text-align: right;">430 / 1000 (43 %)</td>
    <td style="white-space: nowrap; text-align: right;">377 / 1000 (38 %)</td>
    <td style="white-space: nowrap; text-align: right;">507 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">404 / 1000 (40 %)</td>
    <td style="white-space: nowrap; text-align: right;">400 / 1000 (40 %)</td>
    <td style="white-space: nowrap; text-align: right;">515 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">824 / 1000 (82 %)</td>
    <td style="white-space: nowrap; text-align: right;">3927 / 10612 (37 %)</td>
</tr>
</table>

## without the center leaning class

### POLITICS

<table>
<tr>
    <th></th>
    <th>article_bias_prediction</th>
    <th>commoncrawl_news_articles</th>
    <th>dem_rep_party_platform_topics</th>
    <th>gpt4_political_bias</th>
    <th>gpt4_political_ideologies</th>
    <th>media_political_stance</th>
    <th>parliament_speeches_2024</th>
    <th>political_podcasts</th>
    <th>political_tweets</th>
    <th>qbias</th>
    <th>webis_bias_flipper_18</th>
    <th>webis_news_bias_20</th>
    <th>average</th>
</tr>
<tr>
    <th style="white-space: nowrap;">dem_rep_party_platform_topics</th>
    <td style="white-space: nowrap; text-align: right;">567 / 1000 (57 %)</td>
    <td style="white-space: nowrap; text-align: right;">553 / 1000 (55 %)</td>
    <td style="white-space: nowrap; text-align: right;">757 / 1000 (76 %)</td>
    <td style="white-space: nowrap; text-align: right;">330 / 434 (76 %)</td>
    <td style="white-space: nowrap; text-align: right;">820 / 1000 (82 %)</td>
    <td style="white-space: nowrap; text-align: right;">615 / 1000 (62 %)</td>
    <td style="white-space: nowrap; text-align: right;">531 / 1000 (53 %)</td>
    <td style="white-space: nowrap; text-align: right;">745 / 1000 (74 %)</td>
    <td style="white-space: nowrap; text-align: right;">632 / 1000 (63 %)</td>
    <td style="white-space: nowrap; text-align: right;">544 / 1000 (54 %)</td>
    <td style="white-space: nowrap; text-align: right;">594 / 1000 (59 %)</td>
    <td style="white-space: nowrap; text-align: right;">580 / 1000 (58 %)</td>
    <td style="white-space: nowrap; text-align: right;">6511 / 10434 (62 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">gpt4_political_ideologies</th>
    <td style="white-space: nowrap; text-align: right;">601 / 1000 (60 %)</td>
    <td style="white-space: nowrap; text-align: right;">550 / 1000 (55 %)</td>
    <td style="white-space: nowrap; text-align: right;">576 / 1000 (58 %)</td>
    <td style="white-space: nowrap; text-align: right;">348 / 434 (80 %)</td>
    <td style="white-space: nowrap; text-align: right;">982 / 1000 (98 %)</td>
    <td style="white-space: nowrap; text-align: right;">607 / 1000 (61 %)</td>
    <td style="white-space: nowrap; text-align: right;">521 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">684 / 1000 (68 %)</td>
    <td style="white-space: nowrap; text-align: right;">605 / 1000 (60 %)</td>
    <td style="white-space: nowrap; text-align: right;">559 / 1000 (56 %)</td>
    <td style="white-space: nowrap; text-align: right;">688 / 1000 (69 %)</td>
    <td style="white-space: nowrap; text-align: right;">648 / 1000 (65 %)</td>
    <td style="white-space: nowrap; text-align: right;">6387 / 10434 (61 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">media_political_stance</th>
    <td style="white-space: nowrap; text-align: right;">821 / 1000 (82 %)</td>
    <td style="white-space: nowrap; text-align: right;">708 / 1000 (71 %)</td>
    <td style="white-space: nowrap; text-align: right;">560 / 1000 (56 %)</td>
    <td style="white-space: nowrap; text-align: right;">201 / 434 (46 %)</td>
    <td style="white-space: nowrap; text-align: right;">741 / 1000 (74 %)</td>
    <td style="white-space: nowrap; text-align: right;">905 / 1000 (90 %)</td>
    <td style="white-space: nowrap; text-align: right;">457 / 1000 (46 %)</td>
    <td style="white-space: nowrap; text-align: right;">789 / 1000 (79 %)</td>
    <td style="white-space: nowrap; text-align: right;">605 / 1000 (60 %)</td>
    <td style="white-space: nowrap; text-align: right;">638 / 1000 (64 %)</td>
    <td style="white-space: nowrap; text-align: right;">888 / 1000 (89 %)</td>
    <td style="white-space: nowrap; text-align: right;">850 / 1000 (85 %)</td>
    <td style="white-space: nowrap; text-align: right;">7258 / 10434 (70 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">parliament_speeches_2024</th>
    <td style="white-space: nowrap; text-align: right;">537 / 1000 (54 %)</td>
    <td style="white-space: nowrap; text-align: right;">471 / 1000 (47 %)</td>
    <td style="white-space: nowrap; text-align: right;">481 / 1000 (48 %)</td>
    <td style="white-space: nowrap; text-align: right;">264 / 434 (61 %)</td>
    <td style="white-space: nowrap; text-align: right;">566 / 1000 (57 %)</td>
    <td style="white-space: nowrap; text-align: right;">468 / 1000 (47 %)</td>
    <td style="white-space: nowrap; text-align: right;">744 / 1000 (74 %)</td>
    <td style="white-space: nowrap; text-align: right;">496 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">415 / 1000 (42 %)</td>
    <td style="white-space: nowrap; text-align: right;">515 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">573 / 1000 (57 %)</td>
    <td style="white-space: nowrap; text-align: right;">563 / 1000 (56 %)</td>
    <td style="white-space: nowrap; text-align: right;">5349 / 10434 (51 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">political_podcasts</th>
    <td style="white-space: nowrap; text-align: right;">789 / 1000 (79 %)</td>
    <td style="white-space: nowrap; text-align: right;">650 / 1000 (65 %)</td>
    <td style="white-space: nowrap; text-align: right;">572 / 1000 (57 %)</td>
    <td style="white-space: nowrap; text-align: right;">262 / 434 (60 %)</td>
    <td style="white-space: nowrap; text-align: right;">707 / 1000 (71 %)</td>
    <td style="white-space: nowrap; text-align: right;">682 / 1000 (68 %)</td>
    <td style="white-space: nowrap; text-align: right;">521 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">997 / 1000 (100 %)</td>
    <td style="white-space: nowrap; text-align: right;">508 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">619 / 1000 (62 %)</td>
    <td style="white-space: nowrap; text-align: right;">833 / 1000 (83 %)</td>
    <td style="white-space: nowrap; text-align: right;">787 / 1000 (79 %)</td>
    <td style="white-space: nowrap; text-align: right;">6930 / 10434 (66 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">political_tweets</th>
    <td style="white-space: nowrap; text-align: right;">716 / 1000 (72 %)</td>
    <td style="white-space: nowrap; text-align: right;">666 / 1000 (67 %)</td>
    <td style="white-space: nowrap; text-align: right;">590 / 1000 (59 %)</td>
    <td style="white-space: nowrap; text-align: right;">295 / 434 (68 %)</td>
    <td style="white-space: nowrap; text-align: right;">727 / 1000 (73 %)</td>
    <td style="white-space: nowrap; text-align: right;">668 / 1000 (67 %)</td>
    <td style="white-space: nowrap; text-align: right;">507 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">722 / 1000 (72 %)</td>
    <td style="white-space: nowrap; text-align: right;">709 / 1000 (71 %)</td>
    <td style="white-space: nowrap; text-align: right;">574 / 1000 (57 %)</td>
    <td style="white-space: nowrap; text-align: right;">747 / 1000 (75 %)</td>
    <td style="white-space: nowrap; text-align: right;">714 / 1000 (71 %)</td>
    <td style="white-space: nowrap; text-align: right;">6926 / 10434 (66 %)</td>
</tr>
</table>

### BERT base (cased)

<table>
<tr>
    <th></th>
    <th>article_bias_prediction</th>
    <th>commoncrawl_news_articles</th>
    <th>dem_rep_party_platform_topics</th>
    <th>gpt4_political_bias</th>
    <th>gpt4_political_ideologies</th>
    <th>media_political_stance</th>
    <th>parliament_speeches_2024</th>
    <th>political_podcasts</th>
    <th>political_tweets</th>
    <th>qbias</th>
    <th>webis_bias_flipper_18</th>
    <th>webis_news_bias_20</th>
    <th>average</th>
</tr>
<tr>
    <th style="white-space: nowrap;">dem_rep_party_platform_topics</th>
    <td style="white-space: nowrap; text-align: right;">501 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">744 / 1000 (74 %)</td>
    <td style="white-space: nowrap; text-align: right;">271 / 434 (62 %)</td>
    <td style="white-space: nowrap; text-align: right;">681 / 1000 (68 %)</td>
    <td style="white-space: nowrap; text-align: right;">492 / 1000 (49 %)</td>
    <td style="white-space: nowrap; text-align: right;">527 / 1000 (53 %)</td>
    <td style="white-space: nowrap; text-align: right;">603 / 1000 (60 %)</td>
    <td style="white-space: nowrap; text-align: right;">541 / 1000 (54 %)</td>
    <td style="white-space: nowrap; text-align: right;">492 / 1000 (49 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">507 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">5615 / 10434 (54 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">gpt4_political_ideologies</th>
    <td style="white-space: nowrap; text-align: right;">481 / 1000 (48 %)</td>
    <td style="white-space: nowrap; text-align: right;">462 / 1000 (46 %)</td>
    <td style="white-space: nowrap; text-align: right;">581 / 1000 (58 %)</td>
    <td style="white-space: nowrap; text-align: right;">333 / 434 (77 %)</td>
    <td style="white-space: nowrap; text-align: right;">979 / 1000 (98 %)</td>
    <td style="white-space: nowrap; text-align: right;">532 / 1000 (53 %)</td>
    <td style="white-space: nowrap; text-align: right;">510 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">553 / 1000 (55 %)</td>
    <td style="white-space: nowrap; text-align: right;">542 / 1000 (54 %)</td>
    <td style="white-space: nowrap; text-align: right;">487 / 1000 (49 %)</td>
    <td style="white-space: nowrap; text-align: right;">518 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">470 / 1000 (47 %)</td>
    <td style="white-space: nowrap; text-align: right;">5469 / 10434 (52 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">media_political_stance</th>
    <td style="white-space: nowrap; text-align: right;">539 / 1000 (54 %)</td>
    <td style="white-space: nowrap; text-align: right;">627 / 1000 (63 %)</td>
    <td style="white-space: nowrap; text-align: right;">529 / 1000 (53 %)</td>
    <td style="white-space: nowrap; text-align: right;">172 / 434 (40 %)</td>
    <td style="white-space: nowrap; text-align: right;">534 / 1000 (53 %)</td>
    <td style="white-space: nowrap; text-align: right;">734 / 1000 (73 %)</td>
    <td style="white-space: nowrap; text-align: right;">455 / 1000 (46 %)</td>
    <td style="white-space: nowrap; text-align: right;">437 / 1000 (44 %)</td>
    <td style="white-space: nowrap; text-align: right;">488 / 1000 (49 %)</td>
    <td style="white-space: nowrap; text-align: right;">522 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">518 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">559 / 1000 (56 %)</td>
    <td style="white-space: nowrap; text-align: right;">5380 / 10434 (52 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">parliament_speeches_2024</th>
    <td style="white-space: nowrap; text-align: right;">501 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">450 / 1000 (45 %)</td>
    <td style="white-space: nowrap; text-align: right;">473 / 1000 (47 %)</td>
    <td style="white-space: nowrap; text-align: right;">185 / 434 (43 %)</td>
    <td style="white-space: nowrap; text-align: right;">501 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">483 / 1000 (48 %)</td>
    <td style="white-space: nowrap; text-align: right;">734 / 1000 (73 %)</td>
    <td style="white-space: nowrap; text-align: right;">543 / 1000 (54 %)</td>
    <td style="white-space: nowrap; text-align: right;">425 / 1000 (42 %)</td>
    <td style="white-space: nowrap; text-align: right;">506 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">498 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">504 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">5069 / 10434 (49 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">political_podcasts</th>
    <td style="white-space: nowrap; text-align: right;">492 / 1000 (49 %)</td>
    <td style="white-space: nowrap; text-align: right;">495 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">516 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">187 / 434 (43 %)</td>
    <td style="white-space: nowrap; text-align: right;">511 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">469 / 1000 (47 %)</td>
    <td style="white-space: nowrap; text-align: right;">534 / 1000 (53 %)</td>
    <td style="white-space: nowrap; text-align: right;">990 / 1000 (99 %)</td>
    <td style="white-space: nowrap; text-align: right;">495 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">473 / 1000 (47 %)</td>
    <td style="white-space: nowrap; text-align: right;">466 / 1000 (47 %)</td>
    <td style="white-space: nowrap; text-align: right;">517 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">5155 / 10434 (49 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">political_tweets</th>
    <td style="white-space: nowrap; text-align: right;">541 / 1000 (54 %)</td>
    <td style="white-space: nowrap; text-align: right;">593 / 1000 (59 %)</td>
    <td style="white-space: nowrap; text-align: right;">535 / 1000 (54 %)</td>
    <td style="white-space: nowrap; text-align: right;">277 / 434 (64 %)</td>
    <td style="white-space: nowrap; text-align: right;">519 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">544 / 1000 (54 %)</td>
    <td style="white-space: nowrap; text-align: right;">469 / 1000 (47 %)</td>
    <td style="white-space: nowrap; text-align: right;">477 / 1000 (48 %)</td>
    <td style="white-space: nowrap; text-align: right;">668 / 1000 (67 %)</td>
    <td style="white-space: nowrap; text-align: right;">513 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">549 / 1000 (55 %)</td>
    <td style="white-space: nowrap; text-align: right;">509 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">5526 / 10434 (53 %)</td>
</tr>
</table>

### RoBERTa base

<table>
<tr>
    <th></th>
    <th>article_bias_prediction</th>
    <th>commoncrawl_news_articles</th>
    <th>dem_rep_party_platform_topics</th>
    <th>gpt4_political_bias</th>
    <th>gpt4_political_ideologies</th>
    <th>media_political_stance</th>
    <th>parliament_speeches_2024</th>
    <th>political_podcasts</th>
    <th>political_tweets</th>
    <th>qbias</th>
    <th>webis_bias_flipper_18</th>
    <th>webis_news_bias_20</th>
    <th>average</th>
</tr>
<tr>
    <th style="white-space: nowrap;">dem_rep_party_platform_topics</th>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">184 / 434 (42 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">5184 / 10434 (50 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">gpt4_political_ideologies</th>
    <td style="white-space: nowrap; text-align: right;">508 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">474 / 1000 (47 %)</td>
    <td style="white-space: nowrap; text-align: right;">582 / 1000 (58 %)</td>
    <td style="white-space: nowrap; text-align: right;">340 / 434 (78 %)</td>
    <td style="white-space: nowrap; text-align: right;">979 / 1000 (98 %)</td>
    <td style="white-space: nowrap; text-align: right;">552 / 1000 (55 %)</td>
    <td style="white-space: nowrap; text-align: right;">540 / 1000 (54 %)</td>
    <td style="white-space: nowrap; text-align: right;">578 / 1000 (58 %)</td>
    <td style="white-space: nowrap; text-align: right;">593 / 1000 (59 %)</td>
    <td style="white-space: nowrap; text-align: right;">495 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">512 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">521 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">5695 / 10434 (55 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">media_political_stance</th>
    <td style="white-space: nowrap; text-align: right;">637 / 1000 (64 %)</td>
    <td style="white-space: nowrap; text-align: right;">658 / 1000 (66 %)</td>
    <td style="white-space: nowrap; text-align: right;">489 / 1000 (49 %)</td>
    <td style="white-space: nowrap; text-align: right;">189 / 434 (44 %)</td>
    <td style="white-space: nowrap; text-align: right;">511 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">890 / 1000 (89 %)</td>
    <td style="white-space: nowrap; text-align: right;">450 / 1000 (45 %)</td>
    <td style="white-space: nowrap; text-align: right;">665 / 1000 (66 %)</td>
    <td style="white-space: nowrap; text-align: right;">496 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">555 / 1000 (56 %)</td>
    <td style="white-space: nowrap; text-align: right;">583 / 1000 (58 %)</td>
    <td style="white-space: nowrap; text-align: right;">623 / 1000 (62 %)</td>
    <td style="white-space: nowrap; text-align: right;">5856 / 10434 (56 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">parliament_speeches_2024</th>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">486 / 1000 (49 %)</td>
    <td style="white-space: nowrap; text-align: right;">509 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">235 / 434 (54 %)</td>
    <td style="white-space: nowrap; text-align: right;">513 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">493 / 1000 (49 %)</td>
    <td style="white-space: nowrap; text-align: right;">715 / 1000 (72 %)</td>
    <td style="white-space: nowrap; text-align: right;">518 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">449 / 1000 (45 %)</td>
    <td style="white-space: nowrap; text-align: right;">502 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">501 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">499 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">5205 / 10434 (50 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">political_podcasts</th>
    <td style="white-space: nowrap; text-align: right;">566 / 1000 (57 %)</td>
    <td style="white-space: nowrap; text-align: right;">545 / 1000 (55 %)</td>
    <td style="white-space: nowrap; text-align: right;">517 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">233 / 434 (54 %)</td>
    <td style="white-space: nowrap; text-align: right;">509 / 1000 (51 %)</td>
    <td style="white-space: nowrap; text-align: right;">583 / 1000 (58 %)</td>
    <td style="white-space: nowrap; text-align: right;">505 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">993 / 1000 (99 %)</td>
    <td style="white-space: nowrap; text-align: right;">498 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">522 / 1000 (52 %)</td>
    <td style="white-space: nowrap; text-align: right;">530 / 1000 (53 %)</td>
    <td style="white-space: nowrap; text-align: right;">526 / 1000 (53 %)</td>
    <td style="white-space: nowrap; text-align: right;">5534 / 10434 (53 %)</td>
</tr>
<tr>
    <th style="white-space: nowrap;">political_tweets</th>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">184 / 434 (42 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">500 / 1000 (50 %)</td>
    <td style="white-space: nowrap; text-align: right;">5184 / 10434 (50 %)</td>
</tr>
</table>

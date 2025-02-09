# Evaluation of existing politicalness classification models

PoliticalDebateLarge is an NLI classifier and has been supplied a simple zero-shot hypothesis `This text {is not / is}
about politics.`.

The measurements have been conducted using the methodology prescribed in [this document](/docs/model_evaluation) while
the datasets have been sampled to 1 000 rows each.

The resulting accuracies are stored in files

- [on politicalness datasets](results_politicalness_datasets.csv),
- [on political leaning datasets](results_political_leaning_datasets.csv)

and are recorded in the two tables below.

## On politicalness datasets

<table>
    <tr>
        <th></th>
        <th>Amazon reviews 2023</th>
        <th>DialogSum</th>
        <th>Free news</th>
        <th>Goodreads book genres</th>
        <th>IMDB</th>
        <th>IMDB movie genres</th>
        <th>Medium post titles</th>
        <th>News category</th>
        <th>PENS</th>
        <th>PoliBERTweet</th>
        <th>Political or not</th>
        <th>Recipes</th>
        <th>Reddit comments</th>
        <th>Reddit submissions</th>
        <th>Rotten Tomatoes</th>
        <th>Textbooks</th>
        <th>Tweet topic multi</th>
        <th>Yelp review full</th>
        <th>average</th>
    </tr>
    <tr>
        <th style="white-space: nowrap;">TopicPolitics</th>
        <td style="white-space: nowrap;">1000 / 1000 (100 %)</td>
        <td style="white-space: nowrap;">1000 / 1000 (100 %)</td>
        <td style="white-space: nowrap;">717 / 1000 (72 %)</td>
        <td style="white-space: nowrap;">1000 / 1000 (100 %)</td>
        <td style="white-space: nowrap;">1000 / 1000 (100 %)</td>
        <td style="white-space: nowrap;">995 / 1000 (100 %)</td>
        <td style="white-space: nowrap;">795 / 1000 (80 %)</td>
        <td style="white-space: nowrap;">791 / 1000 (79 %)</td>
        <td style="white-space: nowrap;">890 / 1000 (89 %)</td>
        <td style="white-space: nowrap;">821 / 1000 (82 %)</td>
        <td style="white-space: nowrap;">838 / 1000 (84 %)</td>
        <td style="white-space: nowrap;">1000 / 1000 (100 %)</td>
        <td style="white-space: nowrap;">986 / 1000 (99 %)</td>
        <td style="white-space: nowrap;">994 / 1000 (99 %)</td>
        <td style="white-space: nowrap;">993 / 1000 (99 %)</td>
        <td style="white-space: nowrap;">624 / 1000 (62 %)</td>
        <td style="white-space: nowrap;">997 / 1000 (100 %)</td>
        <td style="white-space: nowrap;">1000 / 1000 (100 %)</td>
        <td style="white-space: nowrap;">16441 / 18000 (91 %)</td>
    </tr>
    <tr>
        <th style="white-space: nowrap;">ClassifierMainSubjectPolitics</th>
        <td style="white-space: nowrap;">997 / 1000 (100 %)</td>
        <td style="white-space: nowrap;">996 / 1000 (100 %)</td>
        <td style="white-space: nowrap;">769 / 1000 (77 %)</td>
        <td style="white-space: nowrap;">987 / 1000 (99 %)</td>
        <td style="white-space: nowrap;">999 / 1000 (100 %)</td>
        <td style="white-space: nowrap;">972 / 1000 (97 %)</td>
        <td style="white-space: nowrap;">670 / 1000 (67 %)</td>
        <td style="white-space: nowrap;">705 / 1000 (70 %)</td>
        <td style="white-space: nowrap;">772 / 1000 (77 %)</td>
        <td style="white-space: nowrap;">617 / 1000 (62 %)</td>
        <td style="white-space: nowrap;">742 / 1000 (74 %)</td>
        <td style="white-space: nowrap;">1000 / 1000 (100 %)</td>
        <td style="white-space: nowrap;">964 / 1000 (96 %)</td>
        <td style="white-space: nowrap;">994 / 1000 (99 %)</td>
        <td style="white-space: nowrap;">996 / 1000 (100 %)</td>
        <td style="white-space: nowrap;">644 / 1000 (64 %)</td>
        <td style="white-space: nowrap;">990 / 1000 (99 %)</td>
        <td style="white-space: nowrap;">997 / 1000 (100 %)</td>
        <td style="white-space: nowrap;">15811 / 18000 (88 %)</td>
    </tr>
    <tr>
        <th style="white-space: nowrap;">PoliticalDebateLarge</th>
        <td style="white-space: nowrap;">992 / 1000 (99 %)</td>
        <td style="white-space: nowrap;">980 / 1000 (98 %)</td>
        <td style="white-space: nowrap;">842 / 1000 (84 %)</td>
        <td style="white-space: nowrap;">986 / 1000 (99 %)</td>
        <td style="white-space: nowrap;">994 / 1000 (99 %)</td>
        <td style="white-space: nowrap;">952 / 1000 (95 %)</td>
        <td style="white-space: nowrap;">949 / 1000 (95 %)</td>
        <td style="white-space: nowrap;">950 / 1000 (95 %)</td>
        <td style="white-space: nowrap;">978 / 1000 (98 %)</td>
        <td style="white-space: nowrap;">859 / 1000 (86 %)</td>
        <td style="white-space: nowrap;">996 / 1000 (100 %)</td>
        <td style="white-space: nowrap;">1000 / 1000 (100 %)</td>
        <td style="white-space: nowrap;">909 / 1000 (91 %)</td>
        <td style="white-space: nowrap;">980 / 1000 (98 %)</td>
        <td style="white-space: nowrap;">921 / 1000 (92 %)</td>
        <td style="white-space: nowrap;">955 / 1000 (96 %)</td>
        <td style="white-space: nowrap;">975 / 1000 (98 %)</td>
        <td style="white-space: nowrap;">994 / 1000 (99 %)</td>
        <td style="white-space: nowrap;">17212 / 18000 (96 %)</td>
    </tr>
</table>

## On political leaning datasets

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
        <th style="white-space: nowrap;">TopicPolitics</th>
        <td style="white-space: nowrap;">622 / 1000 (62 %)</td>
        <td style="white-space: nowrap;">178 / 1000 (18 %)</td>
        <td style="white-space: nowrap;">686 / 1000 (69 %)</td>
        <td style="white-space: nowrap;">198 / 612 (32 %)</td>
        <td style="white-space: nowrap;">769 / 1000 (77 %)</td>
        <td style="white-space: nowrap;">408 / 1000 (41 %)</td>
        <td style="white-space: nowrap;">774 / 1000 (77 %)</td>
        <td style="white-space: nowrap;">262 / 1000 (26 %)</td>
        <td style="white-space: nowrap;">393 / 1000 (39 %)</td>
        <td style="white-space: nowrap;">515 / 1000 (52 %)</td>
        <td style="white-space: nowrap;">692 / 1000 (69 %)</td>
        <td style="white-space: nowrap;">642 / 1000 (64 %)</td>
        <td style="white-space: nowrap;">6139 / 11612 (53 %)</td>
    </tr>
    <tr>
        <th style="white-space: nowrap;">ClassifierMainSubjectPolitics</th>
        <td style="white-space: nowrap;">534 / 1000 (53 %)</td>
        <td style="white-space: nowrap;">241 / 1000 (24 %)</td>
        <td style="white-space: nowrap;">540 / 1000 (54 %)</td>
        <td style="white-space: nowrap;">305 / 612 (50 %)</td>
        <td style="white-space: nowrap;">101 / 1000 (10 %)</td>
        <td style="white-space: nowrap;">468 / 1000 (47 %)</td>
        <td style="white-space: nowrap;">600 / 1000 (60 %)</td>
        <td style="white-space: nowrap;">54 / 1000 (5 %)</td>
        <td style="white-space: nowrap;">373 / 1000 (37 %)</td>
        <td style="white-space: nowrap;">413 / 1000 (41 %)</td>
        <td style="white-space: nowrap;">602 / 1000 (60 %)</td>
        <td style="white-space: nowrap;">561 / 1000 (56 %)</td>
        <td style="white-space: nowrap;">4792 / 11612 (41 %)</td>
    </tr>
    <tr>
        <th>PoliticalDebateLarge</th>
        <td>875 / 1000 (88 %)</td>
        <td>338 / 1000 (34 %)</td>
        <td>971 / 1000 (97 %)</td>
        <td>612 / 612 (100 %)</td>
        <td>978 / 1000 (98 %)</td>
        <td>665 / 1000 (66 %)</td>
        <td>993 / 1000 (99 %)</td>
        <td>813 / 1000 (81 %)</td>
        <td>744 / 1000 (74 %)</td>
        <td>833 / 1000 (83 %)</td>
        <td>856 / 1000 (86 %)</td>
        <td>896 / 1000 (90 %)</td>
        <td>9574 / 11612 (82 %)</td>
    </tr>
</table>

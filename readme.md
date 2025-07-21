# Political Leaning and Politicalness Classification of Texts

The source code of the research done in the paper
[Political Leaning and Politicalness Classification of Texts](https://arxiv.org/abs/2507.13913), which addresses the
challenge of automatically classifying text according to political leaning and politicalness using transformer models.
We compose a comprehensive overview of existing datasets and models for these tasks, finding that current approaches
create siloed solutions that perform poorly on out-of-distribution texts. To address this limitation, we compile a
diverse dataset by combining 12 datasets for political leaning classification and creating a new dataset for
politicalness by extending 18 existing datasets with the appropriate label. Through extensive benchmarking with
leave-one-in and leave-one-out methodologies, we evaluate the performance of existing models and train new ones with
enhanced generalization capabilities.

## Models

As a part of the research, we have produced two models achieving state-of-the-art performance on all the collected
datasets: [political-leaning-deberta-large](https://huggingface.co/matous-volf/political-leaning-deberta-large)
and [political-leaning-politics](https://huggingface.co/matous-volf/political-leaning-politics).

## Demo web app

The demo web app in [`demo/political_leaning_prediction_web`](demo/political_leaning_prediction_web) is deployed at
[political-leaning.matousvolf.cz](https://political-leaning.matousvolf.cz/) with the DeBERTa large model trained on all
datasets.

## Results

The complete results of all our measurements are stored in the [`results`](results) directory.

## Analysis

The Jupyter notebooks, which can be used to replicate our findings, are stored in the [`analysis`](analysis) directory.
Variables named with SCREAMING_SNAKE_CASE are meant to be edited for configuration.

## Dataset preprocessing guide

All the used datasets and links to them are listed in the paper. To preprocess them as described in the "Data
preprocessing" section, run the Jupyter notebooks in the
[`datasets/politicalness/notebooks`](datasets/politicalness/notebooks) and
[`datasets/political_leaning/notebooks`](datasets/political_leaning/notebooks) directories. The preprocessed datasets
will be placed into [`datasets/politicalness/preprocessed`](datasets/politicalness/preprocessed) and
[`datasets/political_leaning/preprocessed`](datasets/political_leaning/preprocessed). Some datasets are retrieved
automatically by the notebook, some need to be downloaded manually beforehand – these are listed below.

### Politicalness

Place the datasets into the [`datasets/politicalness/raw`](datasets/politicalness/raw) directory with the following
structure:

- Free news dataset (Git commit f3dfb99)

  🡒 `free-news-dataset`

- PoliBERTweet

  🡒 `polibertweet/published_data_polibertweet-LREC-2022_election_sampled_10000.csv`

  🡒 `polibertweet/published_data_polibertweet-LREC-2022_non_election_sampled_10000.csv`

### Political leaning

Place the datasets into the [`datasets/political_leaning/raw`](datasets/political_leaning/raw) directory with the
following structure:

- Article bias prediction (Git commit ced8111)

  `data/jsons` 🡒 `article_bias_prediction`

- BIGNEWSBLN

  🡒 `bignewsbln/BIGNEWSBLN_center.json`

  🡒 `bignewsbln/BIGNEWSBLN_left.json`

  🡒 `bignewsbln/BIGNEWSBLN_right.json`

- CommonCrawl news articles (version 10.5281/zenodo.7476697)

  `news_articles.db` 🡒 `commoncrawl_news_articles/articles.db`

  `outlet-config.json` 🡒 `commoncrawl_news_articles/outlets.json`

- Media political stance (version 10.5281/zenodo.8417761)

  `poliOscar.complete.en` 🡒 `media_political_stance.tsv`

- Qbias (version 10.5281/zenodo.7682915)

  `allsides_balanced_news_headlines-texts.csv` 🡒 `qbias.csv`

- Webis bias flipper 18 (version 10.5281/zenodo.3250686)

  🡒 `webis_bias_flipper_18.csv`

- Webis news bias 20 (version 10.5281/zenodo.8321586)

  🡒 `webis_news_bias_20.json`

## Authors

- Matous Volf ([me@matousvolf.cz](mailto:me@matousvolf.cz)),
  [DELTA – High school of computer science and economics](https://www.delta-skola.cz), Pardubice, Czechia
- Jakub Simko ([jakub.simko@kinit.sk](mailto:jakub.simko@kinit.sk)),
  [Kempelen Institute of Intelligent Technologies](https://kinit.sk), Bratislava, Slovakia

## Citation

### BibTeX

```bibtex
@misc{volf-simko-2025-political-leaning,
  title        = {Political Leaning and Politicalness Classification of Texts},
  author       = {Matous Volf and Jakub Simko},
  year         = 2025,
  url          = {https://arxiv.org/abs/2507.13913},
  eprint       = {2507.13913},
  archiveprefix = {arXiv},
  primaryclass = {cs.CL}
}
```

### APA

Volf, M. and Simko, J. (2025). Political Leaning and Politicalness Classification of Texts. DELTA – High school of
computer science and economics, Pardubice, Czechia; Kempelen Institute of Intelligent Technologies, Bratislava,
Slovakia.

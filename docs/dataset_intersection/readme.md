# Dataset intersection

## Methodology

The intersections of texts between every pair of datasets have been measured by comparing the titles. If two
rows have the same title, they are considered the same.

Some datasets do not have a title field, so it is necessary to compare the bodies in some way. A primitive char-to-char
string comparison does not serve this purpose, because different article scrapers include different parts of the page,
for instance the title of the comment section. Sophisticated string similarity algorithms (e.g. the Levenstein distance)
are not a viable option, since they have relatively high time complexities. A simpler algorithm has been chosen: slicing
a middle part (50 characters by default or less if the body is shorter) out of one article and testing, whether the
second article contains it. Slicing the middle is considered optimal, as that is the part with the least probability of
a scraping mismatch. Still, this method only gives an estimate of the true intersection – for example, there are
instances of false positive matches caused by two articles both citing one politician's statement in their middle.

Beforehand, both the titles and the bodies have been stripped of any non-letter characters (even whitespace) and
converted to lowercase, so that irrelevant text discrepancies don't manifest.

The measurement can be replicated using [this notebook](../../analysis/dataset_intersection/notebook.ipynb).

## Results

- [Politicalness](politicalness)
- [Political leaning](political_leaning)

The percentages in each row mean the portion of the intersection over all the articles in the dataset in the
corresponding row. For example in the political leaning datasets, the Article bias prediction dataset has an
intersection of 353 articles with the CommonCrawl news articles dataset, which is 0.9 % of the Article bias prediction
dataset. In the CommonCrawl news articles dataset row, the intersection size is the same number (353), but that equals
to 0.4 % of that dataset.

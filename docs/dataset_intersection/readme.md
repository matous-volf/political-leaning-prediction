# Dataset intersection

## Methodology

The intersections of texts between every pair of datasets have been measured by comparing the titles and bodies.

Beforehand, both the titles and the bodies have been stripped of any non-letter characters (even whitespace) and
converted to lowercase, so that irrelevant text discrepancies don't manifest.

Some rows or even whole datasets do not contain a title field, so it is necessary to compare the bodies in some way. A
primitive char-to-char string comparison does not serve this purpose, because, e.g., different web scrapers include
different parts of the page, for instance the title of the comment section. Sophisticated string similarity algorithms
(e.g. the Levenstein distance) are not a viable option, since they have high time complexities for such a large amount
of text. A simpler algorithm has been chosen: slicing a middle part (50 characters by default or less if the body is
shorter) out of the first dataset's row's body and testing, whether the second dataset's row's body contains it. Slicing
the middle is considered optimal, as that is the part with the least probability of a scraping mismatch. Still, this
method only gives an estimate of the true intersection – for example, there are instances of false positive matches
caused by two texts both citing one politician's statement in their middle.

There are a total of nine possible combinations of the row pair's titles and bodies presence or absence. Each one
requires its own comparison approach, as shown in the table below.

<table>
<tr>
    <th colspan="2" rowspan="2"></th>
    <th colspan="3">1st dataset's row</th>
</tr>
<tr>
    <th>only has a title</th>
    <th>only has a body</th>
    <th>has both</th>
</tr>
<tr>
    <th rowspan="3">2nd dataset's row</th>
    <th>only has a title</th>
    <td>titles are equal</td>
    <td>body contains title</td>
    <td>titles are equal</td>
</tr>
<tr>
    <th>only has a body</th>
    <td>body contains title</td>
    <td>2nd body contains 1st body slice</td>
    <td>2nd body contains 1st body slice</td>
</tr>
<tr>
    <th>has both</th>
    <td>titles are equal</td>
    <td>2nd body contains 1st body slice</td>
    <td>titles are equal</td>
</tr>
</table>

The measurements can be replicated using [this notebook](/analysis/dataset_intersection/notebook.ipynb).

## Results

- [Politicalness](politicalness)
- [Political leaning](political_leaning)

The percentages in each row mean the portion of the intersection over all the instances in the dataset in the
corresponding table row. For example in the political leaning datasets, the Article bias prediction dataset has an
intersection of 353 instances with the CommonCrawl news articles dataset, which is 0.9 % of the Article bias prediction
dataset. In the CommonCrawl news articles dataset row, the intersection size is the same number (353), but that equals
to 0.4 % of that dataset.

# Dataset intersection

The intersections of articles between every pair of datasets have been measured by comparing the article titles. If two
articles have the same title (trimmed of leading and trailing whitespace), they are considered the same.

An exception is the CommonCrawl dataset, which doesn't have a title column. So it is necessary to compare the bodies in
some way. A primitive char-to-char string comparison does not serve this purpose, because different article scrapers
include different parts of the page, for instance the title of the comment section. Sophisticated string similarity
algorithms (e.g. the Levenstein distance) are not a viable option, since they have relatively high time complexities. A
simpler algorithm has been chosen: slicing a middle part (e.g. 50 characters) out of one article and testing, whether
the second article contains it. Slicing the middle is considered optimal, as that is the part with the least probability
of a scraping mismatch. Still, this method only gives a rough estimate of the true intersection – for example, there are
instances of false positive matches caused by two articles both citing one politician's statement in their middle.

Beforehand, both the titles and the bodies are stripped of any non-letter characters (even whitespace), so
that irrelevant text discrepancies don't manifest.

The results are recorded in the table below and can be replicated using [this notebook](notebook.ipynb).

<table>
    <tr>
        <th></th>
        <th>CommonCrawl news articles</th>
        <th>Article bias prediction</th>
        <th>Qbias</th>
        <th>Webis-News-Bias-20</th>
        <th>Webis-Bias-Flipper-18</th>
    </tr>
    <tr>
        <th>CommonCrawl news articles</th>
        <td>389471 (100.0 %)</td>
        <td>2514 (0.6 %)</td>
        <td>77 (0.0 %)</td>
        <td>611 (0.2 %)</td>
        <td>610 (0.2 %)</td>
    </tr>
    <tr>
        <th>Article bias prediction</th>
        <td>2514 (6.7 %)</td>
        <td>37490 (100.0 %)</td>
        <td>66 (0.2 %)</td>
        <td>3618 (9.7 %)</td>
        <td>2679 (7.1 %)</td>
    </tr>
    <tr>
        <th>Qbias</th>
        <td>77 (0.4 %)</td>
        <td>66 (0.3 %)</td>
        <td>21533 (100.0 %)</td>
        <td>28 (0.1 %)</td>
        <td>21 (0.1 %)</td>
    </tr>
    <tr>
        <th>Webis-News-Bias-20</th>
        <td>611 (8.1 %)</td>
        <td>3618 (48.2 %)</td>
        <td>28 (0.4 %)</td>
        <td>7514 (100.0 %)</td>
        <td>4831 (64.3 %)</td>
    </tr>
    <tr>
        <th>Webis-Bias-Flipper-18</th>
        <td>610 (9.8 %)</td>
        <td>2679 (43.0 %)</td>
        <td>21 (0.3 %)</td>
        <td>4831 (77.5 %)</td>
        <td>6237 (100.0 %)</td>
    </tr>
</table>

The percentages in each row mean the portion of the intersection over all the articles in the dataset in the
corresponding row. For example, the CommonCrawl news articles dataset has an intersection of 2514 articles with the
Article bias prediction dataset, which is 0.6 % of the CommonCrawl dataset. In the Article bias detection dataset row,
the intersection size is the same number (2514), but that equals to 6.7 % of that dataset.

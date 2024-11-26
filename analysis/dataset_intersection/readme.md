# Dataset intersection

The intersections of articles between every pair of datasets have been measured by comparing the article titles. If two
articles have the same title (trimmed of leading and trailing whitespace), they are considered the same.

Some datasets do not have a title field, so it is necessary to compare the bodies in some way. A primitive char-to-char
string comparison does not serve this purpose, because different article scrapers include different parts of the page,
for instance the title of the comment section. Sophisticated string similarity algorithms (e.g. the Levenstein distance)
are not a viable option, since they have relatively high time complexities. A simpler algorithm has been chosen: slicing
a middle part (50 characters by default or less if the body is shorter) out of one article and testing, whether the
second article contains it. Slicing the middle is considered optimal, as that is the part with the least probability of
a scraping mismatch. Still, this method only gives a rough estimate of the true intersection – for example, there are
instances of false positive matches caused by two articles both citing one politician's statement in their middle.
Moreover, this approach is very expensive when comparing two large datasets. For this reason, a sample (of 10 000
articles by default) is taken and measured from one of them and the resulting intersection size is multiplied
accordingly to make an approximation of the total number of matches.

Beforehand, both the titles and the bodies have been stripped of any non-letter characters (even whitespace) and
converted to lowercase, so that irrelevant text discrepancies don't manifest.

The results are recorded in the table below and can be replicated using [this notebook](notebook.ipynb).

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
</tr>
<tr>
  <th>Article bias prediction</th>
  <td>37550 (100.0 %)</td>
  <td>2622 (7.0 %)</td>
  <td>18 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>3457 (9.2 %)</td>
  <td>0 (0.0 %)</td>
  <td>9 (0.0 %)</td>
  <td>208 (0.6 %)</td>
  <td>66 (0.2 %)</td>
  <td>2713 (7.2 %)</td>
  <td>3681 (9.8 %)</td>
</tr>
<tr>
  <th>CommonCrawl news articles</th>
  <td>2622 (0.6 %)</td>
  <td>429805 (100.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>19083 (4.4 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>172 (0.0 %)</td>
  <td>344 (0.1 %)</td>
  <td>602 (0.1 %)</td>
</tr>
<tr>
  <th>Dem., rep. party platform topics</th>
  <td>18 (0.2 %)</td>
  <td>0 (0.0 %)</td>
  <td>11558 (100.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>146 (1.3 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>16 (0.1 %)</td>
  <td>17 (0.1 %)</td>
</tr>
<tr>
  <th>GPT-4 political bias</th>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>612 (100.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
</tr>
<tr>
  <th>GPT-4 political ideologies</th>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>3200 (100.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
</tr>
<tr>
  <th>Media political stance</th>
  <td>3457 (0.7 %)</td>
  <td>19083 (4.0 %)</td>
  <td>146 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>480163 (100.0 %)</td>
  <td>48 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>240 (0.0 %)</td>
  <td>720 (0.1 %)</td>
  <td>960 (0.2 %)</td>
</tr>
<tr>
  <th>Parliament speeches 2024</th>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>48 (0.2 %)</td>
  <td>24239 (100.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
</tr>
<tr>
  <th>PoliStance issue tweets</th>
  <td>9 (0.1 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>11208 (100.0 %)</td>
  <td>11208 (100.0 %)</td>
  <td>1 (0.0 %)</td>
  <td>2 (0.0 %)</td>
  <td>4 (0.0 %)</td>
</tr>
<tr>
  <th>Political tweets</th>
  <td>208 (0.1 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>11208 (5.9 %)</td>
  <td>189090 (100.0 %)</td>
  <td>95 (0.1 %)</td>
  <td>151 (0.1 %)</td>
  <td>170 (0.1 %)</td>
</tr>
<tr>
  <th>Qbias</th>
  <td>66 (0.3 %)</td>
  <td>172 (0.8 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>240 (1.1 %)</td>
  <td>0 (0.0 %)</td>
  <td>1 (0.0 %)</td>
  <td>95 (0.4 %)</td>
  <td>21715 (100.0 %)</td>
  <td>21 (0.1 %)</td>
  <td>28 (0.1 %)</td>
</tr>
<tr>
  <th>Webis bias flipper 18</th>
  <td>2713 (42.4 %)</td>
  <td>344 (5.4 %)</td>
  <td>16 (0.2 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>720 (11.2 %)</td>
  <td>0 (0.0 %)</td>
  <td>2 (0.0 %)</td>
  <td>151 (2.4 %)</td>
  <td>21 (0.3 %)</td>
  <td>6400 (100.0 %)</td>
  <td>4997 (78.1 %)</td>
</tr>
<tr>
  <th>Webis news bias 20</th>
  <td>3681 (47.7 %)</td>
  <td>602 (7.8 %)</td>
  <td>17 (0.2 %)</td>
  <td>0 (0.0 %)</td>
  <td>0 (0.0 %)</td>
  <td>960 (12.4 %)</td>
  <td>0 (0.0 %)</td>
  <td>4 (0.1 %)</td>
  <td>170 (2.2 %)</td>
  <td>28 (0.4 %)</td>
  <td>4997 (64.7 %)</td>
  <td>7722 (100.0 %)</td>
</tr>
</table>

The percentages in each row mean the portion of the intersection over all the articles in the dataset in the
corresponding row. For example, the Article bias prediction dataset has an intersection of 2 622 articles with the
CommonCrawl news articles dataset, which is 7.0 % of the Article bias prediction dataset. In the CommonCrawl news
articles dataset row, the intersection size is the same number (2 622), but that equals to 0.6 % of that dataset.

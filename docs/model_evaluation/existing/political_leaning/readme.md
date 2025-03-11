# Evaluation of existing political leaning classification models

DistilBertPoliticalBias and PoliticalIdeologiesRobertaFinetuned are in fact trained to predict conservative vs. liberal
leaning. That output has been mapped to right vs. left respectively. The same applies for DistilBertPoliticalTweets,
which is trained to predict republican vs. democratic leaning.

DistilBertPoliticalBias uses a 5-level spectrum, which has been reduced to a 3-level one by mapping both highly and
mildly left-leaning to the left-leaning class and the same for right-leaning.

PoliticalDebateLarge is an NLI classifier and has been supplied a simple zero-shot hypothesis `This text supports {left
/ center / right} political leaning.`, which may not be optimal, as no rigorous testing has been done beforehand.

According to their Hugging Face model cards, some models have been trained on some of the collected datasets. These
relationships are shown in the following table.

<table>
<tr>
    <th>model</th>
    <th>trained on</th>
</tr>
<tr>
    <td>PoliticalBiasBert</td>
    <td>Article bias prediction</td>
</tr>
<tr>
    <td>PoliticalBiasPredictionAllsidesDeberta</td>
    <td>Article bias prediction</td>
</tr>
<tr>
    <td>DistilBertPoliticalBias</td>
    <td>GPT-4 political bias</td>
</tr>
<tr>
    <td>PoliticalDebateLarge</td>
    <td>Dem., rep. party platform topics; Political tweets</td>
</tr>
<tr>
    <td>PoliticalIdeologiesRobertaFinetuned</td>
    <td>GPT-4 political ideologies</td>
</tr>
<tr>
    <td>DebertaPoliticalClassification</td>
    <td>Parliament speeches 2024</td>
</tr>
<tr>
    <td>DistilBertPoliticalTweets</td>
    <td>a subset of Political tweets</td>
</tr>
</table>

This gets reflected in the accuracy results: the models score very high on the datasets they've been trained on.

The measurements have been conducted using the methodology prescribed in [this document](/docs/model_evaluation) while
the datasets have been sampled to 1 000 rows each.

The resulting accuracies are stored in files

- [with center leaning class](results_with_center_leaning_class.csv),
- [without center leaning class](results_without_center_leaning_class.csv)

and are recorded in the two tables below.

TODO

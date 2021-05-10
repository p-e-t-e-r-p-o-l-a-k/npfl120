# EMBEDDINGS
## _REPORT_

In this report, I use cross-lingual embeddings for cross-lingual parsing.
I selected Czech-English and Swedish-English pairs to compare with previous homework (Tree-projection).

## Dictionaries

Using alignments provided for the previous homework, I first generate a dictionary. I select a pair if it appeared at least two times in the corpus.

This yields 513 Czech-English pairs and 758 Swedish-English pairs.

## Cross-lingual embeddings

I use the ``vecmap`` tool to generate multilingual embeddings. Specifically, I use the ``supervised`` setting.

The tool generates separate embeddings for source and target language. I concatenate these and remove duplicate entries.

## UDPipe training and evaluation

Using the cross-lingual embeddings, I train the parser for each language.

### Swedish-English

| Training data | Evaluation data |          Result          |
|:-------------:|:---------------:|:------------------------:|
|       en      |        en       | UAS: 85.04%, LAS: 83.01% |
|       sv      |        sv       | UAS: 84.89%, LAS: 81.08% |
|       en      |        sv       | UAS: 48.45%, LAS: 40.07% |
|       sv      |        en       | UAS: 61.56%, LAS: 54.88% |

### Czech-English

| Training data | Evaluation data |          Result          |
|:-------------:|:---------------:|:------------------------:|
|       en      |        en       | UAS: 85.04%, LAS: 83.01% |
|       cs      |        cs       | UAS: 85.83%, LAS: 83.06% |
|       en      |        cs       | UAS: 36.54%, LAS: 26.53% |
|       cs      |        en       | UAS: 61.61%, LAS: 53.19% |

## Tree-projection

Results from previous homework:

### Swedish-English

| source | target |        HEAD        |       DEPREL       |         LAS        |
|:------:|:------:|:------------------:|:------------------:|:------------------:|
|   en   |   sv   | 0.5675264758309742 | 0.6353675159903533 | 0.4431687113348013 |
|   sv   |   en   | 0.4931054023422743 | 0.6221666037023045 | 0.3894030978466188 |

### Czech-English

| source | target |        HEAD        |        DEPREL       |         LAS        |
|:------:|:------:|:------------------:|:-------------------:|:------------------:|
|   en   |   cs   | 0.3320795271359484 | 0.39145620634067707 | 0.1890918860827512 |
|   cs   |   en   | 0.2853702304495655 | 0.38061956932376273 | 0.1785039667548167 |


## Results

We see that the multilingual embeddings perform better than tree projection. Although, recall that the tree projection method could be implemented better. 

I see further potential for gains in a larger dictionary and more reliable dictionary (the dictionary used here is automatically generated from alignments from rather small data).
# CROSS-LINGUAL POS TAGGING
## _REPORT_

I chose Telugu from English for this task. 

First, I filter out sentences with no translation in the second language. Then I use `fast_align` to obtain word alignment in both directions. Using `atools`, I get intersection and union of both directions.

I evaluate the accuracy on the test set available in UD (`te_mtg-ud-test.conllu`).

* Baseline
    - NOUN everywhere
    - Accuracy: 23.86%
* Baseline 2
    - Pretrained Telugu model from UD
    - Accuracy: 90.57%
* Intersection of alignments
    1. Experiment
        - Sure alignments (target has one source word aligned and vice versa) = POS copied
        - No alignment = most frequent POS tag for the form
        - Accuracy: 21.64%
    2. Experiment
        - Sure alignments = POS copied
        - No alignment = most frequent POS tag for the form
        - Count only sure probabilities (where target has one aligned source and vice versa)
        - Accuracy: 32.32%
    3. Experiment
        - Sure alignments = POS copied
        - No alignment = most frequent POS tag for the form
        - Count only probabilities
        - NOUN where 0 or more than 1 source word aligned 
        - Accuracy: 43.00%
* Union of alignments
    1. Experiment
        - Sure alignments  = POS copied
        - No alignment = most frequent POS tag for the form
        - Accuracy: 33.43%
    2. Experiment
        - Sure alignments = POS copied
        - No alignment = most frequent POS tag for the form
        - Count only probabilities
        - Accuracy: 33.98%
    3. Experiment
        - Sure alignments  = POS copied
        - No alignment = most frequent POS tag for the form
        - Count only probabilities
        - NOUN where 0 or more than 1 source word aligned 
        - Accuracy: 42.30%

The best method for cross-lingual POS tag transfer is to use *intersection* of alignments and trust only sure alignments. Huge improvent could be achieved by using more related language than English.
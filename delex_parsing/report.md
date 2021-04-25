# CROSS-LINGUAL PARSING
## _REPORT_


### English to Telugu transfer
In this assignment, I reuse the tagging model from the previous assignment (cross-lingual POS tagging from English to Telugu).

The best model achieves an accuracy of 43%. I also manually inspect the POS tags and it seems that most of the words are assigned with the NOUN tag, only the last punctuation is mostly correct. 

1. Baseline - UD pretrained Telugu model
    - UAS: 90.29%, LAS: 81.55% 
2. Gold Telugu POS + delexicalized English parser
    - UAS: 60.33%, LAS: 44.94%
3. UD pretrained Telugu POS tagger + delexicalized English parser
    - UAS: 60.19%, LAS: 43.27%
4. Cross-lingual POS tagger (from previous HW) + delexicalized English parser
    - UAS: 65.05%, LAS: 37.31%

It seems strange that the UAS score got better with worse POS tagging accuracy. Though, more accurate tagging helps to improve LAS. 

After a brief manual inspection of the outputs, I suspect that the sentence structure of Telugu seems to be monotonous and can be easily guessed. That might explain, why better POS tagging worsens UAS. On the other hand, LAS is more dependent on POS. Hence, LAS increases with better POS.


### Czech to Slovak transfer

1. Baseline - UD pretrained Slovak model
    - UAS: 88.86%, LAS: 86.70%
2. Gold POS + delexicalized Czech parser
    - UAS: 82.58%, LAS: 77.39%
3. UD pretrained Slovak POS tagger + delexicalized Czech parser
    - UAS: 77.61%, LAS: 71.39%
4. UD pretrained Czech POS tagger + delexicalized Czech parser
    - UAS: 58.57%, LAS: 49.87%
5. Gold POS + lexicalized Czech parser
    - UAS: 76.84%, LAS: 68.35%
6. UD pretrained Slovak POS tagger + lexicalized Czech parser
    - UAS: 69.40%, LAS: 59.67%
7. Czech POS tagger + lexicalized Czech parser
    - UAS: 80.63%, LAS: 72.83%

Compared to Telugu and English, Slovak and Czech are related languages with a large portion of shared vocabulary. Therefore, the delexicalized Czech parser performs not much worse than Slovak one (experiment 2). 

Again, we can see that the POS quality is important for parsing (experiments 2-4). However, the compliance between tagger and parser is important for lexicalized parsing (see experiments 5,6 vs. 7). 

From the experiments is clear that direct use of Czech tagger and parser is the best option when no Slovak annotated data are available. 
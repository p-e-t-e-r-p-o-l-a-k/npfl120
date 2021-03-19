# WALS
## _REPORT_

## Data exploration
I use Pandas to load the data from the TSV file. I have briefly inspected the table and possible values in the feature fields. It has occurred to me that most of the values are not only categories but some kind of scale (e.g., 1A: Consonant Inventories - small, moderately small...). An important observation is that most features are missing for most languages.

## Similarity metric
I have tried two approaches:
- counting common values of features
- converting features into numbers and treating them as scale rather than categories; one minus the difference in a feature is the difference of values normalized to [0; 1]

## Results
1. Most similar languages to Slovak (including genus):
        ```
        [('cze', 'Slavic', 12),
         ('pol', 'Slavic', 9),
         ('swa', 'Bantoid', 9),
         ('fin', 'Finnic', 8),
         ('grk', 'Greek', 8)]
        ```
        The first two most similar are probably correct, but the later ones are only doubly correct (I would expect other Slavic languages).
        I guess that the problem is in the metric and/or in the many missing values.
    
    Most similar languages to German (including genus):
        ```
        [('eng', 'Germanic', 103),
         ('fre', 'Romance', 103),
         ('rus', 'Slavic', 100),
         ('grk', 'Greek', 90),
         ('spa', 'Romance', 87)]
        ```
        Again, English seems to be correct (although I'd expect Dutch). Slavic Russian is incorrect.
        
    The same results with the second metric:
        ```
        [('cze', 'Slavic', 12.0),
         ('fin', 'Finnic', 10.816666666666666),
         ('geo', 'Kartvelian', 10.813095238095237),
         ('ger', 'Germanic', 10.613095238095237),
         ('swa', 'Bantoid', 10.57857142857143)]
        ```
        ```
        [('fre', 'Romance', 129.37177871148458),
         ('eng', 'Germanic', 128.66500933706817),
         ('rus', 'Slavic', 125.99437441643325),
         ('grk', 'Greek', 122.4483426704015),
         ('spa', 'Romance', 121.46223155929039)]
        ```
    The second metric seems to even worse than the first one.
2. Centroid
    Slavic languages (second column - #nan featurs; third column - genus similarity score):
    ```
    [('rus', 36, 386),
     ('pol', 103, 352),
     ('bul', 108, 306),
     ('ukr', 136, 297),
     ('scr', 132, 290),
     ('cze', 134, 266),
     ('slo', 149, 259),
     ('mcd', 154, 210),
     ('blr', 162, 152),
     ('srb', 167, 72),
     ('svk', 179, 72),
     ('sou', 185, 45),
     ('ksu', 191, 12),
     ('srl', 190, 12),
     ('svc', 189, 7),
     ('plb', 189, 4),
     ('bos', 191, 2)]
     ```
    The correlation between #nan features and a genus similarity score is -0.91. Therefore, the most similar language is probably the best annotated one.
    
    Same for Germanic genus:
    ```
    [('eng', 33, 417),
     ('ger', 35, 417),
     ('swe', 114, 340),
     ('dut', 103, 332),
     ('ice', 115, 290),
     ('nor', 125, 290),
     ('dsh', 134, 289),
     ('fri', 168, 105),
     ('afr', 176, 71),
     ('far', 181, 42),
     ('dbr', 191, 13),
     ('dli', 191, 13),
     ('duz', 191, 13),
     ('gau', 191, 13),
     ('gba', 191, 13),
     ('gbl', 191, 13),
     ('gha', 191, 13),
     ('gma', 191, 13),
     ('grp', 191, 13),
     ('gth', 191, 13),
     ('gwe', 191, 13),
     ('alt', 191, 9),
     ('frw', 189, 9),
     ('gbe', 191, 9),
     ('gos', 191, 9),
     ('gpz', 191, 9),
     ('gtg', 191, 9),
     ('gti', 191, 9),
     ('gzu', 191, 9),
     ('lux', 191, 9),
     ('ydb', 191, 9),
     ('ydl', 191, 9),
     ('ylt', 191, 9),
     ('ydd', 190, 8),
     ('fno', 191, 6),
     ('gvi', 191, 6),
     ('fea', 191, 5),
     ('lge', 191, 5),
     ('swv', 191, 0)]
    ```
    The correlation between #nan features and a genus similarity score is -0.97 in this case.
    
3. Weirdest language
    Same as in the goes for the weirdest language. The result is probably the language with the most missing values (e.g., Bosnian for Slavic)

## Possible improvements
The similarity metric suffers from missing values. One could therefore update the metric so that it takes this into account. The second option would be to try to fill in the missing values.

Another improvement would be to distinguish between purely categorical and scale values.

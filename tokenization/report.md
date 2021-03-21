# TOKENIZATION
## _REPORT_

## Task A
1. Cantonese (yue)

    Most similar languages:
    ```
    ('mnd', 'Chinese', 73),
    ('fin', 'Finnic', 54),
    ('tha', 'Kam-Tai', 54),
    ('vie', 'Viet-Muong', 52),
    ('ind', 'Malayo-Sumbawan', 51)
    ```

    I tried Chinese:
    ```
    Tokenizer words - system: 13901, gold: 13918, precision: 77.04%, recall: 76.95%, f1: 77.00%
    Tokenizer sentences - system: 992, gold: 1004, precision: 74.29%, recall: 73.41%, f1: 73.85%
    ```
    and Chinese simplified:
    ```
    Tokenizer words - system: 15851, gold: 13918, precision: 64.17%, recall: 73.09%, f1: 68.34%
    Tokenizer sentences - system: 962, gold: 1004, precision: 77.23%, recall: 74.00%, f1: 75.58%
    ```
    and Vietnamese:
    ```
    Tokenizer words - system: 3858, gold: 13918, precision: 38.28%, recall: 10.61%, f1: 16.62%
    Tokenizer sentences - system: 1394, gold: 1004, precision: 12.63%, recall: 17.53%, f1: 14.68%
    ```

    We see that the spaces between words are important for Vietnamese tokenizer (Vietnamese can even have spaces in a word itself).

2. Buryat (bxr)

    Most similar languages:
    ```
    ('kha', 'Mongolic', 43),
    ('tur', 'Turkic', 40),
    ('knd', 'Southern Dravidian', 38),
    ('eve', 'Tungusic', 36),
    ('jpn', 'Japanese', 36),
    ('lez', 'Lezgic', 36)
    ```

    I haven't found Mongolic in the UD data, but I tried Turkish. Interestingly, these languages use different writing systems (Cyrillic and Latin), but the approximation is surprisingly good:

    ```
    Tokenizer words - system: 10063, gold: 10032, precision: 96.75%, recall: 97.05%, f1: 96.90%
    Tokenizer sentences - system: 867, gold: 908, precision: 94.93%, recall: 90.64%, f1: 92.73%
    ```

    I also tried Japanese:

    ```
    Tokenizer words - system: 10182, gold: 10032, precision: 97.71%, recall: 99.17%, f1: 98.44%
    Tokenizer sentences - system: 53, gold: 908, precision: 15.09%, recall: 0.88%, f1: 1.66%
    ```
    It is quite surprising how good it can tokenize words considering different languages. 

    and Russian:

    ```
    Tokenizer words - system: 9955, gold: 10032, precision: 97.74%, recall: 96.99%, f1: 97.36%
    Tokenizer sentences - system: 846, gold: 908, precision: 93.38%, recall: 87.00%, f1: 90.08%
    ```
3. Upper Sorbian (hsb)

    ```
    ('hin', 'Indic', 6),
    ('arm', 'Armenian', 5),
    ('cre', 'Algonquian', 5),
    ('cze', 'Slavic', 5),
    ('eve', 'Tungusic', 5)
    ```

    In this case, the Czech seems to perform the best:
    ```
    Tokenizer words - system: 10701, gold: 10736, precision: 99.55%, recall: 99.23%, f1: 99.39%
    Tokenizer sentences - system: 627, gold: 623, precision: 92.66%, recall: 93.26%, f1: 92.96%
    ```

    I also tried Polish (at least for me, the language is very similar to Polish):
    ```
    Tokenizer words - system: 10591, gold: 10736, precision: 99.26%, recall: 97.92%, f1: 98.59%
    Tokenizer sentences - system: 643, gold: 623, precision: 89.27%, recall: 92.13%, f1: 90.68%
    ```

    and finally Serbian:
    ```
    Tokenizer words - system: 10179, gold: 10736, precision: 95.89%, recall: 90.92%, f1: 93.34%
    Tokenizer sentences - system: 547, gold: 623, precision: 82.82%, recall: 72.71%, f1: 77.44%
    ```

## Task B

I decided to train the tokenizer for Upper Sorbian.

There is an extremely low amount of data (12k tokens; e.g., Czech PDT has 1.4M).

I decided to use k-fold cross-validation with k = 5. 

Tokenizer words:
* Mean precision: 99.96 %
* Mean recall: 99.87 % 

Tokenizer sentences:
* Mean precision: 98.21 %
* Mean recall: 97.42 % 

Compared with the Czech model (see Task A), the models trained even on the small training data perform better than the Czech model.

Example of the output:
```
# sent_id = 57
# text = Tute prawa a swobody njesmedza so w žanym padźe w napłećiwku k cilam a zasadam Zjednoćenych narodow wužiwać.
1       Tute    _       _       _       _       _       _       _       _
2       prawa   _       _       _       _       _       _       _       _
3       a       _       _       _       _       _       _       _       _
4       swobody _       _       _       _       _       _       _       _
5       njesmedza       _       _       _       _       _       _       _       _
6       so      _       _       _       _       _       _       _       _
7       w       _       _       _       _       _       _       _       _
8       žanym   _       _       _       _       _       _       _       _
9       padźe   _       _       _       _       _       _       _       _
10      w       _       _       _       _       _       _       _       _
11      napłećiwku      _       _       _       _       _       _       _       _
12      k       _       _       _       _       _       _       _       _
13      cilam   _       _       _       _       _       _       _       _
14      a       _       _       _       _       _       _       _       _
15      zasadam _       _       _       _       _       _       _       _
16      Zjednoćenych    _       _       _       _       _       _       _       _
17      narodow _       _       _       _       _       _       _       _
18      wužiwać _       _       _       _       _       _       _       SpaceAfter=No
19      .       _       _       _       _       _       _       _       SpacesAfter=\n
```
#!/usr/bin/env python3
#coding: utf-8

import sys

# field indexes
ID = 0
FORM = 1
LEMMA = 2
UPOS = 3
XPOS = 4
FEATS = 5
HEAD = 6
DEPREL = 7

rules = [
            ("CC", 'CCONJ'),
            ("NN", 'NOUN'),
            ("JJ", 'INTJ'),
            ("VB", 'VERB'),
            ("X", 'X'),
            ("PR", 'PRON'),
            ("CD", 'NUM'),
            ("DT", 'DET'),
            ("HYPH", 'PUNCT'),
            ("IN", 'ADP'),
            ("MD", 'AUX'),
            ("POS", 'PART'),
            ("RP", 'PART'),
            ("RB", 'ADV'),
            ("UH", 'INTJ'),
            ("AFX", 'ADJ'),
            ("EX", 'ADV'),
            ("FW", 'X'),
        ]

to = int(sys.argv[1])
if to > 0:
    sys.stderr.write(f'{rules[to - 1]}\n')

for line in sys.stdin:
    fields = line.strip().split('\t')
    if len(fields) >= 1 and fields[ID].isdigit():

        for h, r in rules[:to]:
            if fields[XPOS].startswith(h):
                fields[XPOS] = r
        
        # TODO harmonize the tag, store the harmonized tag into UPOS
        fields[UPOS] = fields[XPOS]

        # output
        print('\t'.join(fields))
    else:
        # pass thru
        print(line.strip())



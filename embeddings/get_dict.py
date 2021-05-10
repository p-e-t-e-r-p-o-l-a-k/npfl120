from typing import DefaultDict

lang_a = 'sv'
lang_b = 'en'

a = open(f'../tree_projection/treeproj/PUD/{lang_a}_pud-ud-test.conllu').readlines()
b = open(f'../tree_projection/treeproj/PUD/{lang_b}_pud-ud-test.conllu').readlines()
ali = open(f'../tree_projection/treeproj/align/{lang_a}-{lang_b}/{lang_a}-{lang_b}.intersect').readlines()

def read_sentences(lines):
    sentences = []
    sentence = []
    for line in lines:
        if line[0].isnumeric():
            sentence.append(line.split('\t')[1])
        elif len(line.strip()) == 0:
            sentences.append(sentence)
            sentence = []
    return sentences

a = read_sentences(a)
b = read_sentences(b)

d = DefaultDict(int)

for line, c, e in zip(ali, a, b):
    for a in line.split():
        i, j = a.split('-')
        w = c[int(i)] + ' ' + e[int(j)]
        d[w] = d[w] + 1

for w, c in d.items():
    if c > 2:
        print(w)
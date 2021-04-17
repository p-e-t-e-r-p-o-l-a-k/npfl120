#!/usr/bin/env python3
#coding: utf-8

import sys
from collections import defaultdict
import numpy as np

# parameters
source_filename, target_filename, alignment_filename = sys.argv[1:4]

# number of sentences -- in PUD it is always 1000
SENTENCES = 62491

# field indexes
ID = 0
FORM = 1
LEMMA = 2
UPOS = 3
XPOS = 4
FEATS = 5
HEAD = 6
DEPREL = 7

# returns dict[source_id] = [target_id_1, target_id_2, target_id_3...]
# and a reverse one as well
# TODO depending on what type of alignment you use, you may not need to have a list of aligned tokens -- maybe there is at most one, or even exactly one?
def read_alignment(fh):
    line = fh.readline()
    src2tgt = defaultdict(list)
    tgt2src = defaultdict(list)
    for st in line.split():
        (src, tgt) = st.split('-')
        src = int(src)
        tgt = int(tgt)
        src2tgt[src].append(tgt)
        tgt2src[tgt].append(src)
    return (src2tgt, tgt2src)

# returns a list of tokens, where each token is a list of fields;
# ID and HEAD are covnerted to integers and switched from 1-based to 0-based
# if delete_pos=True, then morphological anotation (UPOS, XPOS, FEATS) is stripped
def read_sentence(fh, delete_pos=False):
    sentence = list()
    for line in fh:
        if line == '\n':
            # end of sentence
            break
        elif line.startswith('#'):
            # ignore comments
            continue
        else:
            fields = line.strip().split('\t')
            if fields[ID].isdigit():
                # make IDs 0-based to match alignment IDs
                fields[ID] = int(fields[ID])-1
                # fields[HEAD] = int(fields[HEAD])-1
                if delete_pos:
                    fields[UPOS] = '_'
                    fields[XPOS] = '_'
                    fields[FEATS] = '_'
                sentence.append(fields)
            # else special token -- continue
    return sentence

# takes list of lists as input, ie as returned by read_sentence()
# switches ID and HEAD back to 1-based and converts them to strings
# joins fields by tabs and tokens by endlines and returns the CONLL string
def write_sentence(sentence):
    result = list()
    for fields in sentence:
        # switch back to 1-based IDs
        fields[ID] = str(fields[ID]+1)
        # fields[HEAD] = str(fields[HEAD]+1)
        result.append('\t'.join(fields))
    result.append('')
    return '\n'.join(result)

upos2id = dict()
i = 0
with open(source_filename) as source:
    for sentence_id in range(SENTENCES):
        source_sentence = read_sentence(source)
        for token in source_sentence:
            if not token[UPOS] in upos2id.keys():
                upos2id[token[UPOS]] = i
                i += 1

id2upos = dict({(v,k) for k,v in upos2id.items()})

probs = dict()
def add_prob(w, tag):
    if not w in probs.keys():
        probs[w] = np.zeros(len(upos2id))
    probs[w][upos2id[tag]] += 1

with open(source_filename) as source, open(target_filename) as target, open(alignment_filename) as alignment:
    for sentence_id in range(SENTENCES):
        (src2tgt, tgt2src) = read_alignment(alignment)
        source_sentence = read_sentence(source)
        target_sentence = read_sentence(target, delete_pos=True)
        for target_token in target_sentence:
            target_token_id = target_token[ID]

            #target_sentence[target_token_id][UPOS] = 'NOUN'

            # for each target token aligned to source_token (if any)
            for source_token_id in tgt2src[target_token_id]:
                # pass
                # TODO copy source UPOS to target UPOS?
                add_prob(target_sentence[target_token_id][FORM], source_sentence[source_token_id][UPOS])

with open(source_filename) as source, open(target_filename) as target, open(alignment_filename) as alignment:
    for sentence_id in range(SENTENCES):
        (src2tgt, tgt2src) = read_alignment(alignment)
        source_sentence = read_sentence(source)
        target_sentence = read_sentence(target, delete_pos=True)
        
        # TODO do the projection
        # iterate over source tokens
        # TODO maybe you want to iterate over target tokens?
        '''for source_token in source_sentence:
            source_token_id = source_token[ID]
            # for each target token aligned to source_token (if any)
            for target_token_id in src2tgt[source_token_id]:
                # pass
                # TODO copy source UPOS to target UPOS?
                target_sentence[target_token_id][UPOS] = source_sentence[source_token_id][UPOS]'''
        for target_token in target_sentence:
            target_token_id = target_token[ID]

            #target_sentence[target_token_id][UPOS] = 'NOUN'

            # for each target token aligned to source_token (if any)
            target_sentence[target_token_id][UPOS] = 'NOUN'
            if target_sentence[target_token_id][FORM] in probs.keys():
                p = probs[target_sentence[target_token_id][FORM]]
                upos = np.argmax(p)
                upos = id2upos[upos]
                target_sentence[target_token_id][UPOS] = upos
            else:
                for source_token_id in tgt2src[target_token_id]:
                    # pass
                    # TODO copy source UPOS to target UPOS?
                    target_sentence[target_token_id][UPOS] = source_sentence[source_token_id][UPOS]
    
        print(write_sentence(target_sentence))


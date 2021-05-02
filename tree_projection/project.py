#!/usr/bin/env python3
#coding: utf-8

import sys
from collections import defaultdict

# parameters
source_filename, target_filename, alignment_filename = sys.argv[1:4]

# number of sentences -- in PUD it is always 1000
SENTENCES = 1000

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
# if delete_tree=True, then syntactic anotation (HEAD and DEPREL) is stripped
def read_sentence(fh, delete_tree=False):
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
                fields[HEAD] = int(fields[HEAD])-1
                if delete_tree:
                    # reasonable defaults:
                    fields[HEAD] = -1       # head = root
                    fields[DEPREL] = 'dep'  # generic deprel
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
        fields[HEAD] = str(fields[HEAD]+1)
        result.append('\t'.join(fields))
    result.append('')
    return '\n'.join(result)

def is_cycle(target_head_id, target_token_id, target_sentence):
    curr = target_head_id
    while curr != -1:
        if curr == target_token_id:
            return True
        curr = target_sentence[curr][HEAD]
    return False

with open(source_filename) as source, open(target_filename) as target, open(alignment_filename) as alignment:
    for sentence_id in range(SENTENCES):
        (src2tgt, tgt2src) = read_alignment(alignment)
        source_sentence = read_sentence(source)
        target_sentence = read_sentence(target, delete_tree=True)
        
        # TODO do the projection
        # iterate over source tokens
        # TODO maybe you want to iterate over target tokens?
        root = -1
        for source_token in source_sentence:
            if  source_token[HEAD] == -1:
                root = source_token
                break
        queue = [root,]
        root_id = -1
        for source_token in queue:
            source_token_id = source_token[ID]
            # for each target token aligned to source_token (if any)
            for target_token_id in src2tgt[source_token_id]:

                # deprel
                target_sentence[target_token_id][DEPREL] = source_token[DEPREL]
                if source_token[DEPREL] == 'root':
                    root_id = target_token_id

                # head
                source_head_id = source_token[HEAD]
                potential_heads = src2tgt[source_head_id]
                for target_head_id in potential_heads:
                    if not is_cycle(target_head_id, target_token_id, target_sentence):
                        target_sentence[target_token_id][HEAD] = target_head_id
                        break
                    
            for token in source_sentence:
                if token[HEAD] == source_token_id:
                    queue.append(token)

                # TODO copy source deprel to target deprel?
                # target_sentence[target_token_id][DEPREL] = ...
                # TODO set target head to something
                # source_token_head = source_token[HEAD]
                # ...
                # TODO these are IDs of all tokens aligned to the source_token_head
                # (depending on the alignment type, the list may be empty, have 1 member, or multiple members)
                # potential_heads = src2tgt[source_token_head]
                # ...
                # TODO you should also make sure not to produce cycles
        if root_id == -1:
            for token in target_sentence:
                if token[HEAD] == -1:
                    root_id = token[ID]
                    break

        for token in target_sentence:
            if token[HEAD] == -1 and token[ID] != root_id:
                token[HEAD] = root_id
        print(write_sentence(target_sentence))


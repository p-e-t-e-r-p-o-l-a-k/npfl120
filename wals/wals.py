import pandas as pd
import numpy as np
import argparse


FIRST_FEATURE = '1A Consonant Inventories'
data = pd.read_csv('language.tsv', sep='\t', header=0, index_col=0)


def similatiry(lang, lang2):
    d = data.loc[lang, FIRST_FEATURE:]
    d2 = data.loc[lang2, FIRST_FEATURE:]
    sim =  d.fillna(0).values == d2.fillna(0).values
    #sim =  1 - np.abs(d.fillna(0).values - d2.fillna(0).values) / max_vals
    relevant = (1 - d.isna().to_numpy()) * (1 - d2.isna().to_numpy())
    score = np.sum(relevant * sim)
    return score

def similar_langs(lang, data):
    langs = [(l, similatiry(lang, l)) for l in data.index]
    return sorted(langs, key=lambda x: x[1], reverse=True)[1:]

def centroid(genus):
    d = data.loc[data['genus'] == genus]
    l = [sum(map(lambda x: x[1], similar_langs(lang, d))) for lang in d.index]
    l = np.argmax(l)
    return d.loc[d.index[l], 'Name']

def weidest(genus):
    d = data.loc[data['genus'] == genus]
    l = [sum(map(lambda x: x[1], similar_langs(lang, d))) for lang in d.index]
    l = np.argmin(l)
    return d.loc[d.index[l], 'Name']

def main(args):
    if args.task == 'similar_langs':
        d = pd.DataFrame(data=similar_langs(args.lang, data),columns=['lang', 'score'])
        d = d.loc[d['score'] > 0]
        print(d.to_string())
    elif args.task == 'centroid':
        print(centroid(args.genus))
    elif args.task == 'weidest':
        print(weidest(args.genus))
    else:
        print('Undefined task')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', required=True)
    parser.add_argument('--lang')
    parser.add_argument('--genus')

    main(parser.parse_args())

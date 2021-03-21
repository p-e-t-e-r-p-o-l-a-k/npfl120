import argparse
import random

def main(args):
    sentences = []
    with open(args.data) as input:
        sentence = []
        for line in input.readlines():
            sentence.append(line)
            if line.strip() == '':
                sentences.append(sentence)
                sentence = []
        if len(sentence) > 0:
            sentences.append(sentence)


    random.shuffle(sentences)

    l = len(sentences) // args.folds
    for i in range(args.folds):
        with open(f'train{i}', 'w') as o:
            for d in sentences[0:i*l] + sentences[(i+1)*l:]:
                for line in d:
                    o.write(line)
        with open(f'test{i}', 'w') as o:
            for d in sentences[i:i+l]:
                for line in d:
                    o.write(line)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--folds', type=int, required=True)
    parser.add_argument('--data', required=True)

    main(parser.parse_args())
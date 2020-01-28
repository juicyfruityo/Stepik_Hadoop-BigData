import sys


for line in sys.stdin:
    word, doc, count = line.strip().split('\t')
    print(word + '\t' + doc + ';' + count + ';' + '1')

import sys
import re


for line in sys.stdin:
    doc, sentence = line.strip().split(':', 1)
    for word in re.compile('\w+').findall(sentence):
        print(word + '#' + doc + '\t' + '1')

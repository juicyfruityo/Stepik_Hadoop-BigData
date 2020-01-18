import sys


for line in sys.stdin:
    num, chars = line.strip().split('\t')
    for ch in chars.split(','):
        print(num + ',' + ch + '\t' + '1')

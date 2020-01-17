import sys


for line in sys.stdin:
    num, ch = line.strip().split(',')
    print(ch + '\t' + '1')

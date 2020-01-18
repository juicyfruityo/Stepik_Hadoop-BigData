import sys


for line in sys.stdin:
    elems = list(line.strip().split('\t'))
    print(elems[2])

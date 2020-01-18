import sys


prev = ""
for line in sys.stdin:
    elem, s = line.strip().split('\t')
    if elem == prev:
        print(elem)
    else:
        prev = elem

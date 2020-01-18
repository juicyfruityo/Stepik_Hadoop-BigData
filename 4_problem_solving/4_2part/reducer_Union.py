import sys

elems = set()
for line in sys.stdin:
    elem, s = line.strip().split('\t')
    if elem not in elems:
        elems.add(elem)
        print(elem)

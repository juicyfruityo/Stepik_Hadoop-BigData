import sys


elements = set()
for line in sys.stdin:
    elem, _ = line.strip().split('\t')
    num, ch = elem.split(',')
    if (num, ch) in elements:
        continue
    elements.add((num, ch))
    print(num + ',' + ch)

import sys


for line in sys.stdin:
    elems = list(line.strip().split(' '))
    for i in elems:
        for j in elems:
            if i == j:
                continue
            print(i + ',' + j + '\t' + '1')

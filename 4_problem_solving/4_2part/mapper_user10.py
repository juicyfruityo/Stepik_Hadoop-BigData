import sys


for line in sys.stdin:
    elems = list(line.strip().split('\t'))
    if elems[1] == 'user10':
        print(line.strip())

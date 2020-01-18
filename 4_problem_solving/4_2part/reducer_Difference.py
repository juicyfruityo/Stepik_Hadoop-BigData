import sys


result = []
for line in sys.stdin:
    elem, s = line.strip().split('\t')
    if s == 'A':
        result.append(elem)
    else:
        if len(result) != 0 and result[-1] == elem:
            result.pop(-1)

for i in result:
    print(i)

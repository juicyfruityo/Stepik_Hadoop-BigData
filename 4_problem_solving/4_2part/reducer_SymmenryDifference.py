import sys


resultA = []
resultB = []
for line in sys.stdin:
    elem, s = line.strip().split('\t')
    if s == 'A':
        resultA.append(elem)
    else:
        if len(resultA) > 0:
            if resultA[-1] != elem:
                resultB.append(elem)
            else:
                resultA.pop(-1)
        else:
            resultB.append(elem)

for i in sortde(resultA + resultB):
    print(i)

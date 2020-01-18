import sys


for line in sys.stdin:
    elems = list(line.strip().split(' '))
    for i in elems:
        H = dict()
        for j in elems:
            if j == i:
                continue
            if H.get(j) is None:
                H[j] = 1
            else:
                H[j] += 1
        print(i + '\t' + ','.join([j+':'+str(H[j]) for j in H.keys()]))

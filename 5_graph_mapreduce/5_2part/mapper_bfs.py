import sys
import re

for line in sys.stdin:
    v, d, adj = re.split('\t', line.strip())
    if d == 'INF':
        new_d = 'INF'
    else:
        new_d = int(d) + 1
    print(line.strip())
    adjVert = re.findall('\d+', adj)
    for adjV in adjVert:
        print(adjV + '\t' + str(new_d) + '\t' + '{}')

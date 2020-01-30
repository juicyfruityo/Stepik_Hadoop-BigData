import sys
import re

for line in sys.stdin:
    n, p, struct = re.compile('\t').split(line.strip())
    print(line.strip())

    vertices = re.compile('\d+').findall(struct)
    m = round(float(p) / len(vertices), 3)
    for v in vertices:
        print(v + '\t' + f"{m:.3f}" + '\t' + '{}')

import sys

count = dict()
n = dict()
for line in sys.stdin:
    site, time = line.strip().split('\t')
    if count.get(site) is None:
        count[site] = int(time)
        n[site] = 1
    else:
        count[site] += int(time)
        n[site] += 1
for site in count.keys():
    print(site + '\t' + str(int(count[site] / float(n[site]))))

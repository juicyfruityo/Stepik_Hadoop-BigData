import sys

times = dict()
count = dict()
for line in sys.stdin:
    site, param = line.strip().split('\t')
    time, _ = param.split(';')
    if times.get(site) is None:
        times[site] = int(time)
        count[site] = 1
    else:
        times[site] += int(time)
        count[site] += 1
for site in times.keys():
    print(site + '\t' + str(times[site]) + ';' + str(count[site]))

import sys


check = set()
counts = dict()
for line in sys.stdin:
    num, ch = line.strip().split()
    if counts.get(ch) is None:
        check.add((num, ch))
        counts[ch] = 1
    else:
        if (num, ch) not in check:
            counts[ch] += 1
for ch in counts.keys():
    print(ch + '\t' + str(counts[ch]))

import sys

counts = dict()

for line in sys.stdin:
    words = line.strip().split(' ')
    for word in words:
        if counts.get(word) is None:
            counts[word] = 1
        else:
            counts[word] += 1
for word in counts.keys():
    print(word + '\t' + str(counts[word]))

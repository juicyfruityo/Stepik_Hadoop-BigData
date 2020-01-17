import sys

for line in sys.stdin:
    local = dict()
    words = line.strip().split(' ')
    for word in words:
        if local.get(word) is None:
            local[word] = 1
        else:
            local[word] += 1
    for word in local.keys():
        print(word + '\t' + str(local[word]))

import sys

prev_key = None
count = 0
for line in sys.stdin:
    key, _ = line.strip().split('\t')
    if prev_key and prev_key != key:
        res = prev_key.split('#')
        print(res[0] + '\t' + res[1] + '\t' + str(count))

        prev_key = key
        count = 1
    elif prev_key is None:
        prev_key = key
        count = 1
    else:
        count += 1

res = prev_key.split('#')
print(res[0] + '\t' + res[1] + '\t' + str(count))

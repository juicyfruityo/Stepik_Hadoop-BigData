import sys


prev_word = None
info_arr = []
n = 0
for line in sys.stdin:
    word, value = line.strip().split('\t')
    info = value.split(';')
    if prev_word is None:
        prev_word = word
        info_arr.append(info)
        n = 1
    elif prev_word == word:
        info_arr.append(info)
        n += 1
    else:
        for v in info_arr:
            print(prev_word + '#' + v[0] + '\t' + v[1] + '\t' + str(n))
        info_arr.clear()
        prev_word = word
        info_arr.append(info)
        n = 1

for v in info_arr:
    print(prev_word + '#' + v[0] + '\t' + v[1] + '\t' + str(n))

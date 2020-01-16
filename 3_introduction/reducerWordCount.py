# Напишите программу, которая реализует
# reducer для задачи WordCount в Hadoop Streaming.

import sys

prev_key, prev_num = (None, 0)
for line in sys.stdin:
    key, num = line.strip().split('\t')
    if prev_key and key != prev_key:
        print(prev_key + '\t' + str(prev_num))
        prev_key, prev_num = key, int(num)
    else:
        prev_key = key
        prev_num += int(num)

if prev_key:
    print(prev_key + '\t' + str(prev_num))

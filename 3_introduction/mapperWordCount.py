# Напишите программу, которая реализует
# mapper для задачи WordCount в Hadoop Streaming.
# Вызов: cat input.txt | python mapperWordCount.py
#        | sort | python reducerWordCount.py 


import sys

for line in sys.stdin:
    elems = line.strip().split(' ')
    for elem in elems:
        print(elem + '\t1')

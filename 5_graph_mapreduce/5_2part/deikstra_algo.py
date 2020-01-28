from collections import namedtuple
from pprint import pprint


vert_num, edg_num = map(int, input().strip().split(' '))
edge = namedtuple('edge', ['end', 'weight'])
graph = {}
all_ver = set()

for i in range(edg_num):
    start, end, weight = map(int, input().strip().split(' '))
    graph.setdefault(start, []).append(edge(end, weight))
    all_ver.add(start)
    all_ver.add(end)
start, end = map(int, input().strip().split(' '))

dist = {}
for key in all_ver:
    dist[key] = float('inf')
dist[start] = 0
Q = set([key for key in graph.keys()])

while len(Q) > 0:
    u = min(Q, key=lambda x: dist[x])
    Q.remove(u)
    for e in graph[u]:
        if dist[e.end] > dist[u] + e.weight:
            dist[e.end] = dist[u] + e.weight

if dist.get(end) is None or dist[end] == float('inf'):
    print(-1)
else:
    print(dist[end])

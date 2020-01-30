import sys
import re


N = 5.0
alpha = 0.1

prev_node = None
node_struct = None
default_struct = '{}'
pagerank = 0
default_pr = 0
for line in sys.stdin:
    node, prob, struct = re.compile('[\t+\s+]').split(line.strip())
    vertices = re.compile('\d+').findall(struct)

    if prev_node == node:
        if len(vertices) != 0:
            node_struct = struct
        else:
            pagerank += float(prob)
    else:
        if prev_node is not None:
            pagerank = alpha / N + (1 - alpha) * pagerank
            if node_struct is None:
                node_struct = default_struct
            print(prev_node + '\t' + f'{pagerank:.3f}' + '\t' + node_struct)
        prev_node = node
        node_struct = None
        pagerank = 0
        if len(vertices) != 0:
            node_struct = struct
        else:
            pagerank += float(prob)

pagerank = alpha / N + (1 - alpha) * pagerank
if node_struct is None:
    node_struct = default_struct
print(prev_node + '\t' + f'{pagerank:.3f}' + '\t' + node_struct)

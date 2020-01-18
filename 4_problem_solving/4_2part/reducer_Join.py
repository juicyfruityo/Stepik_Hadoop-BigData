import sys


urls = {}
queries = {}
for line in sys.stdin:
    user, elem = line.strip().split('\t')
    t, name = elem.split(':')
    if t == 'url':
        if urls.get(user) is None:
            urls[user] = [name]
        else:
            urls[user].append(name)
    else:
        if queries.get(user) is None:
            queries[user] = [name]
        else:
            queries[user].append(name)

for user in urls.keys():
    if queries.get(user) is None:
        continue
    for i in queries[user]:
        for j in urls[user]:
            print(user + '\t' + i + '\t' + j)

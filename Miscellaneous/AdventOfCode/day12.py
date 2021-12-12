
with open('c:/Users/mdoskarin001/Desktop/git/Algorithms/Miscellaneous/AdventOfCode/day12.txt') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
from collections import defaultdict, deque
d = defaultdict(set)
capital = set()
noncapital = set()
for line in lines:
    u, v = line.split("-")
    if u.islower() and u not in ['start', 'end']:
        noncapital.add(u)
    if u.isupper():
        capital.add(u)
    if v.islower() and v not in ['start', 'end']:
        noncapital.add(v)
    if v.isupper():
        capital.add(v)

    d[u].add(v)
    d[v].add(u)
paths = set()
q = deque([('start', 'start', 1)])

while q:
    cur, visited, balance = q.popleft()

    if cur == 'end':
        paths.add(visited)

    for nei in d[cur]:
        if nei == 'end' and nei in visited:
            continue
        if nei == 'start':
            continue

        if nei in visited and nei in noncapital and balance == 0 :
            continue
        if nei in visited and nei in noncapital:
            q.append((nei, visited + "->" + nei, balance - 1))
        else:
            q.append((nei, visited + "->" + nei, balance))
            
print(len(paths), paths)





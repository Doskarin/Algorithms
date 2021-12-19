'''
You have an array of integers (initially empty).

You have to perform q queries. Each query is of one of two types:

"1 x" — add the element x to the end of the array;
"2 x y" — replace all occurrences of x in the array with y.
Find the resulting array after performing all the queries.

Input
The first line contains a single integer q (1≤q≤5⋅105) — the number of queries.

Next q lines contain queries (one per line). Each query is of one of two types:

"1 x" (1≤x≤5⋅105);
"2 x y" (1≤x,y≤5⋅105).
It's guaranteed that there is at least one query of the first type.

Output
In a single line, print k integers — the resulting array after performing all the queries, where k is the number of queries of the first type.

Examples
inputCopy
7
1 3
1 1
2 1 2
1 2
1 1
1 2
2 1 3
outputCopy
3 2 2 3 2 
inputCopy
4
1 1
1 2
1 1
2 2 2
outputCopy
1 2 1 
inputCopy
8
2 1 4
1 1
1 4
1 2
2 2 4
2 4 3
1 2
2 2 7
outputCopy
1 3 3 7 
Note
In the first example, the array changes as follows:

[] → [3] → [3,1] → [3,2] → [3,2,2] → [3,2,2,1] → [3,2,2,1,2] → [3,2,2,3,2].

In the second example, the array changes as follows:

[] → [1] → [1,2] → [1,2,1] → [1,2,1].

In the third example, the array changes as follows:

[] → [] → [1] → [1,4] → [1,4,2] → [1,4,4] → [1,3,3] → [1,3,3,2] → [1,3,3,7].

'''
from collections import defaultdict

d = defaultdict(list)
k = 0
for i in range(int(input())):
    a = list(map(int, input().split()))
    if a[0] == 1:
        d[a[1]].append(k)
        k += 1
    elif a[1] != a[2]:
        d[a[2]].extend(d[a[1]])
        del d[a[1]]
r = [0] * k
for i in d:
    for k in d[i]:
        r[k] = str(i)
print(' '.join(r))



    



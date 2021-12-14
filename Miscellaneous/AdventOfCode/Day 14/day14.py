with open('day14.txt') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
polymer = lines[0]
rules = lines[2:]

from collections import defaultdict, Counter
d = defaultdict(str)
for rule in rules:
    u = rule.split(" -> ")[0]
    v = rule.split(" -> ")[1]
    d[u] = v

p1 = defaultdict(int)
for i in range(len(polymer) - 1):
    p1[polymer[i] + polymer[i + 1]] += 1

for j in range(40):
    p2 = defaultdict(int)
    
    for s in p1:
        p2[s[0] + d[s]] += p1[s]
        p2[d[s] + s[1]] += p1[s]

    p1 = p2

count = defaultdict(int)

for key in p1:
    count[key[0]] += p1[key]

count[polymer[-1]] += 1
print(max(count.values()) - min(count.values()))
    


'''
Template:     NNCB
After step 1: NCNBCHB
              NCNBCHB
After step 2: NBCCNBBBCBHCB
              NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
              NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
              NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C

'''
n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

def canCut(length):
    total = 0
    for rope in arr:
        total += rope//length
    
    return total >= k

left, right = 0, 10**8

for _ in range(100):
    mid = left + (right - left) / 2

    if canCut(mid):
        left = mid
    else:
        right = mid

print(left)
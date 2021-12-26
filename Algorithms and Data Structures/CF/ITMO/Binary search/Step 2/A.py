w, h, n = map(int, input().split())
import math
def canFit(x):
    return (x//w) * (x//h) >= n

left, right = min(w, h), max(w, h) * n

while right - left > 1:
    mid = left + (right - left) // 2

    if canFit(mid):
        right = mid
    else:
        left = mid
print(right)
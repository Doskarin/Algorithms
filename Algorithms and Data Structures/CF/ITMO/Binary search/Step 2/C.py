n, x, y = map(int, input().split())

def canPrint(seconds):
    return (seconds//min(x, y) + (seconds - min(x, y))//max(x, y)) >= n



left, right = 0, 10**10

while right - left > 1:

    mid = (right + left) // 2

    if canPrint(mid):
        right = mid
    else:
        left = mid
print(right)


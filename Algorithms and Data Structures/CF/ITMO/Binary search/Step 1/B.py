n, k = map(int, input().split())
arr = [float('-inf')] + list(map(int, input().split())) + [float('inf')]
queries = list(map(int, input().split()))

def find_lower(arr, x):
    left, right = 0, len(arr)

    while right - left > 1:
        mid = left + (right - left) // 2

        if arr[mid] <= x:
            left = mid
        else:
            right = mid

    return left


for q in queries:

    x = find_lower(arr, q)

    if x == 0:
        print(0)
    else:
        print(x)
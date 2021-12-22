n, k = map(int, input().split())

arr = [float('-inf')] + list(map(int, input().split())) + [float('inf')]

queries = list(map(int, input().split()))


def find_upper(arr, x):
    left, right = 0, len(arr)
    while right - left > 1:
        mid = left + (right - left) // 2

        if arr[mid] < x:
            left = mid
        else:
            right = mid
    return right


for q in queries:

    index = find_upper(arr, q)

    if index == len(arr):
        print(n + 1)
    else:
        print(index)
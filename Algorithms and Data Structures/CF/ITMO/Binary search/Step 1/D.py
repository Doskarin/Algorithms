n = int(input())
arr = list(map(int, input().split()))
k = int(input())
arr.sort()
def find_lower(arr, x):
    
    left, right = -1, len(arr)
    while right - left > 1:
        mid = left + (right - left) // 2

        if arr[mid] <= x:
            left = mid
        else:
            right = mid
        
    return left
def find_upper(arr, x):
    
    left, right = -1, len(arr)
    while right - left > 1:
        mid = left + (right - left) // 2
        if arr[mid] < x:
            left = mid
        else:
            right = mid
    return right



for _ in range(k):
    l, r = map(int, input().split())
    left_boundary = find_upper(arr, l)
    right_boundary = find_lower(arr, r)
    #print(left_boundary, right_boundary)
    if left_boundary > right_boundary:
        print(0)
    else:
        print(right_boundary - left_boundary + 1)
    
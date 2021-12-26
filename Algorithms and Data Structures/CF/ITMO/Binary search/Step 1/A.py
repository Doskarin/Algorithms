n, k = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

def find(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == x:
            return True

        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

for x in queries:
    if find(arr, x):
        print("YES")
    else:
        print("NO")
    

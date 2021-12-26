t = int(input())

while t:

    n = int(input())

    arr = list(map(int, input().split()))

    total = sum(arr)
    
    if total % n == 0:
        print(0)

    else:
        print(1)

    t -= 1

    
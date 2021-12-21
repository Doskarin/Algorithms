
def find(num):
    threshold = 10**9
    num = 1
    powersOfTwo = set()
    powersOfThree = set()

    while num < threshold:
        powersOfTwo.add(num)
        num *= 2
    return powersOfTwo
a = []
i, j = 1, 1
two = 1
three = 1
threshold = 10**10
res = []
while three ** 3 <= threshold and two ** 2 <= threshold:
    powerOfTwo = two**2
    powerOfThree = three**3
    if powerOfTwo > powerOfThree:

        res.append(powerOfThree)
        three += 1
    elif powerOfTwo < powerOfThree:
        res.append(powerOfTwo)
        two += 1
    else:
        res.append(powerOfThree)
        two += 1
        three += 1

t = int(input())
from bisect import bisect, bisect_left, bisect_right
for _ in range(t):
    num = int(input())
    print(bisect_right(res, num))








# def countPrimes(n):
#         if n <= 1:
#             return 0
#         primes = [1] * n
#         primes[0], primes[1] = 0, 0
        
#         for i in range(2, 4):
#             if primes[i] == 1:
#                 for j in range(2*i, n, i):
#                     primes[j] = 0
#         nums = set()
#         for num, status in enumerate(primes[1:]):
#             if status:
#                 nums.add(num)
#         return nums


import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n == 0:
        return 0

    return n + f(n - 1)


print(f(int(input())))
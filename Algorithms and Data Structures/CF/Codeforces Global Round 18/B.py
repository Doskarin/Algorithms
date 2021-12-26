def checkTwo(p, num1, num2):
    if num1 > num2:
        return 0
    cur = num2 % 2**(p + 1)
    if num1 // (2**p) == num2 // (2**p):
        if 2**p > cur:
            return 0
        else:
            return num2 - num1 + 1
    else:
        if 2**p <= cur:
            return num2 + 1 - (2**p  + find_low(num2, p + 1))
        else:
            return find_high(num1, p + 1) + (-num1)

def checkOne(num1, num2):
    return (num2 - num1 + 1) // 2

def find_high(num1, p):
    t = num1
    return (t // 2**(p) + 1)*2**(p)

def find_low(num1, p):
    t = num1
    return (t // 2**(p))*2**(p) 

def checkThree(p, num1, num2):
    return checkTwo(p, num1, find_high(num1, p + 1) - 1) + checkTwo(p,find_low(num2, p + 1), num2) + checkOne(find_high(num1, p + 1), find_low(num2, p + 1) - 1)

def check(p, num1, num2):
    cur = 2**(p + 1)
    factor = 2**(p + 1)
    if num1 % cur == 0 and num2 % cur == factor - 1:
        return checkOne(num1, num2)
    if num1 // cur == num2 // factor:
        return checkTwo(p, num1, num2)
    else:
        return checkThree(p, num1, num2)
t = int(input())
while t:

    l, r = map(int, input().split())

    total = r - l + 1
    max_len = len(bin(r)) - 2
    min_count = float('inf')
    for set_bit in range(max_len+1):
        cur = check(set_bit, l, r)
        min_count = min(min_count, total - cur)
    print(min_count)

    t -= 1



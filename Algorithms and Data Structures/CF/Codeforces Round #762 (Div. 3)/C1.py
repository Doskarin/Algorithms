t = int(input())

while t:
    zero = 0
    overflow = 18
    first, sSum = input().split()
    while first and first[zero] == '0':
        first = first[1:]

    while sSum and sSum[zero] == '0':
        sSum = sSum[1:]
    ss = len(sSum) - 1
    ff = len(first) - 1
    
    
    if len(sSum) < len(first) or sSum == first:
        print(-1)
        continue
    res = ''
    go = False
    while ff > -1:
        if ss < ff:
            print(-1)
            go = True
            break
        if sSum[ss] < first[ff]:
            
            if ss <= 0 or sSum[ss - 1] == '0' or int(sSum[ss - 1:ss + 1]) > overflow:
                print(-1)
                go = True
                break
            cand = int(sSum[ss - 1:ss + 1])
            res = str(cand - int(first[ff])) + res
            ss -= 2
            ff -= 1
            
        else:
            res = str(int(sSum[ss]) - int(first[ff])) + res
            ss -= 1
            ff -= 1
            
    if go:
        continue

    if ss > -1:
        res = sSum[:ss + 1] + res
    if not go:
        while len(res) > 1 and res[zero] == '0':
            res = res[1:]
        print(res)
    t -= 1



# t = int(input())

# while t:

#     zero = 0
#     overflow = 18
#     first, sSum = input().split()

#     while sSum and sSum[zero] == '0':
#         sSum = sSum[1:]
    
#     while first and first[zero] == '0':
#         first = first[1:]

    
    
#     p1 = len(sSum) - 1
#     p2 = len(first) - 1
    
#     #edge case
#     if len(sSum) < len(first) or sSum == first:
#         print(-1)
#         continue
#     res = ''
#     bad = True
#     good = True
#     while p2 > -1:
#         if good:
#             if p1 < p2:
#                 print(-1)
#                 bad = False
#                 break

#             if sSum[p1] < first[p2]:
#                 cand = int(sSum[p1 - 1:p1 + 1])
#                 if p1 <= 0 or sSum[p1 - 1] == '0' or cand > overflow:
#                     print(-1)
#                     bad = False
#                     break
#                 res = str(cand - int(first[p2])) + res
                
#                 p1 -= 2
#                 p2 -= 1
#             else:
#                 sum_num = int(sSum[p1])
#                 first_num = int(first[p2])
#                 res = str(sum_num - first_num) + res
#                 p1 -= 1
#                 p2 -= 1
                
#     if not bad:
#         continue

#     if p1 > -1:
#         res = sSum[:p1 + 1] + res

#     if bad:
#         while len(res) > 1 and res[0] == '0':
#             res = res[1:]

#     print(res)
#     t -= 1











# for _ in range(int(input())):
#     a, c = input().split()
#     while a and a[0] == '0':
#         a = a[1:]
#     while c and c[0] == '0':
#         c = c[1:]
#     i, j = len(c) - 1, len(a) - 1
#     t = 0
#     if len(c) < len(a) or c == a:
#         print(-1)
#         continue
#     s = ''
#     br = False
#     while j > -1:
#         if i < j:
#             print(-1)
#             br = True
#             break
#         if c[i] < a[j]:
#             if i <= 0 or c[i - 1] == '0' or int(c[i - 1:i + 1]) > 18:
#                 print(-1)
#                 br = True
#                 break
#             s = str(int(c[i - 1:i + 1]) - int(a[j])) + s
#             i, j = i - 2, j - 1
#         else:
#             s = str(int(c[i]) - int(a[j])) + s
#             i, j = i - 1, j - 1
#     if br:
#         continue
#     if i > -1:
#         s = c[:i + 1] + s
#     while len(s) > 1 and s[0] == '0':
#         s = s[1:]
#     print(s)
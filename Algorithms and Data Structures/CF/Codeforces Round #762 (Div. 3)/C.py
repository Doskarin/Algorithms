t = int(input())

for _ in range(t):
    a, s = map(str, input().split())
    if len(s) < len(a):
        print(-1)
        continue

    i = len(a) - 1
    j = len(s) - 1
    res = ""
    while i >= 0:
        num_a = int(a[i])
        num_s = int(s[j])

        if num_a > num_s:
            if j - 1 < 0:
                print(-1)
                continue
            num_b = int(s[j - 1:j + 1]) - num_a
            res = str(num_b) + res
            j -= 2
            i -= 1
        elif num_a == num_s:
            res = "0" + res
            i -= 1
            j -= 1
        else:
            num_b = num_s - num_a
            res = str(num_b) + res
            i -= 1
            j -= 1
    if j > -2:
        print(-1)
        continue
    p1 = 0
    while res[p1] == "0":
        p1 += 1

    print(res[p1:])
        
            



# for _ in range(t):
#     a, s = map(str, input().split())

#     p_a = 0
#     p_s = 0
#     res = []
#     while p_a < len(a):
#         for i in range(1, 10):
#             cur_num = int(a[p_a]) + i
#             if s.startswith(str(cur_num)):
#                 s = s.replace(str(cur_num),"",1)
#                 res.append(str(int(s[p_s]) - cur_num))
#                 break
#         p_a += 1
#     print(res)
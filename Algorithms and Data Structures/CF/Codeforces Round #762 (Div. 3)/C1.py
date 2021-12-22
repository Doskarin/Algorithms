t = in
for _ in range(int(input())):
    a, c = input().split()
    while a and a[0] == '0':
        a = a[1:]
    while c and c[0] == '0':
        c = c[1:]
    i, j = len(c) - 1, len(a) - 1
    t = 0
    if len(c) < len(a) or c == a:
        print(-1)
        continue
    s = ''
    br = False
    while j > -1:
        if i < j:
            print(-1)
            br = True
            break
        if c[i] < a[j]:
            if i <= 0 or c[i - 1] == '0' or int(c[i - 1:i + 1]) > 18:
                print(-1)
                br = True
                break
            s = str(int(c[i - 1:i + 1]) - int(a[j])) + s
            i, j = i - 2, j - 1
        else:
            s = str(int(c[i]) - int(a[j])) + s
            i, j = i - 1, j - 1
    if br:
        continue
    if i > -1:
        s = c[:i + 1] + s
    while len(s) > 1 and s[0] == '0':
        s = s[1:]
    print(s)
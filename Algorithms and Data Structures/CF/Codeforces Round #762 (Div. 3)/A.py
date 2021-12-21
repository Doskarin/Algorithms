t = int(input())

for _ in range(t):
    string = input()
    if len(string) % 2 == 1:
        print("NO")

    elif string[:len(string)//2] == string[len(string)//2:]:
        print("YES")
    else:
        print("NO")
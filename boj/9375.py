from sys import stdin
T = int(input())
for _ in range(T):
    n = int(input())
    lst = {}
    ans = 1
    for i in range(n):
        name, part = input().split()
        if lst.__contains__(part):
            lst[part] += 1
        else:
            lst[part] = 1
    for p in lst:
        ans *= lst[p] + 1
    ans -= 1
    print(ans)

# in | __contains__
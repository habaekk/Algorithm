N = int(input())

lst = [[0] * 2 for i in range(N)]
dlst = []
cnt = 0

for i in range(N):
    x, y = map(int, input().split())
    lst[i][0] = x
    lst[i][1] = y

for i in range(N):
    cnt = 0
    x, y = lst[i][0], lst[i][1]
    for j in range(N):
        if i == j:
            continue
        else:
            if x < lst[j][0] and y < lst[j][1]:
                cnt += 1
    dlst.append(cnt + 1)

for i in range(len(dlst)):
    if i != len(dlst) - 1:
        print(dlst[i], end = " ")
    else:
        print(dlst[i])
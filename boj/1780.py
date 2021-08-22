from sys import stdin
from sys import setrecursionlimit
input = stdin.readline
setrecursionlimit(26800)

n = int(input())
lst = []

def nine(l):
    global cnt1, cnt0, cnt_1
    cnt1, cnt0, cnt_1 = 0, 0, 0

    a = l[0][0]
    for i in range(n):
        for j in range(n):
            if a != lst[i][j]:
                nine(l[0:n//3][0:n//3])
                nine(l[0:n//3][n//3:2*n//3])
                nine(l[0:n//3][2*n//3:n])
                nine(l[n//3:2*n//3][n//3:2*n//3])
                nine(l[n//3:2*n//3][0:n//3])
                nine(l[n//3:2*n//3][2*n//3:n])
                nine(l[2*n//3:n][n//3:2*n//3])
                nine(l[2*n//3:n][0:n//3])
                nine(l[2*n//3:n][2*n//3:n])
                return
    if a == 0:
        cnt0 += 1
    elif a == 1:
        cnt1 += 1
    else:
        cnt_1 += 1


for _ in range(n):
    lst.append(list(input().split()))

nine(lst)

print(cnt_1, cnt0, cnt1)
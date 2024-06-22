from sys import stdin
from sys import setrecursionlimit
input = stdin.readline
setrecursionlimit(26800)

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

cnt1, cnt0, cnt_1 = 0, 0, 0

def nine(x, y, l):
    global cnt1, cnt0, cnt_1


    a = lst[y][x]

    for i in range(x, x+l):
        for j in range(y, y+l):
            if a != lst[j][i]:
                for k in range(3):
                    for m in range(3):
                        nine(l // 3 * k + x, l // 3 * m + y, l//3)
                return
    if a == 0:
        cnt0 += 1
    elif a == 1:
        cnt1 += 1
    else:
        cnt_1 += 1



nine(0, 0, n)

print(cnt_1, cnt0, cnt1)

# 리커션 에러
# 타임 에러
# x, y, n 입력값을 안했음
# # 그래서 아매 메모리 에러도 있었어
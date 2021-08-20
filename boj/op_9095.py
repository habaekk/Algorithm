from sys import stdin
input = stdin.readline
T = int(input())
import math

for _ in range(T):
    n = int(input())
    cnt = 0
    for i in range(4):
        for j in range(6):
            for k in range(12):
                if 3 * i + j * 2 + k == n:
                    lst = [i, j, k]
                    dv = 1
                    for l in lst:
                        if l == 0:
                            pass
                        else:
                            dv *= math.factorial(l)
                    cnt += math.factorial(i+j+k) / dv

    print(int(cnt))

# DP
# 5를 구해 봤더라면
# 재귀 재귀 재귀 재귀
# 집중이 안돼
# 수학
# 프로그래밍
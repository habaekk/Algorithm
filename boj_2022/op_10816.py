import sys
N = int(sys.stdin.readline())
lst = [0] * 20000001
lst1 = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    lst[lst1[i]+10000000] += 1
M = int(sys.stdin.readline())
lst2 = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    print((lst[lst2[i]+10000000]))


# 사실은 이진 탐색 활용으로 풀 수 있음
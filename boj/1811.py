import sys

N, M, B = map(int, sys.stdin.readline().split())
lst = [[0] * M for _ in range(N)]
for i in range(N):
    lst[i] = list(map(int, sys.stdin.readline().split()))

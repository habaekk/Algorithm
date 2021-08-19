from sys import stdin
input = stdin.readline
dic = {}
N, M = map(int, input().split())
for i in range(N):
    domain, pw = input().split()
    dic[domain] = pw
for j in range(M):
    dm = input().strip("\n")
    print(dic[dm])
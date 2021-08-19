from sys import stdin
input = stdin.readline

dic1 = {}

N, M = map(int, input().split())

for i in range(1, N+1):
    s = input().strip("\n")
    dic1[str(i)] = s
    dic1[s] = str(i)

for j in range(M):
    t = input().strip("\n")
    print(dic1[t])

# isalpha
# isdigit
# isalnum 
# 도 가능
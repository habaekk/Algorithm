from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

dp = [0]
for i in range(len(lst)):
    dp.append(lst[i]+dp[i])

for _ in range(M):
    a, b = map(int, input().split())
    print(dp[b] - dp[a-1])


# dp
# for(M) 안에 dp 넣지 말고 밖에서 # 100,000 번이니까
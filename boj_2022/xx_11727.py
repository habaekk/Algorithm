from sys import stdin
input = stdin.readline
dp = [0, 1, 3]
n = int(input())

for i in range(3, n+1):
    dp.append(dp[i-2]*2 + dp[i-1])
print(dp[n] % 10007)

# dp는 bottom-up을 써라
# dp top-down 하려면 재귀 함수
# 규칙을 왜 못 찾니? # 수를 왜 못 세니?
# 암튼 dp는 이런 느낌으로 풀자~
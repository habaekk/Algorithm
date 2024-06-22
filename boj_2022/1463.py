from sys import stdin
input = stdin.readline

n = int(input())
dp = [0, 0, 1, 1]

for i in range(4, n+1):
    cnt1 = 999999
    cnt2 = 999999
    cnt3 = 999999
    if (i / 2).is_integer():
        cnt2 = dp[i // 2] + 1
    if (i / 3).is_integer():
        cnt3 = dp[i // 3] + 1
    cnt1 = dp[i-1] + 1
    dp.append(min(cnt1, cnt2, cnt3))
print(dp[n])
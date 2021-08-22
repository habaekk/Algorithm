from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))
ans = 0
lst.reverse()
for i in lst:
    if k / i >= 1:
        d = k // i
        ans += d
        k -= d * i
        if k == 0:
            break

print(ans)
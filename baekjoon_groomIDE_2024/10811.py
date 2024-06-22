import sys
input = sys.stdin.read
data = list(map(int, input().split()))

n = data[0]
m = data[1]

lst = list(range(1, n+1))

idx1 = 2
for _ in range(m):
    i = data[idx1]
    j = data[idx1+1]
    lst[i-1:j] = list(reversed(lst[i-1:j]))
    idx1 += 2

print(" ".join(map(str, lst)))
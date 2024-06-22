import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

lst = [0] * n

index = 2
for _ in range(m):
    i = int(data[index])
    j = int(data[index + 1])
    k = int(data[index + 2])
    for idx in range(i - 1, j):
        lst[idx] = k
    index += 3

print(" ".join(map(str, lst)))
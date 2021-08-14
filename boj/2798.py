N, M = map(int, input().split())
lst = list(input().split())
for i in range(len(lst)):
    lst[i] = int(lst[i])

target = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if i == k or j == k:
                continue
            sum = lst[i] + lst[j] + lst[k]
            if sum <= M and sum > target:
                target = sum

print(target)
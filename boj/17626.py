import sys

n = int(sys.stdin.readline())
ans = 0

lst = []

# 제곱수들 모음
for i in range(1,224):
    lst.append(i**2)
l = len(lst)

# 답이 3인 경우
for i in range(l):
    for j in range(l):
        for k in range(l):
            if lst[i] + lst[j] + lst[k] == n:
                ans = 3

# 답이 2인 경우
for i in range(l):
    for j in range(l):
        if lst[i] + lst[j] == n:
            ans = 2                

# 답이 1인 경우
for i in range(l):
    if lst[i] == n:
        ans = 1            

# ans가 1, 2, 3이 아니면 ans는 무조건 4
if ans == 0:
    ans = 4

print(ans)
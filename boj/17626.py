import sys

n = int(sys.stdin.readline())
ans = 0

lst = []
for i in range(1,224):
    lst.append(i**2)
l = len(lst)

# 3
for i in range(l):
    for j in range(l):
        for k in range(l):
            if lst[i] + lst[j] + lst[k] == n:
                ans = 3

# 2
for i in range(l):
    for j in range(l):
        if lst[i] + lst[j] == n:
            ans = 2                

# 1
for i in range(l):
    if lst[i] == n:
        ans = 1            

if ans == 0:
    ans = 4

print(ans)
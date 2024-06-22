### ChatGPT revised ###

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
    lst[i-1], lst[j-1] = lst[j-1], lst[i-1]
    idx1 += 2
    
print(" ".join(map(str, lst)))



### ORIGINAL ###

# import sys
# input = sys.stdin.read
# data = input().split()

# n = int(data[0])
# m = int(data[1])

# lst = [0] * n

# index = 2
# for _ in range(m):
#     i = int(data[index])
#     j = int(data[index + 1])
#     k = int(data[index + 2])
#     for idx in range(i - 1, j):
#         lst[idx] = k
#     index += 3

# print(" ".join(map(str, lst)))
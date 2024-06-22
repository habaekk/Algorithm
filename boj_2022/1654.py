import sys
K, N = map(int, sys.stdin.readline().split()) # K: lines in possession # N: lines needed
lst = []
for _ in range(K):
    lst.append(int(sys.stdin.readline()))

left = 1
right = max(lst)

while left <= right:
    sum = 0
    mid = (left + right) // 2
    for i in range(K):
       sum += lst[i] // mid
    if sum >= N:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1        

print(ans)
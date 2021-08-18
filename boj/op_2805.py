import sys

N, M = map(int, sys.stdin.readline().split()) # N: num of woods # M: target
lst = list(map(int, sys.stdin.readline().split()))
bottom = 0
top = max(lst)
mid = top // 2
while bottom <= top:

    mid = (top + bottom) // 2
    woodGet = 0
    for i in range(N):
        if lst[i] > mid:
            woodGet += lst[i] - mid

    if woodGet == M:
        ans = mid
        break
    elif woodGet > M:
        bottom = mid + 1
        ans = mid
    else:
        top = mid - 1
print(ans)

# 이진 탐색
# 깔끔 하지 못해
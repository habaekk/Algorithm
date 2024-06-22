from sys import stdin
input = stdin.readline

# def z(r, c, N):
#     x, y = 0, 0
#     if N > 1:
#         z(x, y, N//2)
#         z(N//2, y, N//2)
#         z(x, N//2, N//2)
#         z(N//2, N//2, N//2)

# 분할정복인가?
# 시간을 보니 아니다

# 그럼 더 간단하게
n, c, r = map(int, input().split())
# c, r 뒤바뀜

# 행렬 헷갈림
# c = c - 1
# r = r - 1

n = 2**n
cnt = 0
while n > 1:
    if r < n//2 and c < n//2:
        cnt += 0
        # x, y = 0, 0 # 분할 정복식 사고의 잔재
        r, c = r, c
    elif r >= n//2 and c < n//2:
        cnt += (n//2)**2*1
        # x, y = n//2, 0
        r, c = r - n//2, c
    elif r < n//2 and c >= n//2:
        cnt += (n//2)**2*2
        # x, y = 0, n//2
        r, c = r, c - n//2
    else:
        cnt += (n//2)**2*3
        # x, y = n//2, n//2
        r, c = r - n//2, c - n//2
    n = n//2
print(cnt)

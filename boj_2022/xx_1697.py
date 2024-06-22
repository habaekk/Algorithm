import sys
from collections import deque

LIMIT = 100001

def solve(arr, n, k):
    q = deque()
    q.append(n)

    while q:
        i = q.popleft()

        if i == k:
            return arr[i]

        for j in (i+1, i-1, 2*i):
            if (0 <= j < LIMIT) and arr[j] == 0:
                arr[j] = arr[i] + 1
                q.append(j)

N, K = map(int, sys.stdin.readline().split())
find = [0] * LIMIT

print(solve(find, N, K))

# https://devjin-blog.com/boj-1697-hideseek/

# from sys import stdin
# input = stdin.readline

# def double(x):
#     return x*2

# # def walkBackward(x):
# #     return x - 1

# # def walkFoward(x):
# #     return x + 1

# n, k = map(int, input().split())

# pos = n
# cnt = 0

# while pos != k:
#     if pos == 0:
#         cnt += 1
#         pos += 1
#         continue

#     if n > k:
#         cnt += n - k
#         pos = k
#         break
    
#     if double(pos) < k:
#         pos = double(pos)
#         cnt += 1
#         continue
#     elif double(pos) > k:
#         a = k - pos
#         if k % 2 == 0:
#             b = n - (k // 2) + 1
#             c = 9999999999
#         else:
#             b = (pos - (k // 2)) + 2
#             c = (pos - ((k+1)// 2)) + 2
#         cnt += min(a, b, c)
#         pos = k
#     else:
#         cnt += 1
#         pos = double(pos)

# print(cnt)


##############
# MAX를 직접 정하기
# 조건에 걸면 인덱스 아오레 안 걸림
# arr로 제일 처음 온 기록 정하기 # 조건문으로 이미 자리 차있으면 못 오게
# 완전 탐색
# brute force
# 비트마스크
# 순열
# 백트래킹
# BFS
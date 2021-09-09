from collections import deque
m, n = map(int, input().split())
s = []
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    s.append(list(map(int, input().split())))
def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and s[x][y] == 0:
                s[x][y] = s[a][b] + 1
                queue.append([x, y])
for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            queue.append([i, j])
bfs()
isTrue = False
result = -2
for i in s:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)


# https://pacific-ocean.tistory.com/267

# x, y 뒤집히는 건 어쩔 수 없다
# 최소거리 찾기 BFS 방법 기억
# BFS DFS 활용
# 하나하나 쓰지말고 dx dy 사용
# 경우에 맞게 for i in (a, b, c) 이런 식으로
# 하나하나 비교해주면서 최댓값 찾기
# 시작 노드 모아놓기
# 인덱스 범위 볼 때 더해놓고 인덱스가 범위 안에 있는지 아닌지 비교
# 전의 값에 더해 놓기 전의 값에 더해 놓기
# -1인 경우의 수 # 경우의 수 분리하고 생각

# 생각하고 코딩하기




# from sys import stdin
# from collections import deque
# input = stdin.readline
# m, n = map(int, input().split())


# lst = []
# for _ in range(n):
#     lst.append(list(map(int, input().split())))
# maxX = m
# maxY = n
# clst = []
# cnt = 0

# def DFS(x, y):
#     global cnt
#     queue = deque([(x, y)])
    
#     while queue:
#         c = False
#         cc = 0
#         pos = queue.popleft()
#         x, y = pos[0], pos[1]
#         n = lst[y][x]
#         if n == 1:
#             if lst[y][x] == 1:
#                 if x < maxX - 1:
#                     if lst[y][x+1] == 0:
#                         lst[y][x+1] = 1
#                         c = True
#                         cc += 1
#                         queue.append((x+1, y))
#                 if x > 0:
#                     if lst[y][x-1] == 0:
#                         lst[y][x-1] = 1
#                         c = True
#                         cc += 1
#                         queue.append((x-1, y))
#                 if y < maxY - 1:
#                     if lst[y+1][x] == 0:
#                         lst[y+1][x] = 1
#                         c = True
#                         cc += 1
#                         queue.append((x, y+1))
#                 if y > 0:
#                     if lst[y-1][x] == 0:
#                         lst[y-1][x] = 1
#                         c = True
#                         cc += 1
#                         queue.append((x, y-1))
#             if c == True:
#                 cnt += 1

# for i in range(n):
#     for j in range(m):
#         DFS(j, i)

# lst2 = []
# for k in range(n-1):
#     lst2.extend(lst[k])
# ans = 1
# if 0 in lst2:
#     ans = -1
# else:
#     if cnt == 0:
#         ans = 0
#     else:
#         ans = cnt
# print(ans)
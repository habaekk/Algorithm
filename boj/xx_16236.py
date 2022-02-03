# from collections import deque
# import sys
# inputs = sys.stdin.readline

# N = int(input())

# sharkShark = []

# for _ in range(N):
#     sharkShark.append(list(map(int, input().split())))

# for i in range(N):
#     for j in range(N):
#         shark = sharkShark[i][j]
#         if shark == 9:
#             x = i
#             y = j

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# # 먹이 체크
# def preyCheck(lst):
#     eat = False
#     for i in range(N):
#         for j in range(N):
#             prey = lst[i][j]
#             if lst[i][j] != 0 and prey < size:
#                 eat = True
#                 return eat
#     return eat
# # 탐색 하며 이동 거리 체크
# def BFS(x, y, lst, s):
#     movement = [[0] * N for _ in range(N)]
#     root = (x, y)
#     stack = deque([root])
#     visited = []
#     temp = [(100,-1, -1)]
#     while stack:
#         x, y = stack.popleft()
#         if (x, y) not in visited:
#             visited.append((x, y))
#             if lst[x][y] != 0 and lst[x][y] < s:
#                 temp.append((movement[x][y], x, y))
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
                
#                 if nx < 0 or ny < 0 or nx >= N or ny >= N:
#                     continue
#                 if lst[nx][ny] > s:
#                     continue
                
#                 if lst[nx][ny] == 0 or (lst[nx][ny] <= s):
#                     stack.append((nx, ny))
#                     movement[nx][ny] = movement[x][y] + 1
#     return min(temp)
# mamaShark = 0       
# size = 2
# count = 0
# while preyCheck(sharkShark) == True:
#     move, mx, my = BFS(x, y, sharkShark, size)
#     if mx == -1:
#         break
#     sharkShark[mx][my] = 9
#     sharkShark[x][y] = 0
#     x, y = mx, my
#     mamaShark += move
#     count += 1
#     if count == size:
#         size += 1
#         count = 0

# print(mamaShark)

from collections import deque
import sys
def bfs(i, j):
    visit = [[0] * n for i in range(n)]
    visit[i][j] = 1
    eat = []
    dist = [[0] * n for i in range(n)]
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if s[nx][ny] <= s[i][j] or s[nx][ny] == 0:
                    q.append([nx, ny])
                    visit[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                if s[nx][ny] < s[i][j] and s[nx][ny] != 0:
                    eat.append([nx, ny, dist[nx][ny]])
    if not eat:
        return -1, -1, -1
    eat.sort(key = lambda x : (x[2], x[0], x[1]))
    return eat[0][0], eat[0][1], eat[0][2]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
input = sys.stdin.readline
n = int(input())
s = []
for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)
    for j in range(n):
        if a[j] == 9:
            s[i][j] = 2
            start = [i, j]
exp = 0
cnt = 0
while True:
    i, j = start[0], start[1]
    ex, ey, dist = bfs(i, j)
    if ex == -1: break
    s[ex][ey] = s[i][j]
    s[i][j] = 0
    start = [ex, ey]
    exp += 1
    if exp == s[ex][ey]:
        exp = 0
        s[ex][ey] += 1
    cnt += dist
print(cnt)

# 복잡하다 복잡해
# > 런 안되면 런타임 에러 있는 상태?
# 왜 안되냐

# 에러가 나면 문제 조건 중 잘 못 된 건 없나 봐보자
# 애초에 알고리즘을 이상하게 짜긴 했다
# 이것 저것 덕지덕지 쓸모 없는 코드가 붙어 있는 막 붙여 놓은 알고리즘
# 복잡해서 틀렸다
# 그냥 시작을 잘 못 한 듯

# 20
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 3 3 4 4
# 0 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 9 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
# 0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 2 3 3 4 4
# 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 4
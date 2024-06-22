from collections import deque
import sys

input = sys.stdin.readline

m, n, h = map(int, input().split())
tomatos = []
for _ in range(h):
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().split())))
    tomatos.append(temp)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# tomatos[h][n][m]
root = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatos[i][j][k] == 1:
                root.append((i, j, k))

stack = deque(root)
while stack:
    z, y, x = stack.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if nx < 0 or ny < 0 or nz < 0 or nx >= m or ny >= n or nz >= h:
            continue
        if tomatos[nz][ny][nx] == -1:
            continue

        if tomatos[nz][ny][nx] == 0:
            tomatos[nz][ny][nx] = tomatos[z][y][x] + 1
            stack.append((nz, ny, nx))

def result(lst):
    result = 0
    max = -10
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if lst[i][j][k] == 0:
                    result = -1
                    return result
                elif lst[i][j][k] > max:
                    max = lst[i][j][k]
    if max == 1:
        result = 0
    else:
        result = max - 1
    return result

print(result(tomatos))

# pypy3 python 시간초과 차이
# from sys import stdin / import sys 차이 ???
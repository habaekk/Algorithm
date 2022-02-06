import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(input().strip()))

visited = []
count = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(n):
        if (i, j) not in visited and lst[i][j] != '0':
            count += 1

        root = (i, j)
        stack = deque([root])

        while stack:
            a = stack.popleft()
            x, y = a
            if lst[x][y] != '0':
                if a not in visited:
                    lst[x][y] = str(count)
                    visited.append(a)
                    for l in range(4): ###### l -> i 는 틀린다.
                        nx = x + dx[l]
                        ny = y + dy[l]

                        if nx < 0 or ny <0 or nx >= n or ny >= n:
                            continue
                        if lst[nx][ny] == '0':
                            continue

                        if lst[nx][ny] == '1':
                            stack.append((nx, ny))
                            lst[nx][ny] == str(count)

print(count)

houseCount = []
for k in range(1, count+1):
    temp = 0
    for i in range(n):
        for j in range(n):
            if lst[i][j] == str(k):
                temp += 1
    houseCount.append(temp)

houseCount.sort()
for i in range(count):
    print(houseCount[i])

    # for문 i, j, k 다 다르게 쓰기.
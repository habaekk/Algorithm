# n = int(input())
# lst = []
# lst_rg = [[0]*n for _ in range(n)]
# for _ in range(n):
#     lst.append(list(input()))

# for i in range(n):
#     for j in range(n):
#         c = lst[i][j]
#         if c == 'R' or c == 'G':
#             lst_rg[i][j] = 'RG'

# lst2 = []
# lst3 = [[0]*n for _ in range(n)]
# color_i = 0

# def udrl(x, y, color_i):
#     color = lst[x][y]
#     if color == lst[x-1][y] and x-1 > -1:
#         if (x-1, y) not in lst2:
#             lst3[x-1][y] = color_i
#             lst2.append((x-1, y))
#             udrl(x-1, y, color_i)
#     if color == lst[x][y-1] and y-1 > -1:
#         if (x, y-1) not in lst2:
#             lst3[x][y-1] = color_i
#             lst2.append((x, y-1))
#             udrl(x, y-1, color_i)
#     if x+1 < n and color == lst[x+1][y]:
#         if (x+1, y) not in lst2:
#             lst3[x+1][y] = color_i
#             lst2.append((x+1, y))
#             udrl(x+1, y, color_i)
#     if y+1 < n and color == lst[x][y+1]:
#         if (x, y+1) not in lst2:
#             lst3[x][y+1] = color_i
#             lst2.append((x, y+1))
#             udrl(x, y+1, color_i)


# for i in range(n):
#     for j in range(n):
#         if (i, j) not in lst2:
#             color_i += 1
#             lst3[i][j] = color_i
#             lst2.append((i, j))
#             udrl(i, j, color_i)

# lst2 = []
# lst3 = [[0]*n for _ in range(n)]
# color_i_rg = 0

# def udrl_rg(x, y, color_i):
#     color = lst_rg[x][y]
#     if color == lst_rg[x-1][y] and x-1 > -1:
#         if (x-1, y) not in lst2:
#             lst3[x-1][y] = color_i
#             lst2.append((x-1, y))
#             udrl_rg(x-1, y, color_i)
#     if color == lst_rg[x][y-1] and y-1 > -1:
#         if (x, y-1) not in lst2:
#             lst3[x][y-1] = color_i
#             lst2.append((x, y-1))
#             udrl_rg(x, y-1, color_i)
#     if x+1 < n and color == lst_rg[x+1][y]:
#         if (x+1, y) not in lst2:
#             lst3[x+1][y] = color_i
#             lst2.append((x+1, y))
#             udrl_rg(x+1, y, color_i)
#     if y+1 < n and color == lst_rg[x][y+1]:
#         if (x, y+1) not in lst2:
#             lst3[x][y+1] = color_i
#             lst2.append((x, y+1))
#             udrl_rg(x, y+1, color_i)

# for i in range(n):
#     for j in range(n):
#         if (i, j) not in lst2:
#             color_i_rg += 1
#             lst3[i][j] = color_i_rg
#             lst2.append((i, j))
#             udrl_rg(i, j, color_i_rg)

# print(color_i, color_i_rg)

# 문제를 보고 어떤 유형의 문제인가? 부터 생각하자
# 어떤 알고리즘을 써야하나?

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(i, j, v, arr):
    queue = [[i, j]]
    arr[i][j] = 0
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < n and arr[x][y] == v:
                queue.append([x, y])
                arr[x][y] = 0
n = int(input())
s = []
copy = [[0] * n for i in range(n)]
cnt = 0
cntt = 0
for i in range(n):
    s.append(list(map(str, input())))
for i in range(n):
    for j in range(n):
        if s[i][j] == "R" or s[i][j] == "G":
            copy[i][j] = 1
        else:
            copy[i][j] = 2
for i in range(n):
    for j in range(n):
        if s[i][j] != 0:
            bfs(i, j, s[i][j], s)
            cnt += 1
        if copy[i][j] != 0:
            bfs(i, j, copy[i][j], copy)
            cntt += 1
print(cnt, cntt)

# https://pacific-ocean.tistory.com/264

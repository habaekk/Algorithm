from sys import stdin
input = stdin.readline

def S(graph, pos):
    visited = []
    stack = [pos]
    x = pos[0]
    y = pos[1]

    while stack:
        n = stack.pop()
        x = n[0]
        y = n[1]
        if n not in visited and n in lst:
            visited.append(n)
            stack.append((x+1, y))
            stack.append((x, y + 1))
            stack.append((x - 1, y))
            stack.append((x, y - 1))
    return visited

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    lst = []
    for _ in range(k):
        x, y = map(int, input().split())
        lst.append((x, y))

    clst = set()
    cnt = 0
    for position in lst:
        if position in clst:
            continue
        else:
            llst = sorted(S(lst, position))
            clst.update(set(llst))
            cnt += 1

    print(cnt)

# 재귀식 dfs가 시간이 더 짧음
# 탐색한 놈 0으로 갱신법
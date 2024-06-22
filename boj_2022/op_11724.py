from sys import stdin
input = stdin.readline

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

n, m = map(int, input().split())
graph_list = {}
cnt = 0

for i in range(1, n+1):
    graph_list[i] = set()
for j in range(m):
    u, v = map(int, input().split())
    graph_list[u].add(v)
    graph_list[v].add(u)

slst = []
cnt = 0
for i in range(1, n+1):
    if i not in slst:
        lst = DFS(graph_list, i)
        cnt += 1
        slst.extend(lst)

print(cnt)


# 연결 요소?
# DFS BFS
# 인접리스트?
# 다른 사람은 다르게 품
# 재귀

# import sys
# sys.setrecursionlimit(10000)

# def dfs(v):
#     visited[v] = True
#     for e in adj[v]:
#         if not visited[e]:
#             dfs(e)
            
# N, M = map(int, input().split())
# adj = [[] for _ in range(N + 1)]
# visited = [False] * (N + 1)
# count = 0

# for _ in range(M):
#     u, v = map(int, input().split())
#     adj[u].append(v)
#     adj[v].append(u)
    
# for j in range(1, N + 1):
#     if not visited[j]:
#         dfs(j)
#         count += 1

# print(count)

# https://velog.io/@devjuun_s/연결-요소의-개수-백준-11724번python
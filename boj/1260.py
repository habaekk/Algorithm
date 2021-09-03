from sys import stdin
from collections import deque

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            lst = list(graph_list[n] - set(visited))
            lst.sort()
            queue += lst
            # queue += list(graph[n] - set(visited)).sort()
    return visited

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            lst = list(graph_list[n] - set(visited))
            lst.sort()
            stack += reversed(lst)
            # stack += reversed(list(graph[n] - set(visited)).sort())
    return visited


graph_list = {}
n, m, k = map(int, input().split())
for i in range(1, n+1):
    graph_list[i] = set()
for j in range(m):
    a, b = map(int, input().split())
    graph_list[a].add(b)
    graph_list[b].add(a)

result_DFS = DFS(graph_list, k)
result_BFS = BFS(graph_list, k)

for i in range(len(result_DFS)):
    print(result_DFS[i], end=" ")
print()
for i in range(len(result_BFS)):
    print(result_BFS[i], end=" ")
print()


# print(type(list(set(1)))) 다 같이 쓰면 왜 오류나냐??
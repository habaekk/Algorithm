from collections import deque

def bfs(graph, root):
    visited = set()
    queue = deque([root])
    i = 0
    while queue:
        n = queue.popleft()
        if n not in visited:
            if i != 0:
                visited.add(n)
            queue += set(graph[n]) - set(visited)
        i += 1
    
    return visited
    

n = int(input())
lst = []
dic = {}

for _ in range(n):
    lst.append(list(map(int, input().split())))

for i in range(n):
    dic[i] = []
    for j in range(n):
        if lst[i][j] == 1:
            a = dic[i]
            a.append(j)

lst_ans = [[0]*n for _ in range(n)]
for i in range(n):
    visited_current = bfs(dic, i)
    for node in visited_current:
        lst_ans[i][node] = 1

for i in range(n):
    for j in range(n):
        print(lst_ans[i][j], end=" ")
    print()

# 플로이드 - 와샬을 쓰면 더 쉽다.
# 플로이드 - 와샬 쓰이는 데가 많아 보인다.
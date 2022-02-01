# 그래프, 최소거리, 반복
# from collections import deque
# import sys
# n, m = map(int, sys.stdin.readline().split())

# lst = []
# cavin_lst = []
# for i in range(m):
#     lst.append(list(map(int, sys.stdin.readline().split())))

# for i in range(1, m+1):
#     cavinBacon = 0
#     visited = set()
#     queue = deque([i])
#     times = 1
#     while len(visited) < m:
#         current = queue.popleft()
#         for j in range(m):
#             a = lst[j][0]
#             b = lst[j][1]

#             if a == current:
#                 cc = b
#                 cavinBacon += times
#                 queue.append(cc)
#                 visited.add(cc)
#             elif b == current:
#                 cc = a
#                 cavinBacon += times
#                 queue.append(cc)
#                 visited.add(cc)
#         times += 1
        
#     cavin_lst.append(cavinBacon)

# minCavin = min(cavin_lst)
# print(cavin_lst.index(minCavin)+1)

import sys
from collections import deque


def bfs(graph, start):
    num = [0] * (n+1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if i not in visited:
                num[i] = num[a] + 1
                visited.append(i)
                queue.append(i)
    return sum(num)


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    result = []
    for i in range(1, n+1):
        result.append(bfs(graph, i))

    print(result.index(min(result))+1)


# 전체 흐름은 그대로 두고
# 입출력을 문제에 맞게 변형시킨다
# 전체 흐름에 대해 외워야한다
# 입력을 어떻게 변화시킬 것이냐?
# 거기서 출력을 어떻게 만들 것이냐?

# https://chaewsscode.tistory.com/98
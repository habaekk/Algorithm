# from collections import deque

# N, M = map(int, input().split())
# lst = []

# for _ in range(N):
#     lst.append(list(map(int, list(input()))))
# x, y = 0, 0
# lst_sol = [[-1] * M for _ in range(N)]
# lst_sol[0][0] = 1

# dic = {}
# for i in range(N):
#     for j in range(M):
#         if lst[i][j] == 0:
#             continue
#         dic_lst = []
#         if i-1 >= 0:
#             if lst[i-1][j] == 1:
#                 dic_lst.append((i-1, j))
#         if j-1 >= 0:
#             if lst[i][j-1] == 1:
#                 dic_lst.append((i, j-1))
#         if i+1 < N:
#             if lst[i+1][j] == 1:
#                 dic_lst.append((i+1, j))
#         if j+1 < M:
#             if lst[i][j+1] == 1:
#                 dic_lst.append((i, j+1))
#         dic[(i, j)] = set(dic_lst)

# lst_sol[0][0] = 1
# visited = []
# stack = deque([(0, 0)])
# while stack:
#     smol = []
#     node = stack.popleft()
#     a = node[0]
#     b = node[1]
#     if node not in visited:
#         visited.append(node)
#         stack += dic[node] - set(visited)
#         if not(a == 0 and b == 0):
#             for node2 in dic[node]:
#                 if node2 in visited:
#                     aa = node2[0]
#                     bb = node2[1]
#                     smol.append(lst_sol[aa][bb])
#             lst_sol[a][b] = min(smol) + 1

# print(lst_sol[N-1][M-1])

from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

# 너비 우선 탐색
def bfs(x, y):
  # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
  dx = [-1, 1, 0, 0] 
  dy = [0, 0, -1, 1]

  # deque 생성
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    
    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 위치가 벗어나면 안되기 때문에 조건 추가
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      
      # 벽이므로 진행 불가
      if graph[nx][ny] == 0:
        continue
      
      # 벽이 아니므로 이동
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  
  # 마지막 값에서 카운트 값을 뽑는다.
  return graph[N-1][M-1]

print(bfs(0, 0))

# 리스트로 주어지는 문제에서는 dx dy 를 적극 이용하자
# 그래프 탐색은 BFS 아니면 DFS 다. 
# 복잡하게 생각하지 말자
# 새로운 리스트를 쓸 생각하지 말고 그냥 준 거에서 쓰자.
# 딱 봐도 코드가 복잡해지면 제출 해도 오류난다.
# 딱딱하게 새로운 변수로 조작하지 말고, 문제에서 주어진 대로 물 흐르듯이 연결해서 쓰자.
# 완벽한 코드보다 작동하면서 알아서 되는 코드를 쓰자. 느리다.
# 답만 빠르게 구하자.
# visited 안 챙겨도 된다.
# for k in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# for k in range(N): #경로 for문이 가장 상위 단계여야 누락되지 않는다
#     for i in range(N):
#         for j in range(N): 
#             if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
#                 graph[i][j] = 1

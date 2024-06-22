# from sys import stdin
# input = stdin.readline

# def sq2(sqr2):
#     check = True
#     blueCnt = 1
#     whiteCnt = 0
#     for i in range(2):
#         for j in range(2):
#             if sqr2[i][j] != 1:
#                 check = False
#                 whiteCnt += 1
#     if check == True:
#         whiteCnt = 0
#     return whiteCnt


# lst = []
# nlst = []
# N = int(input())
# for i in range(N):
#     lst.append(list(map(int, input().split())))

# white = sq2(lst)
# blue = 

# # lt = lst[0:len(lst) // 2][0:len(lst) // 2]

# # lb = lst[0:len(lst) // 2][(len(lst) // 2) + 1:len(lst)]

# # rt = lst[(len(lst) // 2) + 1:len(lst)][0:len(lst) // 2]

# # rb = lst[(len(lst) // 2) + 1:len(lst)][(len(lst) // 2) + 1:len(lst)]

# # print(lt)

import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

result = []

def solution(x, y, N) :
  color = paper[x][y]
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != paper[i][j] :
        solution(x, y, N//2)
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  if color == 0 :
    result.append(0)
  else :
    result.append(1)


solution(0,0,N)
print(result.count(0))
print(result.count(1))

# 분할 정복
# 쿼드 트리
# 재귀 함수
# 한 줄 반복문
# 리스트와 함수 순서
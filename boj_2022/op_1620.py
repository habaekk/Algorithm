from sys import stdin
input = stdin.readline

dic1 = {}

N, M = map(int, input().split())

# N 개의 줄 입력
for i in range(1, N+1):
    s = input().strip("\n")

    # 딕셔너리에 추가 -> {번호: 이름, 이름: 번호}
    dic1[str(i)] = s
    dic1[s] = str(i)

# M 개의 줄 입력
for j in range(M):
    t = input().strip("\n")
    print(dic1[t])

# isalpha
# isdigit
# isalnum 
# 도 가능
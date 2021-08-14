N, M = map(int, input().split())
lst1 = []
cnt = 0
minv = 9999999999999999

# BW 테이블 2D array 로
for _ in range(N):
    lst1.append(list(input()))
#####test
# print(lst1)

# 시작 좌표 i, j
for i in range(N-7):
    for j in range(M-7):
        # cnt 초기화
        b_cnt = 0
        w_cnt = 0
        cnt = 0
        # 왼쪽 위 B

        for k in range(8):
            for l in range(8):
                if k % 2 == 0:
                    if l % 2 == 0:
                        # 짝수 행 짝수 열
                        if lst1[i+k][j+l] != "B":
                            b_cnt += 1
                    else:
                        # 짝수 행 홀수 열
                        if lst1[i+k][j+l] != "W":
                            b_cnt += 1
                else:
                    if l % 2 == 0:
                        # 홀수 행 짝수 열
                        if lst1[i+k][j+l] != "W":
                            b_cnt += 1 
                    else:
                        # 홀수 행 홀수 열
                        if lst1[i+k][j+l] != "B":
                            b_cnt += 1
        
        # 왼쪽 위 W

        for k in range(8):
            for l in range(8):
                if k % 2 == 0:
                    if l % 2 == 0:
                        # 짝수 행 짝수 열
                        if lst1[i+k][j+l] != "W":
                            w_cnt += 1
                            # print(5, i+k, j+l)
                    else:
                        # 짝수 행 홀수 열
                        if lst1[i+k][j+l] != "B":
                            w_cnt += 1
                            # print(6, i+k, j+l)
                else:
                    if l % 2 == 0:
                        # 홀수 행 짝수 열
                        if lst1[i+k][j+l] != "B":
                            w_cnt += 1 
                            # print(7, i+k, j+l)
                    else:
                        # 홀수 행 홀수 열
                        if lst1[i+k][j+l] != "W":
                            w_cnt += 1
                            # print(8, i+k, j+l)
        if(b_cnt <= w_cnt):
            cnt = b_cnt
        else:
            cnt = w_cnt
        # 최소 색칠 찾기
        # print(cnt)
        if(cnt <= minv):
            minv = cnt

print(minv)


# 8 8
# BBBBWWWW
# BBBBWWWW
# BBBBWWWW
# BBBBWWWW
# BBBBWWWW
# BBBBWWWW
# BBBBWWWB
# BBBBWWWW

# 시작이 B가 아니라 W일 때 최소가 되는 경우
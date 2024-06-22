import sys

N, M, B = map(int, sys.stdin.readline().split())
lst = [[0] * M for _ in range(N)]
inv = B
time = 0
mintime = 9999999999
ansHeight = 0
for i in range(N):
    lst[i] = list(map(int, sys.stdin.readline().split()))

for i in range(257):
    time = 0
    pls = 0
    min = 0
    inv = B
    for j in range(N):
        for k in range(M):
            height = lst[j][k]
            if height > i:
                pls += height - i
            else:
                min += i - height
    time += pls * 2
    time += min
    inv += pls
    if inv >= min:
        if time <= mintime:
            mintime = time
            ansHeight = i
print(mintime, ansHeight)

# 꼭 조건을 다 하나하나 만족시키려 들지 말고 슈루룩 흘러 가듯이 할 수 있는 방법 생각
# 시간 제한 --> pypy3
# 대략 몇 번 정도 돌지 생각 해보고 괜찮으면 그대로 확신 가지기
# 밖에서 뺴서 연산할 수 있으면 뺴서 한거번에 하기
# 한군데에 모아 놓으면 시간이 줄어든다

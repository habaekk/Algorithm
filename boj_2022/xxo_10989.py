import sys

N = int(sys.stdin.readline())
lst=[0] * 10001

for i in range(N):
    k = int(sys.stdin.readline())
    lst[k] = lst[k] + 1

for j in range(len(lst)):
    if lst[j] != 0:
        for _ in range(lst[j]):
            print(j)


# 숫자 갯수는 10,000,000
# 수의 범위는 10,000
# 리스트의 길이
# 이렇게 펼쳐 놓는 접근법
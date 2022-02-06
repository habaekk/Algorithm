# from sys import stdin
# input = stdin.readline

# n = int(input())
# m = int(input())
# S = input()
# s1 = ""
# s2 = ""

# pn = "IOI" + ("OI" * (n-1))
# lpn = list(pn)
# spn = list(S)
# cnt = 0

# for i in range(len(S) - len(pn)):
#     if lpn == spn[i:i+len(pn)]:
#         cnt += 1
# print(cnt)

from sys import stdin
input = stdin.readline

n = int(input())
m = int(input())
S = input()
s1 = ""
s2 = ""

pn = "IOI" + ("OI" * (n-1))
lpn = list(pn)
spn = list(S)
cnt = 0

for i in range(m - (2*n + 1)):
    if lpn == spn[i:i+(2*n + 1)]:
        cnt += 1
print(cnt)

import sys
n = int(input())
m = int(input())
s = sys.stdin.readline()

cnt = 0
answer = 0
stack=[]

for i in range(m):
    if s[i] == "O":
        continue
    else:
        stack.append(i)

for i in range(1, len(stack)):
    if stack[i] - stack[i-1] == 2:
        cnt += 1
    else:
        cnt = 0

    if cnt >= n:
        answer += 1


print(answer)

# 더 짧게 하려면 선형적으로 수정
# 내 코드의 구조를 알아야 함

# 내가 쓴 코드는 index 가 늘어날 때마다 다시 새로 문자열을 보는 느낌.
# 답안의 코드는 전의 결과를 이용해서 문자열 오른쪽 끝에만 새로(추가로) 보는 느낌.
# 연속적으로 cnt를 해야 할 문자열이 나왔을 때, 새로 보느냐, 아니면 전에 카운트 한 걸 이용하느냐는 차이 정도?

# https://hongcoding.tistory.com/58
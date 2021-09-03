n = int(input())
s = []
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])
s = sorted(s, key=lambda a: (a[0], a[1]))
s = sorted(s, key=lambda a: a[1])
last = 0
cnt = 0
for i, j in s:
    if i >= last:
        cnt += 1
        last = j
print(cnt)



# from sys import stdin
# input = stdin.readline

# n = int(input())
# meetings = []
# for i in range(n):
#     meetings.append(list(map(int, input().split())))

# start = 0
# end = 99999999999
# for j in range(len(meetings)):
#     if meetings[j][1] <= end:
#         start = meetings[j][0]
#         end = meetings[j][1]

# cnt = 1
# while True:
#     end2 = 9999999999
#     for j in range(len(meetings)):
#         if meetings[j][0] >= end and meetings[j][1] <= end2:
#             start = meetings[j][0]
#             end2 = meetings[j][1]

#     if end2 == 9999999999:
#         break
#     else:
#         end = end2
#         cnt += 1


# print(cnt)

# 시간초과
# lambda
# 와
# 이걸 왜 못 하지?
# 다르게 생각하기 다르게 생각하기 다르게 생각하기 다르게 생각하기 다르게 생각하기 다르게 생각하기 다르게 생각하기
# 뭔가 이상하면 다른 방법을 찾자 뭔가 이상하면 다른 방법을 찾자
# 경우를 생각해야 한다
# 덧붙이지 말고 구조 자체를 바꾸자
# 불필요한 코드는 안 써도 되지 않을까?
# 너무 한 쪽으로 확신하지도 말자
# 아닐 수도 있다는 생각


# https://pacific-ocean.tistory.com/236
# https://daimhada.tistory.com/38
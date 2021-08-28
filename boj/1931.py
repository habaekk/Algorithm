from sys import stdin
input = stdin.readline

n = int(input())
# lst1 = []
# lst2 = []
# for _ in range(n):
#     a, b = map(int, input().split())
#     lst1.append(a)
#     lst2.append(b)
# cnt = 0
# start = -1
# end = 99
# temp = 0
# while True:
#     temp = end
#     for i in range(n):
#         a, b = lst1[i], lst2[i]
#         if a >= start and b <= end:
#             start, end = a, b
#     if end != temp:
#         cnt += 1
#     else:
#         break

print(cnt)
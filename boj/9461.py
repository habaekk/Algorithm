from sys import stdin

p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12]
for i in range(12, 101):
    p.append(p[i-1] + p[i-5])
T = int(input())
for _ in range(T):
    n = int(input())
    print(p[n])
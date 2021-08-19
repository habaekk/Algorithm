from sys import stdin
import math
input = stdin.readline

N = int(input())
fac = math.factorial(N)
lst = list(str(fac)) # reversed 쓰셈
lst.reverse()
cnt = 0
for i in range(len(lst)):
    if lst[i] != "0":
        break
    else:
        cnt += 1
print(cnt)
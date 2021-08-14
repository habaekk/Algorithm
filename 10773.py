import sys

K = int(sys.stdin.readline())
lst = []
for i in range(K):
    n = int(sys.stdin.readline())
    if n != 0:
        lst.append(n)
    else:
        lst.pop()
print(sum(lst))
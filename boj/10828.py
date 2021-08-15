import sys
N = int(sys.stdin.readline())
lst = []
n = 0
for _ in range(N):
    s = sys.stdin.readline().strip()
    if s == "pop":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())
    elif s == "size":
        print(len(lst))
    elif s == "empty":
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif s == "top":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
    else:
        s, n = s.split()
        lst.append(n)
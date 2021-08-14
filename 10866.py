import sys
N = int(sys.stdin.readline())
lst = []
n = 0
for _ in range(N):
    s = ""
    n = 0
    s = sys.stdin.readline().strip()
    if s.__contains__(" "):
        s, n = s.split(" ")

    if s == "push_front":
        lst.insert(0, n)
    elif s == "push_back":
        lst.append(n)
    elif s == "pop_front":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop(0))
    elif s == "pop_back":
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
    elif s == "front":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
    elif s == "back":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
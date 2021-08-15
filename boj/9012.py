import sys
N = int(sys.stdin.readline())
for _ in range(N):
    lst = []
    s = sys.stdin.readline().strip()
    lst = list(s)
    i = 0
    while i < len(lst) - 1:
        if lst[i] == "(" and lst[i+1] == ")":
            lst.pop(i)
            lst.pop(i)
            i = 0
            continue
        i += 1    
    if len(lst) != 0:
        print("NO")
    else:
        print("YES")

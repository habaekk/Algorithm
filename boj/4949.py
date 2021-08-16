import sys
while True:
    s = sys.stdin.readline().strip("\n")
    if s == ".":
        break
    
    lst = list(s)
    i = 0
    while i < len(lst):
        tt = lst[i]
        if tt == "(" or  tt == ")" or tt == "[" or tt == "]":
            i += 1
        else:
            lst.pop(i)
            i = 0
            continue
    j = 0
    while j < len(lst) - 1:
        if lst[j] == "(" and lst[j+1] == ")":
            lst.pop(j)
            lst.pop(j)
            j = 0
            continue
        elif lst[j] == "[" and lst[j+1] == "]":
            lst.pop(j)
            lst.pop(j)
            j = 0
            continue
        j += 1
    if len(lst) == 0:
        print("yes")
    else:
        print("no")

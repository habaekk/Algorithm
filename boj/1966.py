import sys
T = int(sys.stdin.readline()) # test case

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split()) # N = number of documents # M = target document
    lst = list(map(int, sys.stdin.readline().split())) # priorities
    targetSeq = 1
    while len(lst) > 0:
        maxPrior = max(lst)
        if M == 0:
            if lst[0] >= maxPrior:
                lst.pop(0)
                break
            else:
                temp = lst.pop(0)
                lst.append(temp)
                M = len(lst) - 1
        else:
            if lst[0] >= maxPrior:
                lst.pop(0)
                targetSeq += 1
            else:
                temp = lst.pop(0)
                lst.append(temp)
            M -= 1


    print(targetSeq)
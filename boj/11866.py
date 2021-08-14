import sys
N, K = map(int, sys.stdin.readline().split())

lst1 = []
lst2 = []
lstY = []

for i in range(N):
    lst1.append(i+1)

indx = 1
while len(lstY) < N:

    while len(lst1) != 0:
        n1 = lst1.pop(0)
        if indx % K == 0:
            lstY.append(n1)
        else:
            lst2.append(n1)
        indx += 1

    while len(lst2) != 0:
        n2 = lst2.pop(0)
        if indx % K == 0:
            lstY.append(n2)
        else:
            lst1.append(n2)
        indx += 1

print("<", end="")
for i in range(N):
    if i != N-1:
        print("%d, " %lstY[i], end="")
    else:
        print("%d>" %lstY[i])
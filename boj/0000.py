import sys
N = int(sys.stdin.readline())
lst1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
lst2 = list(map(int, sys.stdin.readline().split()))
lst1.sort()

for i in range(M):
    print(lst1.count(lst2[i]))
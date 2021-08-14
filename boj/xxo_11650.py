import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort()
print(lst)
for i in range(N):
    print(lst[i][0], lst[i][1])

# input 말고 sys.stdin
import sys

N = int(sys.stdin.readline())
lst=[]
for i in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort()

for i in range(N):
    print(lst[i])

# 중복은 없다
# input 말고 sys.stdin
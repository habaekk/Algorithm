import sys
input = sys.stdin.readline
n = int(input())

lst = []
lst = list(map(int, input().split()))
slst = sorted(list(set(lst)))
dic = {}
for i in range(len(slst)):
    dic[list(slst)[i]] = i

for j in lst:
    sys.stdout.write(str(dic[j]) + " ")
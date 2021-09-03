import sys
input = sys.stdin.readline
n = int(input())

lst = []
lst = list(map(int, input().split()))
slst = sorted(list(set(lst)))
dic = {}
for i in range(len(slst)):
    dic[slst[i]] = i

for j in lst:
    print(str(dic[j]), end = " ")

# for i in range(len(slst)):
#     dic[list(slst[i])] = i
# 이것 때문이라고...?

# 군더더기 없는 코딩을 하자
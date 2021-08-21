from sys import stdin
input = stdin.readline

c = int(input())
l = int(input())
lst =[]
for i in range(l):
    a, b = map(int, input().split())
    lst.append([a, b])

nlst = set({1})
mlst = set()
olst = set()
while len(nlst) != len(olst) :
    for k in nlst:
        olst.add(k)
    for j in nlst:
        for i in range(l):
            if lst[i][1] == j or lst[i][0] == j:
                if lst[i][0] == j:
                    mlst.add(lst[i][1])
                else:
                    mlst.add(lst[i][0])
    nlst.update(mlst)
print(len(nlst)-1)
import sys
N = int(sys.stdin.readline())
lst = []
lst2 = [0] * 80001
for i in range(N):
    lst.append(int(sys.stdin.readline()))
for j in range(N):
    lst2[lst[j]+4000] += 1
maxlst2 = max(lst2)
ik = 0
mode = 0
for k in range(len(lst2)):
    if maxlst2 == lst2[k]:
        mode = k - 4000
        ik += 1
    if ik == 2:
        break
lst.sort()
sum1 = sum(lst)
ave = round(sum1 / N)
mid = (N // 2)
ran = lst[-1] - lst[0]

print(ave)
print(lst[mid])
print(mode)
print(ran)

#Counter
#Dictionary
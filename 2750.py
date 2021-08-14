N = int(input())
lst=[]
for i in range(N):
    n = int(input())
    if lst.__contains__(n):
        continue
    else:
        lst.append(n)
lst.sort()
for i in range(len(lst)):
    print(lst[i])
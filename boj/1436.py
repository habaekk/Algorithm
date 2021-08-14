import sys
N = int(sys.stdin.readline())
cnt = 0
lst = []
for i in range(99999999999999999):
    if "666" in str(i):
        lst.append(i)
        cnt += 1
    if cnt == N:
        break

print(lst[cnt-1])
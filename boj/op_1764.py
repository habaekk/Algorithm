from sys import stdin
input = stdin.readline
set1 = set()
set2 = set()

N, M = map(int, input().split())
for i in range(N):
    set1.add(input().strip("\n"))
for j in range(M):
    set2.add(input().strip("\n"))

ans = sorted(list(set1.intersection(set2)))
print(len(ans))
for os in ans:
    print(os)

# print("seperator".join(list)) 
# 리스트 한 줄 코드로 쫙 출력법
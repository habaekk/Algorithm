from sys import stdin
import heapq
input = stdin.readline

n = int(input())
mh = []
for _ in range(n):
    a = int(input())
    if a == 0:
        if mh:
            print(heapq.heappop(mh)[1])
        else:
            print(0)
    else:
        heapq.heappush(mh, (-a, a))

# heap
# heapq
# 어떨 때 유용한 거냐? # 크기순 필요할떄?
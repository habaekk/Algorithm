import heapq
from sys import stdin
input = stdin.readline

heap = []
n = int(input())
for _ in range(n):
    a = int(input())
    if a == 0:
        if len(heap) == 0:
            print(0)
        else:
            h = heapq.heappop(heap)
            print(h[1])
    else:
        if a > 0:
            heapq.heappush(heap, (a, a))
        else:
            heapq.heappush(heap, (-a, a))

# abs()
import heapq
from sys import stdin

input = stdin.readline

heap = []
# heapq.heapify(heap)
n = int(input())

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
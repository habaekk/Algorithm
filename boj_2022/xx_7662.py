import sys
import heapq
input = sys.stdin.readline


test = int(input())
for _ in range(test):
    max_heap, min_heap = [], []
    visit = [False] * 1_000_001

    order_num = int(input())

    for key in range(order_num):
        order = input().rsplit()
        if order[0] == 'I':
            heapq.heappush(min_heap, (int(order[1]), key))
            heapq.heappush(max_heap, (int(order[1]) * -1, key))
            visit[key] = True #True이면 어떤 힙에서도 아직 삭제되지 않은 상태

        elif order[0] == 'D':
            if order[1] == '-1': #삭제연산시, key값을 기준으로 해당 노드가 다른힙에서 삭제된 노드인가를 먼저 판단한다.
                # 이미 상대힙에 의해 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 계쏙 버리다가 이후 삭제대상노드가 나오면 삭제한다.
                while min_heap and not visit[min_heap[0][1]]: # visit이 False일떄 -> 해당노드가 삭제된상태
                    heapq.heappop(min_heap) # 버림 (상대힙에서 이미 삭제된노드이므로)
                if min_heap:
                    visit[min_heap[0][1]] = False # visit이 Ture엿으므로 False로 바꾸고 내가 삭제함
                    heapq.heappop(min_heap)
            elif order[1] == '1':
                while max_heap and not visit[max_heap[0][1]]: #이미 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 모두 버린다.
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

# 모든 연산이 끝난후에도 ㅅ쓰레기 노드가 들어있을수 있으므로, 결과를 내기전 모두 비우고 각 힙의 첫번째 원소값을 출력한다. 
    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')

        
# from sys import stdin
# import heapq
# input = stdin.readline

# t = int(input())
# for _ in range(t):
#     k = int(input())
#     ansLst = []
#     smallest = []
#     largest = []

#     for __ in range(k):
#         a, b = input().split()
#         b = int(b)
#         if a == "I":
#             heapq.heappush(smallest, b)
#             heapq.heappush(largest, (-b, b))
#         elif a == "D":
#             ss = heapq.heappop(smallest)
#             ll = heapq.heappop(largest)[1]
#             if ss >= ll:
#                 smallest = []
#                 largest = []
#             else:
#                 if b == 1:
#                     heapq.heappush(smallest, ss)
#                 elif b == -1:
#                     heapq.heappush(largest, (-ll, ll))
    
#     s = heapq.heappop(smallest)
#     l = heapq.heappop(largest)[1]



#     if s > l:
#         print("EMPTY")
#     else:
#         print(l, s)

# list max min 아니고
# list sort 아니고
# dequeue 아니고
# 결국 heapq 네 # 그래도 여기까지는 잘 왔다 # 와서 어떻게 하는지 몰라서 문제지

# 이중 우선순위 큐
# ===========
# 이중큐(deque)
# ++++++++++++
# 우선순위큐(heapq)

# 동기화...
# 쓰레기 노드...
# 다시 쓰레기 노드 버리기...

# visit = [0] 8 10001 
# 뭐 요런거 활용 잘 해야해
# 하나도 안 쓰고 있잖슴

# key 쓰는거

# 최대힙 * -1 로 쓰는거

# while, if 조건
# 조건을 영리하게 쓰는거

# 좌절
# 내가 풀 수 있나?
# 와 복잡해

# 내 블로그는 왜 위에 안뜨냐

# https://esoongan.tistory.com/71

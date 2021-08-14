import sys

def card2(lst):
    lst.pop(0)    
    second = lst.pop(0)
    lst.append(second)
    return lst

N = int(sys.stdin.readline())

lst1 = [1]


for i in range(10000):
    if len(lst1) > 500000:
        break
    for j in range(2**i):
        if len(lst1) > 500000:
            break
        lst1.append(2*(j+1))


print(lst1[N-1])

#1 2 2 4 2 4 6 8 2 4 6 8 10 12 14 16 2
#요건 규칙을 찾아낸 거 # 더 간단하고 빠른 규칙이 있더라
#collection deque Cpython 더 빠름?
#Queue Queue 는 뭐냐? 멀티 스레딩? # 알고리즘에선 deque 쓴다
# stack, queue deque
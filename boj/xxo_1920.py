import sys

def binarySearch(target, n, lst):
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return True
        
        if lst[mid] > target:
            right = mid - 1
        elif lst[mid] < target:
            left = mid + 1

N = int(sys.stdin.readline())
lstN = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
lstM = list(map(int, sys.stdin.readline().split()))
        
setN = set(lstN)

for i in range(M):
    if setN.__contains__(lstM[i]):
        print(1)
    else:
        print(0)

# 파이선 set / set 탐색은 왜 빠르냐?
# 파이선 dictionary 도
# 파이선 이진탐색
# 수를 바꾸는게 아니고 리스트를 바꿔버려서 느리나? 그 정도는 이 상태에서 바꿔볼 수 있음.
# 아니면 break를 만나는 게 느리나? # lst1[0] --> lst1[m] 으로 가면? 이것도 바꿔 볼 수 있음.
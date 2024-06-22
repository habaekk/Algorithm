n, m = map(int, input().split())

lst = []
for i in range(1, m+1):
    lst.append(i)

if n == m:
    for i in range(1, m+1):
        print(i, end=" ")
elif m == 1:
    for i in range(1, n+1):
        print(i)
else:
    while True:
        if lst[0] == n:
            break
        if len(set(lst)) == len(lst):
            for a in lst:
                print(a, end=" ")
            print()
        for i in range(m-1, 0, -1):
            if lst[i] >= n:
                lst[i-1] += 1
                lst[i] = lst[i-1]
        lst[m-1] += 1

# 백트랙킹 처음 나온 곳
# https://jamesu.dev/posts/2020/04/13/baekjoon-problem-solving-15649/
# 처음은 아니고 이전 문제가 처음이네. 15649.
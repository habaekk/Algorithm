def factorial(a):
    if a == 1 or a == 0:
        return 1
    else:
        return a * factorial(a-1) 

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    C = int(factorial(M) / (factorial(N) * factorial(M-N)))
    print(C) 
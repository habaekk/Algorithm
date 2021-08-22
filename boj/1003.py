from sys import stdin
input = stdin.readline

T = int(input())
fibo = [[1, 0], [0, 1]]

for i in range(2, 41):
    fibo.append([fibo[i-1][0] + fibo[i-2][0], fibo[i-1][1] + fibo[i-2][1]])

for _ in range(T):
    n = int(input())

    print(fibo[n][0], fibo[n][1])
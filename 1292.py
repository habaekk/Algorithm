def s(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + s(n-1)

def c(n):
    for i in range(1, 9999999):
        if s(i-1) < n and s(i) >= n:
            return i

A, B = map(int, input().split())
sum = 0
for i in range(A, B+1):
    sum += c(i)
print(sum)
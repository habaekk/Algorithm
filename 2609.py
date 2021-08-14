def gcf(a, b):
    quotient_a = a
    quotient_b = b
    lst = []
    result = 1
    while True:
        for i in range(2, 10001):
            if quotient_a % i == 0 and quotient_b % i == 0:
                quotient_a = quotient_a / i
                quotient_b = quotient_b / i
                # print(i, quotient_a, quotient_b)
                lst.append(i)
                break
        if i == 10000:
            break
    for j in lst:
        result *= j
    return int(result)

def lcm(a, b):
    quotient_a = a
    quotient_b = b
    lst = []
    result = 1
    while True:
        for i in range(2, 10001):
            if quotient_a % i == 0 and quotient_b % i == 0:
                quotient_a = quotient_a / i
                quotient_b = quotient_b / i
                # print(i, quotient_a, quotient_b)
                lst.append(i)
                break
        if i == 10000:
            lst.append(quotient_a)
            lst.append(quotient_b)
            break
    for j in lst:
        result *= j
    return int(result)

import sys

A, B = map(int, sys.stdin.readline().split())
print(gcf(A, B))
print(lcm(A, B))
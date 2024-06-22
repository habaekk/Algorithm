# 두 일차 방정식의 해

import sys
input = sys.stdin.read
a, b, c, d, e, f = map(int, input().split())

D = a*e - b*d
Dx = c*e - b*f
Dy = a*f - c*d

if D != 0:
    x = Dx // D
    y = Dy // D
    print(x, y)
else:
    print("No unique solution")

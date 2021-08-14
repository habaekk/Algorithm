a, b, c = map(int, input().split())
reward = 0
if a == b and b == c:
    reward = 10000 + a*1000
elif a == b or a == c:
    reward = 1000 + 100*a
elif b == c:
    reward = 1000 + 100*b
else:
    if a >= b and a >= c:
        reward = a * 100
    elif b >= a and b >= c:
        reward = b * 100
    else:
        reward = c * 100
print(reward)
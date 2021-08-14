a, b, c = map(int, input().split())
i = 0.0001
while True:
    if a**2 <= (i*b)**2 + (i*c)**2:
        break
    i += 0.0001

print(int(i*b), int(i*c))
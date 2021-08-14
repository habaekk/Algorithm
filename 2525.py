H, M = map(int, input().split()) #HH MM
t = int(input()) # time needed

M += t

while H >= 24 or M >= 60:
    if M >= 60: #adjust minute
        M -= 60
        H += 1
        if H >= 24: #adjust hour
            H -= 24
print(H, M)
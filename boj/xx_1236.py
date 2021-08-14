h, w = map(int, input().split())
n_guards = 0
lst = []

for k in range(h):
    lst.append(list(input()))
ww = 0
for i in range(h):
    checka = True
    checkb = True
    for j in range(w):
        if lst[i][j] == 'X':
            checka = False
        if lst[j][i] == 'X':
            checkb = False
    if (checka and checkb) == True:
        n_guards += 1
        lst[i][ww] = 'X'
        i = 0
    ww+=1

ww = 0
for i in range(h):
    checka = True
    checkb = True
    for j in range(w):
        if lst[i][j] == 'X':
            checka = False
        if lst[j][i]:
            checkb = False
    if (checka or checkb) == True:
        n_guards += 1
        i = 0
    ww += 1

print(n_guards)
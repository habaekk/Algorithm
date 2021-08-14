N = int(input())
lst = []
result = 0
check = False

for i in range(1, N+1):
    result = 0
    s = i.__str__()
    lst = list(s)
    for j in range(len(lst)):
        result += int(lst[j])
    result += i
    if result == N:
        print(i)
        check = True
        break
if check == False:
    print(0)
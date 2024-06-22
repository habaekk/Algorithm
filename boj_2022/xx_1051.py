N, M = map(int, input().split())
lst = []
for i in range(N):
    lst.extend((list(input())))
smaller = min(N, M)
bigger = max(N, M)
max_size = 0
check = False

for side in range(2, smaller+1):
    for i in range(N*M):
        check = False

        row = ((i+1) // M) + 1
        if ((i+1) % M == 0):
            row -= 1
        col = (i+1) % M
        if col == 0:
            col = M
        if side > N - row + 1:
            break
        elif side > M - col + 1:
            continue
        current_num = lst[i]
        if current_num == lst[i+side-1]:
            if current_num == lst[i+side-1]:
                if current_num == lst[i+M*(side-1)+side-1]:
                    check = True
        if check == True:
            current_size = side**2
            if current_size >= max_size:
                max_size = current_size

print(max_size)
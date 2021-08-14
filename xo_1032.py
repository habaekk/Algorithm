N = int(input())
lst = []
for i in range(N):
    string = input()
    lst.append(list(string))
result = ""
if N == 1:
    print(string)
else:
    for i in range(len(lst[0])):
        for j in range(1, N):
            check = 0
            if lst[0][i] != lst[j][i]:
                result += "?"
                check = 1
                break
        if check == 0:
            result += lst[0][i]

    print(result)

    # N == 1
    # 조건 보고 모든 경우 생각하기
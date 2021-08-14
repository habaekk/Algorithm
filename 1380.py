j = 1
while(True):
    names = []
    nums = []
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        name = input()
        names.append(name)
    for i in range(2 * n - 1):
        num, temp = input().split()
        num = int(num)
        nums.append(num)
    for i in range(1, 1000):
        cc = nums.count(i)
        if cc == 1:
            result_index = i - 1
    print(j, names[result_index])
    j += 1
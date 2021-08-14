Num_list = []
Num_list = map(int, input().split())
sum = 0
for i in Num_list:
    sum += i ** 2
print(sum % 10)
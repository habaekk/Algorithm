n = int(input())
  
fibo = [0, 1, 1]
for i in range(3, 999):
    fibo.append(fibo[i-1]+fibo[i-2])

lst = []
while True:
    target = 0
    for j in range(1, 999):
        f = fibo[j]
        if f == n:
            target = j
        if f > n:
            target = j - 1
            break
    lst.append(target)
    n -= fibo[target]
    if n == 0:
        break

sum = 0
for i in lst:
    sum += fibo[i-1]
print(sum)

			


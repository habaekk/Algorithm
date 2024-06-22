from sys import stdin
input = stdin.readline

s = input()
ans = 0
temp = ""
mn = False
for i in s:
    try:
        int(i)
        temp += i
    except ValueError:
        if mn == True:
            ans -= int(temp)   
        elif i == '-':
            mn = True
            ans += int(temp)
        else:
            ans += int(temp)
        temp = ""
print(ans)

# 더 쉬운 풀이 있음
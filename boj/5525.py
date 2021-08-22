from sys import stdin
input = stdin.readline

n = int(input())
m = int(input())
S = input()
s1 = ""
s2 = ""

pn = "IOI" + ("OI" * (n-1))
lpn = list(pn)
spn = list(S)
cnt = 0

for i in range(len(S) - len(pn)):
    if lpn == spn[i:i+len(pn)]:
        cnt += 1
print(cnt)
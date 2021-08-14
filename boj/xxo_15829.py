L = int(input())
S = list(input())
M = 1234567891
r = 31
sum = 0
for i in range(len(S)):
    sum += ((ord(S[i]) - 96) * r ** (i))
    sum = sum % M
print(sum)

# Hash
# Mod M
# %
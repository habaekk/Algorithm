import sys
lst1 = []
lst2 = []

N = int(sys.stdin.readline())

for i in range(N):
    a, b = sys.stdin.readline().split()
    lst1.append(int(a))
    lst2.append(b)
for i in range(1, 201):
    for j in range(len(lst1)):
        if lst1[j] == i:
            print(lst1[j], lst2[j])

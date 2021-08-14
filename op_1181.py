N = int(input())
lst1 = []
lst2 = []
prev = ""

for i in range(N):
    lst1.append(input())

for i in range(1, 51):
    lst2 = []
    for j in range(N):
        if (len(lst1[j]) == i):
            lst2.append(lst1[j])
    lst2.sort()
    for k in range(len(lst2)):
        current = lst2[k]
        if (current != prev):
            print(current)
        else:
            pass
        prev = current

# import sys
# input = sys.stdin.readline

# n = int(input())
# words = []


# for _ in range(n):
#     word = input().rstrip()
#     if word not in words:
#         words.append(word)

# words.sort(key=lambda x: (len(x), x))

# for word in words:
#     print(word)
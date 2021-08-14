import sys
N = int(sys.stdin.readline())
lst = []
for _ in range(N):

    s = sys.stdin.readline()
    if s.__contains__(" "):
        s, n = s.split(" ")
    print(s)
    if n:
        print(n)
from sys import stdin
input = stdin.readline

M = int(input())
st = set([])
for _ in range(M):
    s = input().strip("\n")
    if s == "all":
        st = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'}
    elif s == "empty":
        st.clear()
    else:
        s, n = s.split()
        if s == "add":
            st.update(n)
        elif s == "remove":
            st.discard(n)
        elif s == "check":
            if st.__contains__(n):
                print(1)
            else:
                print(0)
        elif s == "toggle":
            if st.__contains__(n):
                st.remove(n)
            else:
                st.update(n)
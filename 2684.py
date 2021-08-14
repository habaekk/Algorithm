P = int(input())
A = []
for i in range(P):
    a = 0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    A = list(input())
    for j in range(38):
        check = ""
        check = A[j] + A[j+1] + A[j+2]
        if check == "TTT":
            a += 1
    for j in range(38):
        check = ""
        check = A[j] + A[j+1] + A[j+2]
        if check == "TTH":
            b += 1
    for j in range(38):
        check = ""
        check = A[j] + A[j+1] + A[j+2]
        if check == "THT":
            c+= 1
    for j in range(38):
        check = ""
        check = A[j] + A[j+1] + A[j+2]
        if check == "THH":
            d+= 1
    for j in range(38):
        check = ""
        check = A[j] + A[j+1] + A[j+2]
        if check == "HTT":
            e += 1                    
    for j in range(38):
        check = ""
        check = A[j] + A[j+1] + A[j+2]
        if check == "HTH":
            f += 1
    for j in range(38):
        check = ""
        check = A[j] + A[j+1] + A[j+2]
        if check == "HHT":
            g += 1
    for j in range(38):
        check = ""
        check = A[j] + A[j+1] + A[j+2]
        if check == "HHH":
            h += 1                        
    print(a, b, c, d, e, f, g, h)
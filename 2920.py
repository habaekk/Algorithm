p1, p2, p3, p4, p5, p6, p7, p8 = map(int, input().split())

if (p1 < p2 and p2 < p3 and p3 < p4 and p4 < p5 and p5 < p6 and p6 < p7 and p7 < p8):
    print("ascending")
elif (p1 > p2 and p2 > p3 and p3 > p4 and p4 > p5 and p5 > p6 and p6 > p7 and p7 > p8):
    print("descending")    
else:
    print("mixed")
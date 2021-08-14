oxta = input()
answer = ""
c = 0
for i in oxta:
    i = int(i)
    if c == 0:
        if i == 7:
            answer +="111"
        elif i == 6:
            answer +="110"
        elif i == 5:
            answer +="101"
        elif i == 4:
            answer +="100"
        elif i == 3:
            answer +="11"
        elif i == 2:
            answer +="10"
        elif i == 1:
            answer +="1"
        elif i == 0:
            answer +="0"
    else:
        if i == 7:
            answer +="111"
        elif i == 6:
            answer +="110"
        elif i == 5:
            answer +="101"
        elif i == 4:
            answer +="100"
        elif i == 3:
            answer +="011"
        elif i == 2:
            answer +="010"
        elif i == 1:
            answer +="001"
        elif i == 0:
            answer +="000"
    c += 1
print(answer)
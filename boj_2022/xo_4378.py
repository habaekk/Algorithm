def correction(word):
    lst1 = ["W", "E", "R", "T", "Y", "U", "I", 'O', 'P', '[', ']', '\\', 'S','D','F','G','H','J','K','L',';','\'', 'X','C','V','B','N','M',',', '.', '/', '1','2','3','4','5','6','7','8','9','0','-','=']
    lst2 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']' , 'A','S','D','F','G','H','J','K','L', ';', 'Z','X','C','V','B','N','M', ',', '.','`','1','2','3','4','5','6','7','8','9','0','-']
    for i in range(len(lst1)):
        if word == lst1[i]:
            return lst2[i]
        elif word == " ":
            return " "

while True:
    try:
        sentence = input()
        result = ""
        for i in sentence:
            result += correction(i)
        print(result)
    except:
        break

# try except 으로 풀어도 되나??
# 파이선에선 여러줄을 받아서 다음 줄이 있으면 ~ 실행 이런 구문은 안되나?
# sys.stdin?
# strip?
# split("\n)??
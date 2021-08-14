def yun(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def date_cal(date, month, year):
    if yun(year) == True:
        if month == 1:
            return date
        elif month == 2:
            return 31 + date
        elif month == 3:
            return 31 + 29 + date
        elif month == 4:
            return 31 + 29 + 31 + date
        elif month == 5:
            return 31 + 29 + 31 + 30 + date
        elif month == 6:
            return 31 + 29 + 31 + 30 + 31 + date
        elif month == 7:
            return 31 + 29 + 31 + 30 + 31 + 30 + date
        elif month == 8:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + date
        elif month == 9:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + date
        elif month == 10:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + date
        elif month == 11:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + date
        else:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + date 
    else:
        if month == 1:
            return date
        elif month == 2:
            return 31 + date
        elif month == 3:
            return 31 + 28 + date
        elif month == 4:
            return 31 + 28 + 31 + date
        elif month == 5:
            return 31 + 28 + 31 + 30 + date
        elif month == 6:
            return 31 + 28 + 31 + 30 + 31 + date
        elif month == 7:
            return 31 + 28 + 31 + 30 + 31 + 30 + date
        elif month == 8:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + date
        elif month == 9:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + date
        elif month == 10:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + date
        elif month == 11:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + date
        else:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + date 

while True:
    D, M, Y = map(int, input().split())
    if Y == 0:
        break
    else:
        print(date_cal(D, M, Y))
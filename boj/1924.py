x, y = map(int, input().split())

DAYS = ("SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT")

def dayIndex(d):
    return d % 7

o = 31
e = 30
t = 28

if x == 1:
    i = dayIndex(y)
elif x == 2:
    i = dayIndex(o+y)
elif x == 3:
    i = dayIndex(o+t+y)
elif x == 4:
    i = dayIndex(o+t+o+y)
elif x == 5:
    i = dayIndex(o+t+o+e+y)
elif x == 6:
    i = dayIndex(o+t+o+e+o+y)
elif x == 7:
    i = dayIndex(o+t+o+e+o+e+y)
elif x == 8:
    i = dayIndex(o+t+o+e+o+e+o+y)
elif x == 9:
    i = dayIndex(o+t+o+e+o+e+o+o+y)
elif x == 10:
    i = dayIndex(o+t+o+e+o+e+o+o+e+y)
elif x == 11:
    i = dayIndex(o+t+o+e+o+e+o+o+e+o+y)
elif x == 12:
    i = dayIndex(o+t+o+e+o+e+o+o+e+o+e+y)

print(DAYS[i])
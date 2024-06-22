def isInCircle(x, y, cx, cy, r): # check if x, y in circle
    if (x-cx)**2 + (y-cy)**2 <= r**2:
        return True
    else:
        return False

def inCircleListMaker(x, y, cx, cy, r, lst):
    lst.append(isInCircle(x, y, cx, cy, r))
    return lst

def orbitInOutCalculator(num_circle, lst1, lst2):
    orbit = 0
    for i in range(num_circle):
        if lst1[i] != lst2[i]:
            orbit += 1
    return orbit


N = int(input())
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    n_circles = int(input())
    lst_start = []
    lst_end = []
    for i in range(n_circles):
        c_x, c_y, rad = map(int, input().split())
        lst_start = inCircleListMaker(x1, y1, c_x, c_y, rad, lst_start)
        lst_end = inCircleListMaker(x2, y2, c_x, c_y, rad, lst_end)
    result = orbitInOutCalculator(n_circles, lst_start, lst_end)
    print(result)
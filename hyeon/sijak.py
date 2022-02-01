import random

EPOCH = 10
object1 = 1

reproductionRate = 0.9
eliminationRate = 0.5

def reproduction(num2):
    rand = random.random()
    if rand < reproductionRate:
        num2 += 1

    return num2
    
def elimination(num2):
    rand = random.random()
    if rand < eliminationRate:
        num2 -= 1

    return num2

def selfReproduction(num):
    num = reproduction(num)
    num = elimination(num)
    
    return num
    


for _ in range(EPOCH):
    for __ in range(object1):
        object1 = selfReproduction(object1)
    print(object1)
import sys

n = int(sys.stdin.readline())
lst1 = []
stackLst = []
popPushLst = []
lstInput = []
isNo = True
temp = 0
for _ in range(n):
    lstInput.append(int(sys.stdin.readline()))
for i in range(1, n+1):
    lst1.append(i)
targetIndex = 0
while True:
    if len(lst1) == 0 and len(stackLst) == 0:
        isNo = False
        break
    target = lstInput[targetIndex]
    if len(stackLst) != 0:
        if stackLst[-1] == target:
            stackLst.pop()
            targetIndex += 1
            popPushLst.append("-")
        else:
            while temp < target:
                temp = lst1.pop(0)
                stackLst.append(temp)
                popPushLst.append("+")
            if stackLst[-1] != target:
                isNo = True
                break
    else:
        while temp < target:
            temp = lst1.pop(0)
            stackLst.append(temp)
            popPushLst.append("+")
        if stackLst[-1] != target:
            isNo = True
            break
if isNo == True:
    print("NO")
else:
    for pm in popPushLst:
        print(pm)
while(True):
    iinput = input()
    lst = list(iinput)
    if iinput == "0":
        break

    rev_lst = list(reversed(lst))
    
    check = True

    for i in range(len(lst)):
        if lst[i] != rev_lst[i]:
            check = False
    
    if check == False:
        print("no")
    
    else:
        print("yes")
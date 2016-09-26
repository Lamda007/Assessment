count = 0
while True and count < 17:
    x = int (input("enter your age please or Zero to quit: "))
    count = count + 1
    if x == 0:
        break
    if count == 17 and x != 24:
            x = int (input("enter your real age please or Zero to quit: "))
    if x >= 18 and x < 90:
        print ("welcome in")
    else:
        print ("you're not eligable")

for row in range(5):
    for col in range(3):
        if row==0 or row==2 or col==0 or col==2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
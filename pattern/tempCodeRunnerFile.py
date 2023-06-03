n=int(input("enter the number"))
k=2
for a in range(1,n+1):
    for col in range(1,n*2):
        if a+col==n+1 or col-a==n-1:
            print("*",end="")
        elif a==n and col!=k:
            k=k+2
            print("*",end="")
        else:
            print(end=" ")
    print()
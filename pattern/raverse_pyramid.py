n=int(input("enter the number"))
for i in range(n,0,-1):
    for col in range(0,n-i):
        print(end=" ")
    for col in range(0,i):
        print("*",end=" ")
    print()

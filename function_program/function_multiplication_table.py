def table(n):
    if n<0:
        print("retry")
    else:
        for i in range(10):
            print(n,"x",i+1,"=",n*(i+1))
n=int(input("enter the number:"))
table(n)

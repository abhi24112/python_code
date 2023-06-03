def great(a,b,c):
    if a>b and a>c:
         return a
    elif b>a and b>c:
        return b
    else:
        return c
print("insert only different number")
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
z=great(a,b,c)
print(z,"is the greatest number")


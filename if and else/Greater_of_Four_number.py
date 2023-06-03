#Greater of Four number

a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
d=int(input("enter the fourth number"))
if a>b:
    f1=a
else:
    f1=b
if c>d:
    f2=c
else:
    f2=d
if f1>=f2:
    print("this is a greatest number:",f1)
else:
    print("this is a greatest number:",f2)

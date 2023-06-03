a=int(input("enter the first subject marks"))
b=int(input("enter the second subject marks"))
c=int(input("enter the third subject marks"))
if a<33 and b<33 and c<33:
    print("you are fail")
elif (a+b+c)/3>=40:
    print("your are pass")
else:
    print("you are pass")

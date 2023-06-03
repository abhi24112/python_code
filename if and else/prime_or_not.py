num=int(input("enter the number "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            a=True 
            break
    if a:
        print("it is not a prime number")
    else:
        print("it is a prime number")
else:
    print("it is not a prime number")
    

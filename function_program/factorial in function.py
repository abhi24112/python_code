def fact(x):
    j=1
    res=1
    while j<=x:
        res=res*j
        j=j+1
    return res
n=int(input("enter the number : "))
i=0
sum=1
while i<=n:
    f=fact(i)
    sum=sum+1/f
    i+=1 

print(sum)

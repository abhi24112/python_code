l=eval(input("Enter the number :"))
leng=len(l)
sum=0
for a in range(leng):
    sum+=l[a]
mean=sum/leng
print("Mean of  the list is :",mean)
def sum(z):
    total=0
    for a in z:
        total+=a
    return total
n=eval(input("enter the number"))
q=sum(n)
print("sum is:",q)
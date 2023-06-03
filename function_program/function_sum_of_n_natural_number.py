def sum(a):
    if a<=1:
        return a
    else:
        return a + sum(a-1)
n=int(input("enter the number:"))
z=sum(n)
print(z)
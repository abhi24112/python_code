def reverse(a):
    index = len(a)
    string=''
    while index>0:
        string+=a[index-1]
        index=index-1
    return string
p=input("enter the string:")
z=reverse(p)
print("reverse of ",p,"is",z)
def search(item,lst):
    for a in range(10):
        if lst[a]==item:
            return a
n=input("enter the number for search:")
list=[1,2,3,4,5,678,9,35,578,45]
z=search(n,list)
if z==None or z==0:
    print("number is not found")
else:
    print("number is found at index:",z)

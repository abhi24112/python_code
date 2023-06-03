l=eval(input("Enter the number :"))
leng=len(l)
min_ele=l[0]
index=0
for a in range(1,leng):
    if min_ele>l[a]:
        min_ele=l[a]
        index=a
print("Given list is:",l)
print("Minimum element is ",min_ele,"at index ",index)


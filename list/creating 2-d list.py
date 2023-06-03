l=[]
r=int(input("how many rows?"))
c=int(input("how many column?"))
for i in range(r):
    row=[ ]
    for j in range(c):
        ele=int(input("enter the list element:"))
        row.append(ele)
    l.append(row)
print("list created is:",l)

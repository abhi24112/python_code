l=eval(input("Enter the list :"))
s=int(input("Enter the  search number:"))
leng=len(l)
for a in range(leng):
    if l[a]==s:
        break
print("Search elemet is found at index:",a)

s=[]
for i in range (5):
    a=int(input("Enter the element:"))
    s.append(a)
print(s)
s[1]=6
s.append(7)
s.pop(5)
print(s)
def rev(s):
    length=len(s)
    stack=[]
    for i in range (0,length):
        stack.append(s[i])
    s=""
    for i in range (0,length):
        s+=stack.pop()
    return s
s=input("enter the string:")
rs=rev(s)
print("reverse of the string is:",rs)

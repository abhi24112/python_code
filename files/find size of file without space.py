f1=open("abhi.txt","r")
s=" "
size=0
tsize=0
while s:
    s=f1.readline()
    tsize=tsize+len(s)
    size=size+len(s.strip())
print("size of file : ",size)
print("total size of file : ",tsize)
f1.close()


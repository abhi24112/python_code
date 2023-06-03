f=open("abhi.txt","r")
str=" "
while str:
    str=f.readline()
    if str[0]=='p':
        print(str)
f.close()
    

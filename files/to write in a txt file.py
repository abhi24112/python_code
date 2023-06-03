f=open("myfiel.txt","w")
while f:
    line=input("enter the line:")
    f.writelines(line)
    option=input("If you want write one more line so||press ->y|| if you want to close ||press ->n||:")
    if option=='y':
        continue
    if option=='n':
        break
f.close()

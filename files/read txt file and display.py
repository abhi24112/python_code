def read():
    f=open("abhi.txt","r")
    str=" "
    while str:
        str=f.readline()
        print(str)
    f.close()

a=open("poem.txt","r")
b=a.read()
if "twinkle" in b:
    print("yes twinkle is present in poem.txt")
else:
    print("no twinkle is not present in poem.txt")
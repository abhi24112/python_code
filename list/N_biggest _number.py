l=eval(input("Enter the number :"))
n=int(input("Enter the number :"))
l.sort()
length=len(l)
for a in range(n):
    print(a+1,"bigest number is",l[(n+1)-length-a])

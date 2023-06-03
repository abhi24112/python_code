print("-------for celsius to fahrenheit press y-------")
print("-------for fahrenheit to celsius press n-------")
n=input("enter your choise:")
if n=="y":
    def fah(a):
        f=(a*9/5)+32
        print(f,"fahrenheit")
    c=int(input("enter the celsius value:"))
    fah(c)
elif n=="n":
    def fah(f):
        b=(f-32)*5/9
        print(b,"celsius")
    c=int(input("enter the fahrenheit value:"))
    fah(c)
else:
    print("your choise is not available")









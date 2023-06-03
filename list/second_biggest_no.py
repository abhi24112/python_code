n=eval(input("Enter the number:"))
s=set(n)
s.remove(max(s))
print(max((s)))
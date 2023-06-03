# Dictionary to translate hindi to english

a={"Namaste":"hello","panni":"Water","agg":"fire"}
print("****you can see the translation of these words only***")
print(a.keys())
s=input("enter the word:")
f=a[s] #we can also use  get function f=a.get(s)
print("The translation of",s,"is",f)
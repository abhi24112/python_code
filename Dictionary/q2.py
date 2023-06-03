''' Crete a empty dict and  allow 4 friend to enter their favourite language as a value
and their name as  a key and print the dictionary'''

d={}
for i in range(4):
    key=input("Enter your name:")
    value=input("Enter your favourite language:")
    d.setdefault(key,value)
print(d)

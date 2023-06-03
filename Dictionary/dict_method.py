a={"Name":"Abhishek", "class":"btech","roll_no":1}
new_dict={"id":3434,"roll_no":2}

print(a.keys())

print(a.values())

print(a.get("Name"))

a.update(new_dict)
print(a)

print(a.pop("roll_no"))

a.setdefault("real",2)
print(a)

a.setdefault("class")
print(a)

a.clear()
print(a)
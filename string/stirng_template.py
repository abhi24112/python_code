# using replace 

letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
'''

print(letter)
a=input("Enter your name:")
b=input("Enter the date:")

letter=letter.replace("<|NAME|>",a)
letter=letter.replace("<|DATE|>",b)
print(letter)
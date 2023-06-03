#Spam detector

a=input("enter the content:")
if "make a lot of money" in a:
    spam=True
if "buy now" in a:
    spam=True
if "subscribe this " in a:
    spam=True
if "click this" in a:
    spam=True
else:
    spam=False
if spam:
    print("it is a spam")
else:
    print("it is not a spam")

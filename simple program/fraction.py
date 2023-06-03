# Factional values 

from fractions import Fraction
x=int(input("Enter the number :"))
y=int(input("Enter the nubmer :"))
f=Fraction(x,y)
print(f)
print(f.numerator)
print(f.denominator)
print(f.as_integer_ratio)
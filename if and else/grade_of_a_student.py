#write a progrme to calculate a grade of a student
#90-100-->A+
#80-90 --> A
#70-80 -->B
#60-70 -->C
#50-60 -->D
#50-60 -->E
#<50 --F

a=input("Enter the name of the student:")
n=int(input("Enter the marks"))
if n>=90:
    grade="A+"
elif n>=80:
    grade="A"
elif n>=70:
    grade="B"
elif n>=60:
    grade="C"
elif n>=50:
    grade="D"
else:
    grade="F"
print(a,"your grade is:",grade)

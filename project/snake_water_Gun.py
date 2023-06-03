import random
def game(a,b):
    if a==b:
        return None
    elif a=='s':
        if b=='w':
            return False
        elif b=='g':
            return True
    elif a=='w':
        if b=='g':
            return False
        elif b=='s':
            return True
    elif a=='g':
        if b=='s':
            return False
        elif b=='w':
            return True
print("computer trun choise in b/w snake,water & gun?")
computer=random.randint(1,3)
if computer==1:
    comp='s'
elif computer==2:
    comp='w'
else:
    comp='g'
player=input("your turn choise in b/w Snake(s),Water(w) & Gun(g)?")
z=game(comp,player)

print("computer choise is:",comp)
print("your choise is:",player)
if z==None:
    print("Match is tie!")
elif z:
    print("You Win!")
else:
    print("You lose!")




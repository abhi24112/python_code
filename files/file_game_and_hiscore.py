def game(n):
    return n
n=int(input("entre the high score: "))
hiscore=game(n)
with open("hiscore.txt","r") as f:
    score=f.read()
if score=='':
    with open("hiscore.txt","w") as f:
        f.write(str(hiscore))
    print('you make a first high score')
elif int(score)<hiscore:
    with open("hiscore.txt","w") as f:
        f.write(str(hiscore))
    print("you make an high score")
else:
    print("you don't make a hiscore")


 
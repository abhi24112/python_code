'''program to print elements of a list ['q','w','e','r','t','y'] 
in seperate lines along with elements both indexes (+ve and -ve)'''


lst=['q','w','e','r','t','y']
l=len(lst)
for a in range(l):
    print("At index",a,"and",(a-l),":",lst[a])

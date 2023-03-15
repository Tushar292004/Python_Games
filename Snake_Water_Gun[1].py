import random

def gamewin(comp, you):
    if comp == you:
        print("TIE")
    elif comp == "s":
        if you == "g":
            print("You won")
        else :
            print("Computer won")

    elif comp == "w":
        if you == "s":
            print("You won")
        else :
            print("Computer won")

    elif comp == "g":
        if you == "w":
            print("You won")
        else :
            print("Computer won") 

    else :
        print("wrong choice")                       
                





you = input("yoyr turn : Snake(s) Water(w) Gun(g)? ")


print(("compuer's turn : Snake(s) Water(w) Gun(g)? " ))
r = random.randint(1, 3)

if r == 1:
    comp = 's'
elif r == 2:
    comp = 'w'
elif r==3 :
    comp = 'g'


print(f"computer chose {comp}")
print(f"you chose {you}")




gamewin(comp, you)

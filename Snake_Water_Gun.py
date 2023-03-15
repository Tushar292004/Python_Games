import random  #neccessary to genrate random option by computer

#function will cehck the result
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
                
#users choice
you = input("your turn : Snake(s) Water(w) Gun(g)? ")

print(("compuer's turn : Snake(s) Water(w) Gun(g)? " ))

#computer will choice from number 1 to number 3 
r = random.randint(1, 3) 

#on the basis of random number the choice will be assigned for the computer
if r == 1:
    comp = 's'
elif r == 2:
    comp = 'w'
elif r==3 :
    comp = 'g'


print(f"computer chose {comp}")
print(f"you chose {you}")

#calling resukt checking function
gamewin(comp, you)

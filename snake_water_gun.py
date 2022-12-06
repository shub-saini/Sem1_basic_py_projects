import random

choice=["s","w","g"]

listind=random.randint(0,2)
comp=choice[listind]
print("Choose either s, w or g")
user=input("Your input -")

if user in choice:
    if user!=comp:
        if user=="s" and comp=="w":
            print("You Won")
        elif user=="g" and comp=="s":
            print("You Won")
        elif user=="w" and comp=="g":
            print("You Won")
        else:
            print("You Lost")
        print("computer -",comp)
    else:
        print("Both picked the same option\n Try again!")
        print("Computer -",comp)
else:
    print("Please enter a valid input \nTry again!")
    

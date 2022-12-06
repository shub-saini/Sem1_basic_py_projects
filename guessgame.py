import random
number=random.randint(1,101)
attempt=1
guess=int(input("Your guess: "))
while(True):
    if number>guess:
        guess=int(input("your guess is too low. Try one more guess: "))
        attempt+=1
    elif number <guess:
        guess=int(input("your guess is too high. Try one more time: "))
        attempt+=1
    else:
        print(f"Correct! the right number is {number}. You have taken {attempt} attempts")
        break
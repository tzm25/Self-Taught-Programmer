import random
number=random.randint(0,5)
guess=int(input("I'm thinking about a number between zero and ten. Can you guess it? "))

while True:
    if guess==number:
        break
    else:
        guess=int(input("Sorry! Try again. "))


print("Congraculations!! You got it.")
        

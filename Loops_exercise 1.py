import random
guess=["red", "yellow", "green", "paleblue", "orange", "black", "brown"]

print("Here is the names of the some colors: ", guess)

while True:
    color=guess[random.randint(0,len(guess)-1)]
    user=input("I'm thinking about a color, can you guess it: ")

    while True:
        if(color == user.lower()):
            break
        else:
            user=input("Nope, try again: ")

    print("Congraculations! You guessed it.")
    
    again=input("Let's play again?Type 'no' to quit.")
    
    if again.lower()=="no":
        break

print("It was fun.Thanks for playing game.")

    

list_ = [0,5,19,26,39,29,47,49,43,32]

while True:
    print("Type q to quit.")
    usr = input("Please guess a number between 0 to 50: ")
    if usr == "q":
        break
    if int(usr) in list_ :
        print("Congraculations! You guessed.")
    if int(usr) not in list_:
        print("Sorry!You are wrong.")
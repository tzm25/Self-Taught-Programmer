qs = ["What's your name?", "What's your favourite color?","What's your favourite food"]

n = 0

while True:
    print("Type q to quit:")
    a= input(qs[n])
    if a == "q":
        break
    n = (n+1)/3
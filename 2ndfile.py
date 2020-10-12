

def maximum(First_Number,Second_Number,Third_Number):
    if (First_Number >= Second_Number) and (First_Number >= Third_Number):
        max_num = First_Number
    elif (Second_Number >= First_Number) and (Second_Number >= Third_Number):
        max_num = Second_Number
    else:
        max_num = Third_Number
    return max_num

First_Number = int(input("Please type a number: "))
print ("Your first number is", First_Number)
Second_Number = int(input("Please type a number again: "))
print ("Your second number is", Second_Number)
Third_Number = int(input("Again type a number please: "))
print ("And your third number is:", Third_Number)

print("The maximum number is" ,maximum(First_Number,Second_Number,Third_Number))
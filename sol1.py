import random
balance = 1000 
round = ["1", "1", "0", "0", "1"]
ls = random.choice(round)
for i in ls:
	if i=="1":
		win_bal = balance + 100
		print("Congraculations!You won.Your balance is", win_bal)

		
	elif i=="0":
		lose_bal= balance - 100
		print("Sorry!You lost.Your balance is", lose_bal)
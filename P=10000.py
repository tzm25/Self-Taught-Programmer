import math

P=10000
r=float(0.08)
n=12
print("P = 1000")
print("r = 0.08")
print("n = 12")
t= int(input("Please insert number of years 't': "))

A =  P*((1+r/n)**(n*t))

print ("The final amount after t years is",round(A,3))
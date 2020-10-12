print("BMI(body mass index) of a person")

height=float(input("Please type your height in meters: "))
weight=float(input("Please type your weight in kg: "))

BMI=(round((weight/(height**2)),1))
print("Body mass index: ", BMI)

if(BMI<=18.5):
    classificaton="Underweight"

elif(BMI>18.5 and BMI<=24.9):
    classification="Normal Weight"

elif(BMI>24.9 and BMI<=24.9):
    classification="Overweight"

else:
    classification="obesity"

print("The classification of your BMI is: ", classification)

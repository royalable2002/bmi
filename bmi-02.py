# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

#It should tell them the interpretation of their BMI based on the BMI value.

#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.

height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))

bmi_as_int = round(weight / height ** 2)

if bmi_as_int < 18.5:
    print(f"your BMI is {bmi_as_int}, you are underweight.")
elif bmi_as_int < 25:
    print(f"your BMI is {bmi_as_int}, you have a normal weight.")
elif bmi_as_int < 30:
    print(f"your BMI is {bmi_as_int}, you are slightly overweight.")  
elif bmi_as_int < 35:
    print(f"your BMI is {bmi_as_int}, you are obese.") 
else:
    print(f"your BMI is {bmi_as_int}, you are clinically obese.")        




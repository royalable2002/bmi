# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# BMI = Weight / Height ** 2

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int(weight) / float(height) ** 2

bmi_as_int = int(bmi)
print(bmi_as_int)

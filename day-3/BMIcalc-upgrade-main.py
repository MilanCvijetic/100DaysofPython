# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int (weight) // float (height)**2
bmi_as_int=int (bmi)
print(bmi_as_int)

if bmi_as_int <= 18.5:
    print(f"Your BMI is {bmi_as_int}, you are underweight.")
elif bmi_as_int <= 25:
    print(f"Your BMI is {bmi_as_int}, you have a normal weight.")
elif bmi_as_int <= 30:
    print(f"Your BMI is {bmi_as_int}, you are slightly overweight.")
elif bmi_as_int <= 35:
    print(f"Your BMI is {bmi_as_int}, you are obese.")
else:
    print(f"Your BMI is {bmi_as_int}, you are clinically obese.")

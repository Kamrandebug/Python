# BMI Calculator
# Ask the user to enter their weight (kg) and height (meters). Calculate BMI and print the result
# Below 18.5 → "Underweight"
# 18.5 to 24.9 → "Normal"
# 25 and above → "Overweight"

weight = int(input("Enter Your Weight : "))
hight = float(input("Enter Hight in Meters : "))

bmi = weight / hight ** 2

if bmi < 18.5:
  print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
  print("Normal")
elif bmi >= 25:
  print("Overweight")

# Weekday or Weekend
# Ask the user to enter a day number (1–7). Print whether it is a weekday or weekend.
# (1–5 weekday, 6–7 weekend)

number = int(input("Enter any day number from 1 to 7 : "))

if number >= 1 and number <= 5:
    print("Its a week day")
elif number == 6 or number == 7:
    print("Its a Weekend day")
else:
    print("Invalid Number")
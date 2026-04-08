# Leap Year
# Ask the user to enter a year. Print whether it is a leap year or not.
# (Hint: A year is leap if it is divisible by 4)

year = int(input("Enter an year : "))


if year % 4 == 0 :
 print("This is a leap Year")
else:
 print("Its not a leap Year")
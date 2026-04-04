# ============================================================
#  PYTHON COURSE — Chapter 5: if / elif / else
# ============================================================
# Conditional statements let your program make decisions.
# Code inside a block only runs when its condition is True.
#
# Syntax:
#   if condition:
#       # runs when condition is True
#   elif another_condition:
#       # runs when the above is False but this is True
#   else:
#       # runs when ALL conditions above are False
#
# ⚠️ Indentation (4 spaces) defines the block — no { } in Python!
# ============================================================


# ── Example 1: Basic if-else ─────────────────────────────────
# The simplest form — two possible paths: True or False.

a = 6

if a > 10:
    print("I will do task A")   # runs only if a > 10
else:
    print("I will do task B")   # runs when a is NOT > 10

# Output: I will do task B  (because 6 is not > 10)


# ── Example 2: elif Chain (Ice Cream Shop) ───────────────────
# Use elif when you have MORE than two possible outcomes.
# Python checks each condition top-to-bottom and stops at the first True.

money = int(input("Please enter the money you have: "))

if money == 10:
    print("You can have a Choco Bar ice cream 🍫")
elif money == 20:
    print("You can have a Mango Dolly 🥭")
elif money == 30:
    print("You can have a Frosty 🍦")
else:
    # None of the above matched — this is the default/fallback
    print("You can have a Cone 🍧")


# ── Example 3: Compare Two Numbers ───────────────────────────
# Demonstrates using variables from input inside conditions.

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    # Both conditions above were False — numbers must be equal
    print("Both numbers are the same")


# ── Example 4: Gender Greeting (or operator) ─────────────────
# A single condition can check multiple values using 'or'.

gen = input("Enter your gender (M or F): ")

if gen == 'M' or gen == 'm':    # accept both upper and lower case
    print("Good morning, Sir! 👨")
elif gen == 'F' or gen == 'f':
    print("Good morning, Ma'am! 👩")
else:
    print("Unidentified gender")


# ── Example 5: Even or Odd ───────────────────────────────────
# % (modulo) gives the remainder. If divisible by 2, remainder is 0.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an Even number")   # e.g. 4 % 2 = 0 → even
else:
    print(f"{num} is an Odd number")    # e.g. 7 % 2 = 1 → odd


# ── Example 6: Voting Eligibility ────────────────────────────
# Combining input + condition to simulate a real-world check.

name = input("Enter your name: ")
age  = int(input("Enter your age: "))

if age >= 18:
    print(f"Hello {name}, you are eligible to vote ✅")
else:
    print(f"Hello {name}, you are not eligible to vote ❌")
    print(f"You need {18 - age} more year(s).")


# ── Example 7: Leap Year ─────────────────────────────────────
# Leap year rules:
#   Rule 1: divisible by 400             → leap year
#   Rule 2: divisible by 100 (not 400)   → NOT a leap year
#   Rule 3: divisible by 4   (not 100)   → leap year
#   Otherwise → NOT a leap year
#
# We use 'and' to combine two conditions that must BOTH be True.

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a Leap Year 🗓️")
elif year % 100 == 0:
    print(f"{year} is NOT a Leap Year")
elif year % 4 == 0:
    print(f"{year} is a Leap Year 🗓️")
else:
    print(f"{year} is NOT a Leap Year")


# ── Example 8: Temperature Classifier ────────────────────────
# A long elif chain — Python exits as soon as one condition matches.

t = int(input("Enter the temperature (°C): "))

if t < 0:
    print("🥶 Freezing cold!")
elif t < 10:                      # we already know t >= 0 from above
    print("🧥 Very cold")
elif t < 20:                      # we already know t >= 10
    print("🌬️  Cold")
elif t < 30:                      # we already know t >= 20
    print("😊 Pleasant")
elif t < 40:                      # we already know t >= 30
    print("☀️  Hot")
else:                             # t >= 40
    print("🔥 Extremely hot!")


# ── Bonus: Nested if ─────────────────────────────────────────
# You can place an if statement inside another if block.
# Use sparingly — deeply nested code gets hard to read.

score = int(input("Enter your score (0-100): "))

if score >= 33:
    print("Result: PASS ✅")
    if score >= 90:
        print("Grade: A+")
    elif score >= 75:
        print("Grade: A")
    elif score >= 60:
        print("Grade: B")
    else:
        print("Grade: C")
else:
    print("Result: FAIL ❌")


# ── Bonus: Ternary (One-Line) Condition ──────────────────────
# Useful for simple True/False assignments in a single line.
# Syntax: value_if_true  if  condition  else  value_if_false

n = 7
result = "Even" if n % 2 == 0 else "Odd"
print(result)   # Odd


# ============================================================
#  Quick Recap
#  • if   → first condition to check
#  • elif → additional conditions (as many as you need)
#  • else → fallback when nothing above matched
#  • Indentation (4 spaces) defines the block
#  • Ternary: x = A if condition else B
# ============================================================

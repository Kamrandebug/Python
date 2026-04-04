# ============================================================
#  PYTHON COURSE — Chapter 7: While Loops
# ============================================================
# A while loop repeats a block of code AS LONG AS a condition is True.
# Use a while loop when you DON'T KNOW in advance how many times
# the loop should run.
#
# Syntax:
#   while condition:
#       # code to repeat
#       # ⚠️ always update the condition variable — or you'll loop forever!
# ============================================================


# ── Example 1: Print 1 to 30 ─────────────────────────────────
# Classic counter pattern: initialise → check → update

a = 1                  # Step 1: initialise

while a <= 30:         # Step 2: condition (runs while this is True)
    print(a, end=" ")
    a = a + 1          # Step 3: update (move toward ending the loop)
print()

# ⚠️ If you forget Step 3, the loop runs forever — an infinite loop!


# ── Example 2: Reverse a Number ──────────────────────────────
# We use % to extract the last digit and // to remove it.
# We don't know how many digits the number has → while loop fits.
#
# Example: 1234
#   rev=0*10 + 1234%10=4  → rev=4,   a=123
#   rev=4*10 + 123%10=3   → rev=43,  a=12
#   rev=43*10 + 12%10=2   → rev=432, a=1
#   rev=432*10 + 1%10=1   → rev=4321, a=0  → loop ends

a   = int(input("Enter a number to reverse: "))
rev = 0

while a > 0:
    rev = rev * 10 + a % 10   # build reversed number digit by digit
    a   = a // 10              # remove last digit

print(f"Reversed: {rev}")


# ── Example 3: Palindrome Number Check ───────────────────────
# Same reversal logic, but we compare with the original.

a    = int(input("Check palindrome number: "))
copy = a    # save original before we modify a
rev  = 0

while a > 0:
    rev = rev * 10 + a % 10
    a   = a // 10

if copy == rev:
    print(f"{copy} IS a palindrome number ✅")
else:
    print(f"{copy} is NOT a palindrome number ❌")


# ── Example 4: Sum of Digits ─────────────────────────────────
# Extract each digit and add it up.
# Example: 1234 → 1+2+3+4 = 10

num   = int(input("Find sum of digits of: "))
copy  = num
total = 0

while num > 0:
    total += num % 10    # add last digit to total
    num   //= 10          # drop last digit

print(f"Sum of digits of {copy} = {total}")


# ── Example 5: Count Digits ───────────────────────────────────
# How many digits does the number have?

num   = int(input("Count digits of: "))
count = 0

while num > 0:
    count += 1
    num   //= 10

print(f"Number of digits: {count}")


# ── Example 6: Strong Number (while + for) ───────────────────
# A strong number equals the sum of factorials of its digits.
# Example: 145 → 1! + 4! + 5! = 1 + 24 + 120 = 145 ✅

num  = int(input("Check strong number: "))
copy = num
total  = 0

while num > 0:
    digit = num % 10        # extract last digit
    fact  = 1
    for i in range(1, digit + 1):
        fact *= i           # calculate digit's factorial
    total += fact
    num //= 10

if total == copy:
    print(f"{copy} is a Strong Number 💪")
else:
    print(f"{copy} is NOT a Strong Number")


# ── Example 7: Number Guessing Game ──────────────────────────
# while True creates an infinite loop.
# We use break to exit when the correct guess is found.
# This is the RIGHT way to loop when you don't know how many tries it'll take.

import random

secret = random.randint(1, 10)   # generate a random number between 1 and 10
tries  = 0

print("\n🎮 Guessing Game — guess a number between 1 and 10")

while True:
    guess = int(input("Your guess: "))
    tries += 1

    if guess == secret:
        print(f"🎉 Correct! You guessed it in {tries} {'try' if tries == 1 else 'tries'}!")
        break            # exit the infinite loop
    elif guess < secret:
        print("📈 Too low! Go higher.")
    else:
        print("📉 Too high! Go lower.")


# ── Example 8: ATM PIN Validator ─────────────────────────────
# Give the user 3 chances to enter the correct PIN.

correct_pin = "1234"
attempts    = 3

while attempts > 0:
    pin = input("\nEnter your PIN: ")
    if pin == correct_pin:
        print("✅ Access granted! Welcome.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"❌ Wrong PIN. {attempts} attempt(s) remaining.")
        else:
            print("🔒 Account locked. Too many wrong attempts.")


# ── while-else ───────────────────────────────────────────────
# Just like for-else, the else block runs only if the loop
# ended naturally (condition became False) — not via break.

n = 1
while n <= 5:
    print(n, end=" ")
    n += 1
else:
    print("\nLoop finished normally (no break).")


# ============================================================
#  Quick Recap
#  • while loop → use when number of iterations is unknown
#  • Always update the loop variable to avoid infinite loops
#  • while True + break → loop until a condition is met
#  • while-else → else runs only if no break occurred
#  • Digit tricks: num % 10 = last digit,  num // 10 = drop it
# ============================================================

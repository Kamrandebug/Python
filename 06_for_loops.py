# ============================================================
#  PYTHON COURSE — Chapter 6: For Loops
# ============================================================
# A for loop repeats a block of code for every item
# in a sequence (range, string, list, etc.).
#
# Syntax:
#   for variable in sequence:
#       # code to repeat
#
# Use a for loop when you KNOW how many times to repeat.
# ============================================================


# ── range() Basics ───────────────────────────────────────────
# range(stop)          → 0, 1, 2, … stop-1
# range(start, stop)   → start, start+1, … stop-1
# range(start, stop, step) → with custom step

for i in range(5):           # 0 1 2 3 4
    print(i, end=" ")
print()

for i in range(1, 6):        # 1 2 3 4 5
    print(i, end=" ")
print()

for i in range(1, 10, 2):   # 1 3 5 7 9  (step = 2)
    print(i, end=" ")
print()

for i in range(10, 0, -1):  # 10 9 8 … 1  (countdown)
    print(i, end=" ")
print()


# ── Example 1: Print 1 to N ──────────────────────────────────
n = int(input("Enter a number: "))

print(f"Numbers from 1 to {n}:")
for i in range(1, n + 1):    # n+1 because stop is exclusive
    print(i, end=" ")
print()


# ── Example 2: Multiplication Table ─────────────────────────
n = int(input("Which table do you want? "))

print(f"\nMultiplication Table of {n}:")
for i in range(1, 11):
    print(f"{n}  x  {i:2}  =  {n * i}")
    # :2 pads the number to 2 digits for clean alignment


# ── Example 3: Sum of 1 to N ─────────────────────────────────
# Accumulator pattern — start at 0, add each value.

n   = int(input("Find sum from 1 to: "))
total = 0

for i in range(1, n + 1):
    total = total + i   # accumulate

print(f"Sum of 1 to {n} = {total}")
# Tip: the formula n*(n+1)/2 gives the same result instantly!


# ── Example 4: Factorial ─────────────────────────────────────
# Accumulator pattern — start at 1, multiply each value.

n    = int(input("Find factorial of: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i    # keep multiplying

print(f"{n}! = {fact}")


# ── Example 5: Sum of Even and Odd Separately ────────────────

n    = int(input("Enter upper limit: "))
even = 0
odd  = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even += i
    else:
        odd += i

print(f"Sum of even numbers : {even}")
print(f"Sum of odd  numbers : {odd}")


# ── Example 6: Factors of a Number ──────────────────────────
# A factor divides the number with no remainder.

n = int(input("Find factors of: "))
print(f"Factors of {n}: ", end="")

for i in range(1, n + 1):
    if n % i == 0:         # if remainder is 0, i is a factor
        print(i, end="  ")
print()


# ── Example 7: Perfect Number ────────────────────────────────
# A perfect number equals the sum of its proper divisors (excluding itself).
# Example: 6 → divisors are 1, 2, 3 → 1+2+3 = 6 ✅

n   = int(input("Check perfect number: "))
total = 0

for i in range(1, n):      # exclude n itself
    if n % i == 0:
        total += i

if total == n:
    print(f"{n} is a Perfect Number ✅")
else:
    print(f"{n} is NOT a Perfect Number ❌")


# ── Example 8: Prime Number Check ───────────────────────────
# A prime number has exactly 2 factors: 1 and itself.

n     = int(input("Check prime number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print(f"{n} is a Prime Number 🔢")
else:
    print(f"{n} is NOT a Prime Number")


# ── Example 9: Iterating Over a String ──────────────────────
# for loops work on ANY sequence, including strings.

word = "CODING"
print("Characters in word:")

for ch in word:
    print(ch, end=" ")
print()

# Using index
for i in range(len(word)):
    print(f"Index {i} → {word[i]}")


# ── Example 10: Reverse a String ─────────────────────────────

a = "CODING"
b = ""

for i in range(len(a) - 1, -1, -1):   # go from last index to 0
    b = b + a[i]

print(f"Reversed: {b}")
# Tip: a[::-1] does the same thing in one step!


# ── Example 11: Palindrome String Check ─────────────────────
# A palindrome reads the same forwards and backwards. Example: NAMAN

word = input("Enter a word to check palindrome: ").upper()
rev  = ""

for i in range(len(word) - 1, -1, -1):
    rev = rev + word[i]

if rev == word:
    print(f"'{word}' IS a palindrome ✅")
else:
    print(f"'{word}' is NOT a palindrome ❌")


# ── Example 12: Count Digits, Letters, Special Chars ─────────

text = "sdfsogn12413@#$%^&U"
digits  = 0
letters = 0
special = 0

for ch in text:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1
    else:
        special += 1

print(f"Digits   : {digits}")
print(f"Letters  : {letters}")
print(f"Special  : {special}")


# ── Example 13: for-else ─────────────────────────────────────
# The else block runs only if the loop completed WITHOUT a break.

print("\nChecking range 1-20 for number 56:")
for i in range(1, 21):
    if i == 56:
        print("Found 56! Breaking.")
        break
    print(i, end=" ")
else:
    # This runs because 56 was never found — break was never hit
    print("\n56 not found. Loop completed normally.")


# ── Example 14: All Primes from 2 to 20 ──────────────────────
# Nested loop + for-else pattern

print("Prime numbers between 2 and 20:")
for num in range(2, 21):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            break              # not prime — stop checking
    else:
        print(num, end="  ")   # inner loop finished without break → prime
print()


# ── Example 15: Star Patterns ────────────────────────────────
# Nested loops — outer controls rows, inner controls columns.

rows = int(input("\nEnter number of rows for patterns: "))

# Right triangle
print("Right Triangle:")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()   # move to next line after each row

# Inverted right triangle
print("Inverted Triangle:")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Pyramid
print("Pyramid:")
for i in range(1, rows + 1):
    print("  " * (rows - i), end="")   # leading spaces
    print("* " * i)


# ── Example 16: Strong Number ────────────────────────────────
# A strong number = sum of factorials of its digits equals itself.
# Example: 145 → 1! + 4! + 5! = 1 + 24 + 120 = 145 ✅

num  = int(input("Check strong number: "))
copy = num
total  = 0

while num > 0:
    digit = num % 10   # extract last digit
    fact  = 1
    for i in range(1, digit + 1):
        fact *= i
    total += fact
    num //= 10         # remove last digit

if total == copy:
    print(f"{copy} is a Strong Number 💪")
else:
    print(f"{copy} is NOT a Strong Number")


# ============================================================
#  Quick Recap
#  • range(stop) / range(start, stop) / range(start, stop, step)
#  • for ch in string  → iterate characters directly
#  • Accumulator pattern → start with 0 or 1, update each loop
#  • for-else → else block runs only if no break occurred
#  • Nested loops → outer = rows, inner = columns (for patterns)
# ============================================================

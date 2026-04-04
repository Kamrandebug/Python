# ============================================================
#  PYTHON COURSE — Chapter 3: Strings
# ============================================================
# A string is a sequence of characters.
# Strings are IMMUTABLE — you cannot change a character in place.
# ============================================================

# ── Creating Strings ─────────────────────────────────────────
s1 = "Hello"
s2 = 'World'
s3 = """This is a
multi-line string"""    # triple quotes allow line breaks

print(s1, s2)
print(s3)


# ── Indexing ─────────────────────────────────────────────────
# Each character has an index starting from 0.
# Negative indexes count from the end.
#
#   C  O  D  I  N  G
#   0  1  2  3  4  5
#  -6 -5 -4 -3 -2 -1

a = "CODING"
print(a[0])    # C  — first character
print(a[-1])   # G  — last character
print(a[3])    # I


# ── Slicing ──────────────────────────────────────────────────
# Syntax: string[start : stop : step]
# start → inclusive,  stop → exclusive,  step → jump

print(a[0:4])    # CODI  — index 0 to 3
print(a[::])     # CODING — full string (default start, stop, step)
print(a[::-1])   # GNIDOC — reversed string  ✅ useful trick
print(a[::2])    # CDN   — every 2nd character


# ── String Length ────────────────────────────────────────────
print(len(a))    # 6


# ── String Concatenation & Repetition ────────────────────────
first = "Coding"
last  = "Academy"
full  = first + last    # joins strings
print(full)             # CodingAcademy

print("Ha" * 3)         # HaHaHa — repeats the string


# ── f-Strings (Formatted String Literals) ────────────────────
# The cleanest way to embed variables inside a string.
# Prefix with f and wrap expressions in { }

name = "Kamran"
age  = 23
print(f"my name is {name} and my age is {age}")
print(f"next year I will be {age + 1}")   # expressions work inside {}


# ── Taking Input from User ───────────────────────────────────
# input() always returns a STRING — convert if you need a number.
# Uncomment to run interactively:

# name = input("What is your name? ")
# age  = int(input("What is your age? "))   # convert string → int
# print(f"Hello {name}, you are {age} years old!")


# ── Common String Methods ────────────────────────────────────
s = "  hello, world!  "

print(s.upper())          #   HELLO, WORLD!
print(s.lower())          #   hello, world!
print(s.strip())          # hello, world!  — removes leading/trailing spaces
print(s.strip().title())  # Hello, World!  — capitalises each word
print(s.strip().replace("world", "Python"))   # hello, Python!

sentence = "apple,banana,mango"
print(sentence.split(","))    # ['apple', 'banana', 'mango'] — splits into list

words = ["apple", "banana", "mango"]
print(", ".join(words))       # apple, banana, mango  — joins list into string

print("hello".startswith("he"))   # True
print("hello".endswith("lo"))     # True
print("hello".find("ll"))         # 2  — index where substring starts
print("hello".count("l"))         # 2  — how many times 'l' appears


# ── String Check Methods ─────────────────────────────────────
print("123".isdigit())     # True  — all digits?
print("abc".isalpha())     # True  — all letters?
print("abc123".isalnum())  # True  — letters or digits only?
print("  ".isspace())      # True  — only whitespace?


# ── Escape Characters ────────────────────────────────────────
print("Line 1\nLine 2")    # \n → new line
print("Col1\tCol2")        # \t → tab
print("He said \"Hi\"")    # \" → literal double quote inside string


# ── Checking Membership ──────────────────────────────────────
print("Cod" in "Coding")    # True
print("xyz" in "Coding")    # False


# ── print(dir(str)) ──────────────────────────────────────────
# Run this to see ALL available string methods:
# print(dir(str))


# ============================================================
#  Quick Recap
#  • Strings are immutable sequences of characters
#  • Use f-strings for clean formatting: f"Hello {name}"
#  • input() always returns a string — cast with int() or float()
#  • Slicing: s[start:stop:step]   |   s[::-1] reverses a string
# ============================================================

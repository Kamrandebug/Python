# --- INTEGERS (int) ---
# Whole numbers. No decimal. No limit in Python (unlike other languages!)
age = 25
year = 2026
negative = -100

# --- FLOATS (float) ---
# Numbers with decimals. Stored as binary fractions (important gotcha!)
price = 19.99
pi = 3.14159

# ⚠️ Famous float gotcha every dev must know:
print(0.1 + 0.2)  # Output: 0.30000000000000004  ← NOT 0.3!
# Why? Because floats are stored in binary and 0.1 can't be represented exactly.

# --- STRINGS (str) ---
name = "Ali"
city = 'Lahore'

# --- BOOLEANS (bool) ---
# Only two values. Used in conditions everywhere.
is_logged_in = True
has_permission = False

# Boolean is actually a subclass of int in Python!
print(True + True)   # Output: 2  ← True == 1, False == 0

# --- NONE (NoneType) ---
# Represents "nothing" / absence of value. NOT zero. NOT empty string.
result = None


# How to Check a Type
x = 42
print(type(x))
print(type('Kamran'))
print(type(3.14))
print(type(True))


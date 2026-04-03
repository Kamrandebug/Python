# Arithmetic Operators

a, b = 17, 5

print(a + b)   # 22  — Addition
print(a - b)   # 12  — Subtraction
print(a * b)   # 85  — Multiplication
print(a / b)   # 3.4 — Division (ALWAYS returns float!)
print(a // b)  # 3   — Floor division (drops decimal, rounds DOWN)
print(a % b)   # 2   — Modulus (remainder)
print(a ** b)  # 1419857 — Exponentiation (17 to the power 5)

# ⭐ Modulus is incredibly useful:
# Check if number is even:  n % 2 == 0
# Check if divisible by x:  n % x == 0
# Wrap around (like a clock): index % length


# Comparison Operators

x, y = 10, 20

print(x == y)   # False — Equal to
print(x != y)   # True  — Not equal to
print(x > y)    # False — Greater than
print(x < y)    # True  — Less than
print(x >= 10)  # True  — Greater than or equal
print(x <= 9)   # False — Less than or equal

# Chaining comparisons — unique to Python!
age = 25
print(18 <= age <= 65)   # True — very readable!
# In other languages you'd write: age >= 18 and age <= 65


# Logical Operators

# and — BOTH must be True
print(True and True)   # True
print(True and False)  # False

# or — AT LEAST ONE must be True
print(True or False)   # True
print(False or False)  # False

# not — flips the boolean
print(not True)   # False
print(not False)  # True

# Real-world example:
age = 20
has_id = True
can_enter = age >= 18 and has_id
print(can_enter)  # True

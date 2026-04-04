# ============================================================
#  PYTHON COURSE — Chapter 4: Operators
# ============================================================
# Operators are symbols that perform operations on values.
# Python has 6 main categories of operators.
# ============================================================


# ── 1. Arithmetic Operators ──────────────────────────────────
# Used for mathematical calculations.
#
#  Operator  Meaning            Example   Result
#  ────────  ─────────────────  ───────   ──────
#  +         Addition           5 + 3     8
#  -         Subtraction        5 - 3     2
#  *         Multiplication     5 * 3     15
#  /         Division (float)   5 / 2     2.5
#  //        Floor Division     5 // 2    2  (drops decimal)
#  %         Modulo (remainder) 5 % 2     1
#  **        Exponent           5 ** 2    25

a = 5
b = 32

print(a + b)    # 37
print(b - a)    # 27
print(a * b)    # 160
print(b / a)    # 6.4   — always float
print(b // a)   # 6     — floor (rounded down)
print(b % a)    # 2     — remainder of 32 ÷ 5
print(5 ** 3)   # 125   — 5 to the power of 3

# ⚠️ BODMAS / PEMDAS applies — same order of operations as maths
print(12 + 4 / 2)   # 14.0  (division happens first, then addition)


# ── 2. Assignment Operators ──────────────────────────────────
# Used to assign or update a variable's value.

x = 10     # basic assignment

# Compound assignment — shorthand for x = x <op> value
x += 5     # x = x + 5  →  15
x -= 3     # x = x - 3  →  12
x *= 2     # x = x * 2  →  24
x /= 4     # x = x / 4  →   6.0
x //= 2    # x = x // 2 →   3.0
x **= 3    # x = x ** 3 →  27.0
x %= 5     # x = x % 5  →   2.0

print(x)   # 2.0


# ── 3. Comparison (Relational) Operators ─────────────────────
# Compare two values and always return True or False.
#
#  Operator  Meaning                  Example
#  ────────  ───────────────────────  ──────────────
#  ==        equal to                 5 == 5   → True
#  !=        not equal to             5 != 3   → True
#  >         greater than             7 > 3    → True
#  <         less than                2 < 9    → True
#  >=        greater than or equal    5 >= 5   → True
#  <=        less than or equal       4 <= 4   → True

print(12.1 == 12)    # False  — float vs int
print(12.1 != 12)    # True
print(12.1 > 12)     # True
print(45 < 67)       # True
print(23 >= 23)      # True
print(45 <= 45)      # True

# ── Strings are compared using ASCII values ─
print(ord("A"))         # 65  — ASCII code for 'A'
print(ord("B"))         # 66
print("ABC" > "ACD")   # False — 'B'(66) < 'C'(67) at index 1
# print("A" > 34)       # ❌ TypeError — can't compare str with int


# ── 4. Logical Operators ─────────────────────────────────────
# Combine multiple conditions.
#
#  Operator  Returns True when…
#  ────────  ──────────────────────────────────────────────
#  and       ALL conditions are True
#  or        AT LEAST ONE condition is True
#  not       Flips True → False and False → True

# and — every condition must be True
print(12 > 20 and 123 > 100)   # False  — first condition fails

# or — at least one must be True
print(12 != 12 or 10 > 5)      # True   — last condition is True

# not — negates the result
print(not 12 == 12)            # False  — 12==12 is True, not flips it to False

# Combining all three
age = 25
has_id = True
print(age >= 18 and has_id and not False)   # True


# ── 5. Identity Operators ────────────────────────────────────
# Check whether two variables point to the SAME object in memory.
# Use 'is' for None checks, not ==

x = None
print(x is None)      # True  ✅ correct way
print(x is not None)  # False


# ── 6. Membership Operators ──────────────────────────────────
# Check whether a value exists inside a sequence (string, list, etc.)

name = "CodingAcademy"
print("Coding" in name)       # True
print("xyz"    not in name)   # True

fruits = ["apple", "mango", "banana"]
print("mango" in fruits)    # True


# ============================================================
#  Quick Recap
#  Arithmetic  : + - * / // % **
#  Assignment  : = += -= *= /= //= %= **=
#  Comparison  : == != > < >= <=  (always return bool)
#  Logical     : and  or  not
#  Identity    : is  is not
#  Membership  : in  not in
# ============================================================

# ============================================================
#  PYTHON COURSE — Chapter 2: Data Types
# ============================================================
# Python automatically detects the type of a value.
# Use type() to check what type a variable holds.
# ============================================================

# ── 1. Integer (int) ─────────────────────────────────────────
# Whole numbers — positive, negative, or zero. No decimal point.

a = -34
b = 100
c = 0

print(type(a))   # <class 'int'>
print(a, b, c)


# ── 2. Float (float) ─────────────────────────────────────────
# Numbers WITH a decimal point.
# Division (/) always returns a float, even if the result is whole.

x = 56.8
y = 12 / 3      # → 4.0  (float, not 4)
z = -0.001

print(type(x))   # <class 'float'>
print(y)         # 4.0


# ── 3. Complex (complex) ─────────────────────────────────────
# Numbers with a real part and an imaginary part (j = √-1).
# Mostly used in scientific/mathematical computing.

v = 34j
w = 3 + 5j

print(type(v))   # <class 'complex'>
print(w.real)    # 3.0  — real part
print(w.imag)    # 5.0  — imaginary part


# ── 4. String (str) ──────────────────────────────────────────
# A sequence of characters enclosed in single or double quotes.

s1 = "Hello, World!"
s2 = 'Python is fun'
s3 = "It's easy"        # single quote inside double quotes — no problem
s4 = '1231243235 dsagaiogiaeb !@#$%^&*'   # any characters are allowed

print(type(s1))   # <class 'str'>
print(len(s1))    # 13 — number of characters including the comma and space


# ── 5. Boolean (bool) ────────────────────────────────────────
# Only two possible values: True or False (capitalised!)
# Used heavily in conditions and comparisons.

is_logged_in = True
is_admin     = False

print(type(is_logged_in))   # <class 'bool'>
print(10 > 5)               # True  — comparison produces a bool
print(10 == 20)             # False

# Boolean is actually a subtype of int in Python
print(int(True))    # 1
print(int(False))   # 0


# ── 6. None (NoneType) ───────────────────────────────────────
# Represents the absence of a value. Like null in other languages.

result = None
print(type(result))      # <class 'NoneType'>
print(result is None)    # True  — use 'is', not == for None


# ── Type Conversion (Casting) ────────────────────────────────
# Convert between types using int(), float(), str(), bool()

num_str = "42"
num_int = int(num_str)       # "42" → 42
num_flt = float(num_str)     # "42" → 42.0
back_to_str = str(num_int)   # 42  → "42"

print(type(num_int))    # <class 'int'>
print(type(num_flt))    # <class 'float'>

# ⚠️ You can't convert a non-numeric string to int/float
# int("hello")  # ❌ ValueError


# ── Checking Types ───────────────────────────────────────────
value = 3.14
print(isinstance(value, float))   # True  — preferred over type() for checks
print(isinstance(value, int))     # False


# ============================================================
#  Quick Recap
#  Type        Example          Use case
#  ──────────  ───────────────  ──────────────────────────
#  int         42, -7           counting, indexing
#  float       3.14, -0.5       measurements, division
#  complex     3+5j             math / signal processing
#  str         "hello"          text
#  bool        True / False     conditions, flags
#  NoneType    None             missing / empty value
# ============================================================

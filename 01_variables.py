# ============================================================
#  PYTHON COURSE — Chapter 1: Variables
# ============================================================
# A variable is a named container that stores a value in memory.
# You don't need to declare a type — Python figures it out.
# ============================================================

# ── Syntax ──────────────────────────────────────────────────
#   variable_name = value

name = "Kamran"
age  = 23
pi   = 3.14

print(name)   # Kamran
print(age)    # 23
print(pi)     # 3.14


# ── Naming Conventions ──────────────────────────────────────
# Python supports multiple styles. Pick ONE and stay consistent.

CodingAcademy    = "students"   # PascalCase   → used for class names
codingAcademy    = "students"   # camelCase    → popular in JS, avoid in Python
coding_academy   = "students"   # snake_case   ✅ recommended for variables in Python


# ── Rules for Variable Names ─────────────────────────────────
# ✅ Can contain letters, digits, and underscores
# ✅ Must START with a letter or underscore (not a digit)
# ❌ Cannot use Python keywords (if, for, while, class …)

score_1  = 100       # ✅ valid
_hidden  = "secret"  # ✅ valid
# 1score = 10        # ❌ SyntaxError — starts with a digit


# ── Multiple Assignment ──────────────────────────────────────
x = y = z = 0          # all three get the same value
a, b, c = 10, 20, 30   # unpacking — each variable gets its own value

print(x, y, z)   # 0 0 0
print(a, b, c)   # 10 20 30


# ── Swapping Variables ───────────────────────────────────────
# In most languages you need a temp variable. Python does it in one line!
a, b = b, a
print(a, b)   # 20 10  (swapped!)


# ── Reassignment ─────────────────────────────────────────────
# A variable can be reassigned to any type at any time
city = "Delhi"
print(city)   # Delhi

city = 100    # now it holds an integer — Python allows this
print(city)   # 100


# ── Constants (by convention) ────────────────────────────────
# Python has no built-in constant keyword.
# UPPER_SNAKE_CASE signals "treat this as a constant — don't change it."
MAX_SPEED   = 120
PI          = 3.14159
APP_VERSION = "1.0.0"


# ── Checking Variable Type ───────────────────────────────────
brand = "Nike"
price = 2999
print(type(brand))   # <class 'str'>
print(type(price))   # <class 'int'>


# ── Deleting a Variable ──────────────────────────────────────
temp = "I am temporary"
del temp
# print(temp)   # ❌ NameError — variable no longer exists after del


# ============================================================
#  Quick Recap
#  • Use snake_case for variable names
#  • = is assignment,  == is comparison (equality check)
#  • Python is dynamically typed — no need to declare types
# ============================================================

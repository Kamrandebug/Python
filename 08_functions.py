# ============================================================
#  PYTHON COURSE — Chapter 8: Functions
# ============================================================
# A function is a reusable block of code that performs a task.
# Define once → call many times.
#
# Benefits:
#   ✅ Avoid code repetition (DRY — Don't Repeat Yourself)
#   ✅ Makes code readable and organised
#   ✅ Easy to test and debug
#
# Syntax:
#   def function_name(parameters):
#       # body
#       return value   # optional
# ============================================================


# ── 1. Basic Function (no parameters) ────────────────────────

def greet():
    print("Hello! Welcome to Coding Academy 👋")

greet()    # calling the function


# ── 2. Function with Parameters ──────────────────────────────
# Parameters are inputs the function needs to do its job.

def hello(name, age):
    print(f"Your name is {name} and your age is {age}")

hello("Kamran", 23)             # positional arguments — order matters
hello(age=22, name="Harsh")     # keyword arguments  — order doesn't matter


# ── 3. Default Parameter Values ──────────────────────────────
# If the caller doesn't pass a value, the default is used.

def welcome(name, course="Python"):
    print(f"Welcome {name} to the {course} course!")

welcome("Kamran")           # uses default course
welcome("Harsh", "DSA")     # overrides the default


# ── 4. Return Values ─────────────────────────────────────────
# return sends a result back to the caller.
# Without return, a function returns None by default.

def add(a, b):
    return a + b    # sends the result back

result = add(12, 67)
print(f"Sum: {result}")    # 79

# You can return multiple values — Python returns them as a tuple
def min_max(lst):
    return min(lst), max(lst)

lo, hi = min_max([3, 1, 9, 2, 7])
print(f"Min: {lo}, Max: {hi}")


# ── 5. Practical Function — Palindrome Checker ───────────────
# Functions make reusable logic clean and testable.

def is_palindrome(st):
    rev = ""
    for i in range(len(st) - 1, -1, -1):
        rev += st[i]

    if rev == st:
        print(f"'{st}' IS a palindrome ✅")
    else:
        print(f"'{st}' is NOT a palindrome ❌")

is_palindrome("NAMAN")
is_palindrome("CURSOR")
is_palindrome("LEVEL")


# ── 6. *args — Variable Positional Arguments ─────────────────
# Use *args when you don't know how many arguments will be passed.
# Inside the function, args is a tuple.

def total(*args):
    print(f"Arguments received: {args}")
    return sum(args)

print(total(1, 2, 3))            # 6
print(total(10, 20, 30, 40))     # 100


# ── 7. **kwargs — Variable Keyword Arguments ─────────────────
# Use **kwargs to accept any number of keyword arguments.
# Inside the function, kwargs is a dictionary.

def information(**kwargs):
    print("\nYour Information:")
    print("-" * 20)
    for key, value in kwargs.items():
        print(f"  {key:15} : {value}")

information(name="Kamran", age=23, designation="AI/ML Engineer")


# ── 8. Scope — Local vs Global ───────────────────────────────
# Variables created inside a function are LOCAL — not visible outside.
# Variables created outside are GLOBAL.

course = "Python"    # global variable

def show_course():
    language = "Python"    # local variable — only exists inside here
    print(f"Inside function: {course}")    # can READ global variable

show_course()
print(f"Outside function: {course}")
# print(language)   # ❌ NameError — local variable doesn't exist here


# ── 9. Decorator ─────────────────────────────────────────────
# A decorator WRAPS a function — it adds behaviour before/after
# without modifying the original function.
# Used in real projects for logging, authentication, timing, etc.

def decorate(func):
    def wrapper(*args, **kwargs):
        print("─" * 30)
        print("▶ Starting function...")
        func(*args, **kwargs)           # call the original function
        print("✅ Function completed.")
        print("─" * 30)
    return wrapper

@decorate
def addition(a, b):
    print(f"The sum of {a} + {b} = {a + b}")

addition(12, 67)


# ── 10. Lambda — Anonymous Functions ─────────────────────────
# A lambda is a small, one-line function with no name.
# Syntax: lambda arguments: expression

square = lambda x: x ** 2
print(square(5))    # 25

add = lambda a, b: a + b
print(add(3, 4))    # 7

# Lambdas shine with map(), filter(), sorted()
nums   = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)      # [2, 4, 6, 8, 10]

evens   = list(filter(lambda x: x % 2 == 0, nums))
print(evens)        # [2, 4]


# ── 11. map() ────────────────────────────────────────────────
# Applies a function to every item in a list.

def double(x):
    return x * 2

nums   = [1, 2, 3, 4, 5]
result = list(map(double, nums))
print(result)   # [2, 4, 6, 8, 10]


# ── 12. Recursion ────────────────────────────────────────────
# A function that calls ITSELF. Every recursive function needs:
#   1. A base case (to stop)
#   2. A recursive case (to reduce the problem)

def factorial(n):
    if n == 0 or n == 1:   # base case — stop here
        return 1
    return n * factorial(n - 1)    # recursive case

print(factorial(5))    # 120  →  5 * 4 * 3 * 2 * 1


# ============================================================
#  Quick Recap
#  • def → define a function
#  • Parameters → inputs,   return → output
#  • Default params → used when caller doesn't pass a value
#  • *args → variable positional args (tuple inside)
#  • **kwargs → variable keyword args (dict inside)
#  • Decorator → wraps a function to add extra behaviour
#  • Lambda → one-line anonymous function
#  • Recursion → function that calls itself (needs a base case)
# ============================================================

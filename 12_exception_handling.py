# ============================================================
#  PYTHON COURSE — Chapter 12: Exception Handling
# ============================================================
# An exception is an error that occurs at RUNTIME.
# Without handling, it crashes the program.
# With handling, you can respond gracefully and keep running.
#
# Syntax:
#   try:
#       risky code
#   except ExceptionType as err:
#       handle the error
#   else:
#       runs only if NO exception occurred
#   finally:
#       ALWAYS runs — cleanup code goes here
# ============================================================


# ── Why Do We Need This? ─────────────────────────────────────
# print(10 / 0)          # ❌ ZeroDivisionError — crashes program
# int("hello")           # ❌ ValueError
# my_list = [1,2,3]
# my_list[10]            # ❌ IndexError
# open("missing.txt")    # ❌ FileNotFoundError


# ── Example 1: Basic try-except ──────────────────────────────

a = int(input("Enter a number (try 0 to see the error): "))

try:
    result = 10 / a          # this may raise ZeroDivisionError
    print(f"Result: {result}")

except ZeroDivisionError:
    # catches ONLY ZeroDivisionError
    print("❌ Error: Cannot divide by zero!")


# ── Example 2: Catching Any Exception ────────────────────────
# Use Exception as a catch-all (use sparingly — be specific when possible).

a = int(input("Enter a number: "))

try:
    print(10 / a)

except Exception as err:
    # 'err' holds the error message
    print(f"❌ An error occurred: {err}")


# ── Example 3: try-except-else-finally ───────────────────────
# else  → runs ONLY when no exception was raised
# finally → ALWAYS runs (use for cleanup: closing files, db, etc.)

a = int(input("Enter a number: "))

try:
    result = 10 / a

except ZeroDivisionError as err:
    print(f"❌ Error: {err}")

else:
    # This only runs if the try block succeeded
    print(f"✅ No error! Result is: {result}")

finally:
    # This ALWAYS runs — no matter what
    print("🔄 Execution complete (finally block ran)")

print("Program continues normally after the try block...")


# ── Example 4: Catching Multiple Specific Exceptions ─────────

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("❌ Cannot divide by zero")
    except TypeError:
        print("❌ Invalid type — please use numbers")

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # error message
print(safe_divide(10, "a"))  # error message


# ── Example 5: raise — Custom Exception ──────────────────────
# You can manually raise an exception when data is invalid.
# This is called "raising" or "throwing" an exception.

age = int(input("Enter your age (must be between 10 and 18): "))

try:
    if age < 10 or age > 18:
        raise ValueError(f"Age {age} is out of range. Must be 10–18.")
    else:
        print("✅ Welcome to the club!")

except ValueError as err:
    print(f"❌ Invalid input: {err}")

print("Program continues...")


# ── Example 6: Custom Exception Classes ──────────────────────
# For big projects, you create your OWN exception types.

class InsufficientFundsError(Exception):
    """Raised when account balance is too low."""
    def __init__(self, balance, amount):
        self.message = f"Cannot withdraw ₹{amount}. Available balance: ₹{balance}"
        super().__init__(self.message)


def withdraw(balance, amount):
    try:
        if amount > balance:
            raise InsufficientFundsError(balance, amount)
        balance -= amount
        print(f"✅ Withdrawal successful. New balance: ₹{balance}")
        return balance

    except InsufficientFundsError as err:
        print(f"❌ {err}")
        return balance

balance = withdraw(500, 200)    # ✅ works
balance = withdraw(balance, 400)  # ❌ not enough


# ── Example 7: Nested try-except ─────────────────────────────
# You can nest try blocks inside each other.

try:
    num = int(input("Enter an integer: "))   # may raise ValueError
    try:
        result = 100 / num                   # may raise ZeroDivisionError
        print(f"100 / {num} = {result}")
    except ZeroDivisionError:
        print("❌ Inner error: division by zero")

except ValueError:
    print("❌ Outer error: that's not a valid integer")


# ── Common Built-in Exceptions ───────────────────────────────
#
#  Exception            When it happens
#  ─────────────────    ─────────────────────────────────────────────
#  ZeroDivisionError    Dividing by zero
#  ValueError           Wrong value type (e.g. int("hello"))
#  TypeError            Wrong type operation (e.g. "a" + 1)
#  IndexError           List index out of range
#  KeyError             Dictionary key not found
#  FileNotFoundError    Opening a file that doesn't exist
#  AttributeError       Calling a method that doesn't exist
#  NameError            Using a variable that's not defined
#  OverflowError        Number too large for the type


# ============================================================
#  Quick Recap
#  • try     → code that might fail
#  • except  → what to do when it fails (be specific!)
#  • else    → runs only if NO exception occurred
#  • finally → ALWAYS runs (cleanup)
#  • raise   → manually trigger an exception
#  • Custom exceptions → inherit from Exception class
# ============================================================

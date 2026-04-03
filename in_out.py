# Input

# Always returns a STRING — remember this!
name = input("What is your name? ")
print(f"Hello, {name}!")

# Getting numbers from user
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

print(f"You are {age} years old and {height}m tall.")

# Multiple inputs in one line
x, y = input("Enter two numbers separated by space: ").split()
x, y = int(x), int(y)
print(f"Sum = {x + y}")

# Or the compact way:
a, b = map(int, input("Enter two numbers: ").split())
print(f"Sum = {a + b}")


# Output

# Basic
print("Hello, World!")

# Multiple values (sep controls separator)
print("Ali", "Ahmed", "Zara")          # Ali Ahmed Zara
print("Ali", "Ahmed", "Zara", sep=", ") # Ali, Ahmed, Zara
print("Ali", "Ahmed", sep=" | ")        # Ali | Ahmed

# end= controls what comes after (default is newline \n)
print("Loading", end="")
print("...", end="\n")
# Output: Loading...

# Print anything
print(42, 3.14, True, None, [1, 2, 3])

# Pretty printing for debugging
data = {"name": "Ali", "age": 25}
import pprint
pprint.pprint(data)
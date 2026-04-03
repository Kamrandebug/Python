name = "Muhammad Kamran"

# Indexing — access individual characters (0-based)
print(name[0])   # 'M'
print(name[-1])  # 'n'  ← negative index goes from the end

# Slicing — extract a portion [start:end:step]
print(name[0:8])    # 'Muhammad'
print(name[9:])     # 'Kamran'
print(name[::-1])   # 'narmaK dammahuM'  ← reverses the string!



# Essential String Methods


text = "  hello world  "

# Cleaning
print(text.strip())       # "hello world" — removes whitespace
print(text.lstrip())      # "hello world  "
print(text.rstrip())      # "  hello world"

# Case
print(text.upper())       # "  HELLO WORLD  "
print(text.lower())       # "  hello world  "
print(text.title())       # "  Hello World  "

# Searching
sentence = "Python is awesome"
print(sentence.find("is"))       # 7 — returns index
print(sentence.count("o"))       # 2
print(sentence.startswith("Py")) # True
print(sentence.endswith("me"))   # True
print("awesome" in sentence)     # True ← most Pythonic way!

# Replacing & Splitting
print(sentence.replace("awesome", "powerful"))
# "Python is powerful"

words = sentence.split(" ")   # ['Python', 'is', 'awesome']
joined = "-".join(words)       # 'Python-is-awesome'



# String Formatting — 3 Ways


name = "Ali"
age = 25
city = "Lahore"

# 1. Old way — % formatting (avoid in new code)
print("My name is %s and I am %d years old" % (name, age))

# 2. .format() — still common in older codebases
print("My name is {} and I am {} years old".format(name, age))
print("My name is {name} and I live in {city}".format(name=name, city=city))

# 3. f-strings — THE modern way (Python 3.6+). Use this always.
print(f"My name is {name} and I am {age} years old")
print(f"Next year I'll be {age + 1}")     # expressions work inside!
print(f"Pi is approximately {3.14159:.2f}")  # formatting: 2 decimal places
# Type Conversion IMPLICIT & EXPLICIT

# --- IMPLICIT (Python does it automatically) ---
result = 5 + 2.0   # int + float = float automatically
print(result)       # 7.0
print(type(result)) # <class 'float'>

# --- EXPLICIT (you convert manually) ---

# To integer
print(int("42"))     # 42   ← string to int
print(int(3.99))     # 3    ← float to int (truncates, does NOT round!)
print(int(True))     # 1
print(int(False))    # 0

# To float
print(float("3.14")) # 3.14
print(float(5))      # 5.0

# To string
print(str(100))      # "100"
print(str(3.14))     # "3.14"
print(str(True))     # "True"

# To boolean
print(bool(0))       # False  ← FALSY values
print(bool(""))      # False
print(bool(None))    # False
print(bool([]))      # False  ← empty list is falsy too

print(bool(1))       # True   ← everything else is TRUTHY
print(bool("hello")) # True
print(bool(-1))      # True   ← even negative numbers are truthy!
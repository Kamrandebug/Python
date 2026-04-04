# ============================================================
#  PYTHON COURSE — Chapter 11: Dictionaries
# ============================================================
# A dictionary stores data as KEY : VALUE pairs.
# Keys must be unique and immutable (str, int, tuple).
# Values can be anything.
#
# Use dictionaries when data has a natural label/name.
# Example: a person's name → age, a product → price.
#
# Syntax: my_dict = { key1: value1, key2: value2 }
# ============================================================


# ── Creating a Dictionary ────────────────────────────────────
student = {
    "name"  : "Kamran",
    "age"   : 23,
    "course": "Python",
    "grade" : "A"
}

print(student)
print(type(student))   # <class 'dict'>


# ── Accessing Values ─────────────────────────────────────────
print(student["name"])             # Kamran
print(student.get("age"))          # 23
print(student.get("email", "N/A")) # N/A  — default if key not found

# ⚠️ student["email"] would raise KeyError if key doesn't exist
# Use .get() when key might be missing


# ── CRUD Operations (Create, Read, Update, Delete) ───────────
d = {10: 100, 20: 200, 30: 300, 40: 400}

# Update — change an existing value
d[10] = 150
print(f"After update: {d}")

# Create — add a new key-value pair
d[50] = 500
print(f"After add: {d}")

# Delete — remove a key-value pair
del d[30]
print(f"After delete: {d}")

# Another way to delete — pop() also returns the value
removed = d.pop(20)
print(f"Removed value: {removed}")
print(d)


# ── Useful Dictionary Methods ────────────────────────────────
d = {10: 100, 20: 200, 30: 300, 40: 400}

print(d.keys())     # dict_keys([10, 20, 30, 40])
print(d.values())   # dict_values([100, 200, 300, 400])
print(d.items())    # dict_items([(10,100), (20,200), ...])


# ── Iterating Over a Dictionary ──────────────────────────────
# Iterating gives you the KEYS by default.

print("\nLooping over keys:")
for key in d:
    print(f"  Key: {key}  →  Value: {d[key]}")

print("\nLooping over items (key & value together):")
for key, value in d.items():   # .items() gives (key, value) pairs
    print(f"  {key} : {value}")


# ── Example 1: Sum of All Values ─────────────────────────────
d     = {10: 100, 20: 200, 40: 300}
total = 0

for key in d:
    total += d[key]    # or: total += d[key] using values()

print(f"Total of values: {total}")

# One-liner using sum()
print(f"Total (one-liner): {sum(d.values())}")


# ── Example 2: Merge Two Dictionaries ────────────────────────
d1 = {10: 100, 20: 200, 40: 300}
d2 = {40: 400, 50: 500, 60: 600}

# Method 1 — loop
for key in d2:
    d1[key] = d2[key]    # if key exists it overwrites, else it creates
print(f"Merged: {d1}")

# Method 2 — .update() (cleaner)
d1 = {10: 100, 20: 200, 40: 300}
d1.update(d2)
print(f"Merged with update(): {d1}")

# Method 3 — ** unpacking (Python 3.5+)
merged = {**d1, **d2}
print(f"Merged with **: {merged}")


# ── Example 3: Merge and ADD Common Key Values ───────────────
d1 = {10: 100, 20: 200, 40: 300}
d2 = {40: 400, 50: 500, 60: 600}

for key in d2:
    if key in d1:
        d1[key] += d2[key]   # add to existing value
    else:
        d1[key] = d2[key]    # create new key

print(f"After merge+add: {d1}")


# ── Example 4: Frequency Count ───────────────────────────────
# Count how many times each item appears in a list.

items = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 7, 8]
freq  = {}

for item in items:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print(f"Frequency: {freq}")

# One-liner using .get()
freq2 = {}
for item in items:
    freq2[item] = freq2.get(item, 0) + 1   # get current count (default 0) + 1
print(f"Frequency (get): {freq2}")


# ── Example 5: Word Frequency in a Sentence ──────────────────
sentence = "the cat sat on the mat the cat"
words    = sentence.split()
freq     = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("\nWord frequencies:")
for word, count in freq.items():
    print(f"  '{word}' → {count}")


# ── Nested Dictionary ────────────────────────────────────────
# Dictionary values can themselves be dictionaries.

students = {
    "Kamran": {"age": 23, "grade": "A"},
    "Harsh" : {"age": 25, "grade": "B"},
    "Naman" : {"age": 22, "grade": "A+"},
}

for name, info in students.items():
    print(f"{name}: Age={info['age']}, Grade={info['grade']}")


# ── Dictionary Comprehension ─────────────────────────────────
# Create a dictionary in one line.
# Syntax: { key_expr: val_expr for item in iterable }

squares = {i: i ** 2 for i in range(1, 11)}
print(f"\nSquares: {squares}")

even_squares = {i: i ** 2 for i in range(1, 11) if i % 2 == 0}
print(f"Even squares: {even_squares}")


# ── Checking Membership ──────────────────────────────────────
info = {"name": "Kamran", "age": 23}
print("name" in info)     # True  — checks KEYS only
print(23 in info)         # False — 23 is a value, not a key
print(23 in info.values()) # True  — check values with .values()


# ============================================================
#  Quick Recap
#  • dict = { key: value } — keys must be unique & immutable
#  • Access: d[key] or d.get(key, default)
#  • d.keys()   d.values()   d.items()
#  • Delete: del d[key]  or  d.pop(key)
#  • Merge: d1.update(d2)  or  {**d1, **d2}
#  • Frequency pattern: d[k] = d.get(k, 0) + 1
#  • Dict comprehension: {k: v for k, v in ...}
# ============================================================

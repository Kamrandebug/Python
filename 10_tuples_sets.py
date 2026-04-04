# ============================================================
#  PYTHON COURSE — Chapter 10: Tuples & Sets
# ============================================================


# ════════════════════════════════════════════════════════════
#  PART A — TUPLES
# ════════════════════════════════════════════════════════════
# A tuple is an ordered, IMMUTABLE collection.
# Immutable = once created, items CANNOT be changed.
#
# Use tuples for data that should never change:
# e.g. coordinates, RGB colors, days of the week.
#
# Syntax: my_tuple = (item1, item2, item3)
# ============================================================

# ── Creating Tuples ──────────────────────────────────────────
coords   = (10, 20)
rgb      = (255, 128, 0)
mixed    = (1, "hello", 3.14, True)
empty    = ()

print(coords)
print(type(coords))   # <class 'tuple'>

# ⚠️ Single-element tuple MUST have a trailing comma!
single = (5,)         # ✅ this is a tuple
not_a_tuple = (5)     # ❌ this is just an integer in parentheses

print(type(single))       # <class 'tuple'>
print(type(not_a_tuple))  # <class 'int'>


# ── Indexing & Slicing ───────────────────────────────────────
# Same as lists — 0-based, supports negatives.

t = (1, 2, 3, 4, 5)
print(t[0])     # 1
print(t[-1])    # 5
print(t[1:4])   # (2, 3, 4)
print(t[::-1])  # (5, 4, 3, 2, 1)


# ── Immutability ─────────────────────────────────────────────
t = (10, 20, 30)
# t[0] = 99   # ❌ TypeError — tuples cannot be changed

# You CAN reassign the variable itself (that's not changing the tuple)
t = (99, 20, 30)   # ✅ new tuple assigned to t


# ── Tuple Methods ────────────────────────────────────────────
a = (1, 2, 3, 4, 5, 5, 5, 5.5, "hello")

print(a.count(5))      # 3 — how many times 5 appears
print(a.index(3))      # 2 — index of first occurrence of 3
print(len(a))          # 9 — number of items


# ── Tuple Packing & Unpacking ────────────────────────────────
# Packing: multiple values → one tuple
point = 10, 20, 30     # parentheses optional for packing

# Unpacking: one tuple → multiple variables
x, y, z = point
print(x, y, z)    # 10 20 30

# Useful for swapping
a, b = 1, 2
a, b = b, a
print(a, b)       # 2 1


# ── Iterating Over a Tuple ───────────────────────────────────
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

for day in days:
    print(day, end="  ")
print()

# Using enumerate to get index + value
for index, day in enumerate(days):
    print(f"{index}: {day}")


# ── Tuple vs List — When to Use Which ────────────────────────
#
#  Feature         Tuple           List
#  ─────────────   ────────────    ──────────────────
#  Mutable?        ❌ No            ✅ Yes
#  Syntax          (1, 2, 3)       [1, 2, 3]
#  Speed           ✅ Faster        Slightly slower
#  Use case        Fixed data      Dynamic data
#  Can be a dict   ✅ Yes           ❌ No (unhashable)
#  key?


# ════════════════════════════════════════════════════════════
#  PART B — SETS
# ════════════════════════════════════════════════════════════
# A set is an UNORDERED collection of UNIQUE items.
# Duplicates are automatically removed.
#
# Use sets when:
#   - You want to store unique values only
#   - You need fast membership checks
#   - You want to perform union, intersection, difference
#
# Syntax: my_set = {item1, item2, item3}
# ============================================================

# ── Creating Sets ────────────────────────────────────────────
s = {1, 2, 3, 4, 5}
print(s)
print(type(s))   # <class 'set'>

# Duplicates are automatically removed
s2 = {1, 2, 2, 3, 3, 3, 4}
print(s2)    # {1, 2, 3, 4}

# ⚠️ Empty set must use set(), NOT {} — that creates an empty dict!
empty_set  = set()   # ✅ correct
empty_dict = {}      # this is a dict, not a set


# ── Iterating Over a Set ─────────────────────────────────────
# Sets are unordered — you won't always get the same print order!

a = {1, 8, 9, "hello", 2, 3, 4, 5}
for item in a:
    print(item, end="  ")
print()


# ── Set Methods ──────────────────────────────────────────────
s = {1, 2, 3, 4, 5}

s.add(6)           # add one item
s.update([7, 8])   # add multiple items
s.remove(3)        # remove item — ❌ KeyError if not found
s.discard(99)      # remove item — ✅ NO error if not found
popped = s.pop()   # remove & return a RANDOM item
print(s)
print(f"Popped: {popped}")

s.clear()          # remove all items
print(s)           # set()


# ── Set Operations ───────────────────────────────────────────
# This is where sets shine — mathematical operations.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)    # Union        — all items from both sets
print(a & b)    # Intersection — only common items
print(a - b)    # Difference   — items in a but NOT in b
print(a ^ b)    # Symmetric diff — items in either but NOT both

# Same operations with methods
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

# -= removes all items of b from a
a -= b
print(f"After a -= b: {a}")


# ── Set Membership Check ─────────────────────────────────────
# 'in' with sets is O(1) — much faster than lists for large data!

students = {"Alice", "Bob", "Charlie", "Dave"}
print("Alice" in students)    # True
print("Eve"   in students)    # False


# ── Remove Duplicates from a List Using a Set ────────────────
nums_with_dups = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_nums    = list(set(nums_with_dups))
print(unique_nums)    # [1, 2, 3, 4, 5]  (order may vary)


# ── frozenset ────────────────────────────────────────────────
# An immutable version of a set — cannot be changed after creation.
# Can be used as dictionary keys (regular sets cannot).

fs = frozenset([1, 2, 3, 4])
print(fs)
# fs.add(5)   # ❌ AttributeError — frozenset is immutable


# ============================================================
#  Quick Recap
#  TUPLES
#  • Ordered, immutable — use for fixed data
#  • Single-item tuple needs trailing comma: (5,)
#  • Methods: count(), index(), len()
#
#  SETS
#  • Unordered, unique items — no duplicates
#  • | union   & intersection   - difference   ^ symmetric diff
#  • add(), remove(), discard(), pop(), clear()
#  • Fast membership check: item in my_set
# ============================================================

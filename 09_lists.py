# ============================================================
#  PYTHON COURSE — Chapter 9: Lists
# ============================================================
# A list is an ordered, mutable (changeable) collection
# that can hold items of ANY type — even mixed types.
#
# Syntax:  my_list = [item1, item2, item3]
# ============================================================


# ── Creating Lists ───────────────────────────────────────────
nums   = [12, 13, 14, 15, 16, 34.5]
fruits = ["apple", "mango", "banana"]
mixed  = [1, "hello", 3.14, True, None]   # mixed types are allowed
empty  = []

print(nums)
print(type(nums))   # <class 'list'>


# ── Indexing & Slicing ───────────────────────────────────────
# Works exactly like strings — 0-based, supports negatives & slicing.

a = [10, 20, 30, 40, 50]

print(a[0])     # 10  — first item
print(a[-1])    # 50  — last item
print(a[1:4])   # [20, 30, 40]
print(a[::-1])  # [50, 40, 30, 20, 10]  — reversed


# ── Looping Over a List ───────────────────────────────────────

nums = [12, 13, 14, 15, 16, 34.5]

# Method 1 — by index (use when you need the index)
for i in range(len(nums)):
    print(f"Index {i}: {nums[i]}")

# Method 2 — directly over values (cleaner, preferred)
for val in nums:
    print(val, end=" ")
print()


# ── Modifying a List ─────────────────────────────────────────
fruits = ["apple", "mango", "banana"]

fruits.append("grape")       # add to end
fruits.insert(1, "kiwi")     # insert at index 1
fruits.remove("mango")       # remove by value
popped = fruits.pop()        # remove & return last item
fruits[0] = "pineapple"      # update by index

print(fruits)
print(f"Popped: {popped}")


# ── Common List Methods ──────────────────────────────────────
nums = [5, 3, 8, 1, 9, 2]

print(len(nums))         # 6  — number of items
print(sum(nums))         # 28 — total
print(min(nums))         # 1  — smallest
print(max(nums))         # 9  — largest
print(sorted(nums))      # [1, 2, 3, 5, 8, 9]  — returns new sorted list
nums.sort()              # sorts IN PLACE (modifies the original)
print(nums)
nums.reverse()           # reverses IN PLACE
print(nums)
print(nums.count(3))     # how many times 3 appears
print(nums.index(8))     # index of first occurrence of 8


# ── Example 1: Positive and Negative Elements ────────────────

l = [-45, 67, 12, -68, -69, 34]
positives = []
negatives = []

for i in l:
    if i >= 0:
        positives.append(i)
    else:
        negatives.append(i)

print(f"Positive: {positives}")
print(f"Negative: {negatives}")


# ── Example 2: Average of a List ─────────────────────────────

scores = [12, 435, 67, 89, 23, 25, 69]
total  = 0

for val in scores:
    total += val

average = total / len(scores)
print(f"Average: {average:.2f}")    # :.2f → 2 decimal places


# ── Example 3: Find Largest Element with Index ───────────────

l       = [12, 567, 43, 235, 347, 568, 45, 7]
largest = l[0]
idx     = 0

for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        idx     = i

print(f"Largest value: {largest} at index {idx}")


# ── Example 4: Second Largest Element ────────────────────────

l          = [12, 16, 13, 19, 17]
largest    = l[0]
sec_largest = l[0]

for val in l:
    if val > largest:
        sec_largest = largest
        largest     = val
    elif val > sec_largest and val != largest:
        sec_largest = val

print(f"Largest: {largest},  Second Largest: {sec_largest}")


# ── Example 5: Check if List is Sorted ───────────────────────

a = [12, 13, 18, 15, 16]

for i in range(len(a) - 1):
    if a[i] > a[i + 1]:       # found a pair out of order
        print("❌ List is NOT sorted")
        break
else:
    print("✅ List IS sorted")


# ── Example 6: Most Frequent Element ─────────────────────────

a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5]
freq = {}

# Build frequency dictionary
for item in a:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

# Find the maximum frequency
max_count = max(freq.values())

# Find which element has that frequency
for item in freq:
    if freq[item] == max_count:
        print(f"{item} appears {max_count} times — most frequent 🏆")
        break


# ── List Comprehension ───────────────────────────────────────
# A concise one-liner to create a new list.
# Syntax: [expression for item in iterable if condition]

squares  = [i ** 2 for i in range(1, 6)]         # [1, 4, 9, 16, 25]
evens    = [i for i in range(1, 21) if i % 2 == 0]  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
upper    = [ch.upper() for ch in "coding"]       # ['C','O','D','I','N','G']

print(squares)
print(evens)
print(upper)


# ── 2D Lists (Matrix) ────────────────────────────────────────
# A list of lists — like a table with rows and columns.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access: matrix[row][col]
print(matrix[1][2])    # 6  (row 1, col 2)

# Loop through all elements
for row in matrix:
    for val in row:
        print(val, end="  ")
    print()


# ============================================================
#  Quick Recap
#  • Lists are ordered and mutable (changeable)
#  • append() adds to end,  insert(i, x) adds at index
#  • remove(x) removes by value,  pop() removes last item
#  • sorted() returns new,  .sort() modifies in place
#  • List comprehension: [expr for x in iterable if cond]
# ============================================================

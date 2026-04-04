# ============================================================
#  PYTHON COURSE — Chapter 13: File Handling
# ============================================================
# File handling lets your program read and write to files on disk.
# Data stored in files persists even after the program closes.
#
# Built-in function: open(filename, mode)
#
# Modes:
#  'r'   Read     — opens file for reading (default)
#                   ❌ FileNotFoundError if file doesn't exist
#  'w'   Write    — creates file or OVERWRITES existing content
#  'a'   Append   — adds to the END, creates file if missing
#  'x'   Exclusive— creates a NEW file, ❌ error if it exists
#  'r+'  Read+Write — file must already exist
#
# Add 'b' for binary mode: 'rb', 'wb', 'ab' (for images, pdfs etc.)
# ============================================================


# ── 1. Writing to a File ─────────────────────────────────────
# 'w' mode creates the file if it doesn't exist.
# ⚠️ If the file already exists, 'w' will ERASE all previous content!

file = open("superman.txt", "w")
file.write("Superman is the Man of Steel.\n")
file.write("He can fly and is faster than a speeding bullet.\n")
file.close()    # Always close the file after use!

print("✅ File written successfully.")


# ── 2. Reading a File ─────────────────────────────────────────
# 'r' mode reads the file. The file must already exist.

file = open("superman.txt", "r")

# read() — reads the entire file as one string
content = file.read()
print("\n── Full content ──")
print(content)

file.close()

# readline() — reads one line at a time
file = open("superman.txt", "r")
line1 = file.readline()
line2 = file.readline()
print("── Line by Line ──")
print(line1, end="")
print(line2, end="")
file.close()

# readlines() — returns a LIST of all lines
file = open("superman.txt", "r")
lines = file.readlines()
print("\n── readlines() ──")
for line in lines:
    print(line.strip())   # strip() removes the \n at end of each line
file.close()


# ── 3. Appending to a File ───────────────────────────────────
# 'a' mode adds content to the END — existing content is preserved.

file = open("superman.txt", "a")
file.write("His weakness is Kryptonite.\n")
file.close()

print("✅ Content appended.")


# ── 4. Using 'with' Statement (Recommended) ──────────────────
# 'with' automatically closes the file — even if an error occurs.
# This is the BEST PRACTICE for file handling in Python.

with open("superman.txt", "r") as f:
    content = f.read()
    print("\n── Reading with 'with' ──")
    print(content)
# File is automatically closed here — no need to call f.close()


# ── 5. Writing Multiple Lines with writelines() ──────────────

heroes = [
    "Batman - Dark Knight\n",
    "Iron Man - Genius Billionaire\n",
    "Spider-Man - Friendly Neighbourhood Hero\n"
]

with open("heroes.txt", "w") as f:
    f.writelines(heroes)   # writes a list of strings

print("✅ heroes.txt created.")

# Reading it back
with open("heroes.txt", "r") as f:
    for line in f:
        print(line.strip())


# ── 6. Exception Handling with Files ─────────────────────────
# Always handle errors when working with files.

try:
    with open("missing_file.txt", "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print("❌ Error: File not found!")

except PermissionError:
    print("❌ Error: You don't have permission to access this file.")

except Exception as err:
    print(f"❌ Unexpected error: {err}")


# ── 7. Checking if a File Exists ─────────────────────────────
import os

if os.path.exists("superman.txt"):
    print("✅ superman.txt exists")
else:
    print("❌ File does not exist")

# Other useful os functions
print(os.getcwd())         # current working directory
print(os.listdir("."))     # list all files in current directory


# ── 8. Working with File Paths ───────────────────────────────
import os

# Build paths safely (works on Windows, Mac, Linux)
folder = "my_folder"
file   = "data.txt"
path   = os.path.join(folder, file)
print(path)   # my_folder/data.txt  (or my_folder\data.txt on Windows)


# ── 9. Deleting and Renaming Files ───────────────────────────
# Uncomment to try these:

# os.remove("heroes.txt")               # delete a file
# os.rename("superman.txt", "clark.txt") # rename a file


# ── 10. Reading a File Line by Line (Memory Efficient) ───────
# For LARGE files, loop directly over the file object
# instead of loading everything into memory at once.

with open("superman.txt", "r") as f:
    print("\n── Line by line (memory efficient) ──")
    for line in f:              # Python reads one line at a time
        print(line.strip())


# ============================================================
#  Quick Recap
#  Mode    Purpose
#  ──────  ──────────────────────────────────────────────────
#  'r'     Read  (file must exist)
#  'w'     Write (creates / overwrites)
#  'a'     Append (adds to end)
#  'x'     Create new (error if file exists)
#
#  Best Practices:
#  ✅ Always use 'with open(...)' — auto-closes the file
#  ✅ Use strip() to remove trailing \n when reading lines
#  ✅ Wrap file ops in try-except for FileNotFoundError
# ============================================================

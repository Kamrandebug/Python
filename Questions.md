⭐ Level 1 — Warm Up (Q1–Q3)

Q1 — Personal Info Card

Ask the user for their name, age, and city. Then print a formatted info card like this:

==============================
   Name  : Ali
   Age   : 25
   City  : Lahore
   Born  : 2001
==============================
💡 Concepts: input(), type conversion, f-strings, arithmetic

Q2 — The Receipt Printer

Ask the user for 3 item names and their prices. Calculate and print a receipt with each item, a subtotal, 16% tax, and the final total — all aligned neatly.

-----------------------------
 Item         Price
-----------------------------
 Burger       Rs. 500.00
 Fries        Rs. 150.00
 Drink        Rs. 100.00
-----------------------------
 Subtotal     Rs. 750.00
 Tax (16%)    Rs. 120.00
 TOTAL        Rs. 870.00
-----------------------------
💡 Concepts: input(), float conversion, arithmetic operators, f-string formatting

Q3 — String Inspector

Ask the user to enter any sentence. Then print:

Total characters (with spaces)
Total characters (without spaces)
Number of words
The sentence in UPPERCASE and reversed
Whether the sentence contains the word "python" (case-insensitive)


💡 Concepts: string methods — len(), split(), replace(), upper(), in operator

⭐⭐ Level 2 — Getting Serious (Q4–Q7)

Q4 — The Smart Calculator

Ask the user for two numbers and an operator (+, -, *, /, //, %, **).
Perform the correct operation and print the result.
Handle the division by zero case gracefully.

Enter first number: 10
Enter operator: /
Enter second number: 0
❌ Error: Cannot divide by zero!
💡 Concepts: input(), type conversion, all arithmetic operators, comparison

Q5 — Odd/Even & Divisibility Checker

Ask the user for a number. Print:

Is it odd or even?
Is it divisible by 3, 5, or both? (FizzBuzz style)
Is it positive, negative, or zero?
Is it a single digit, double digit, or more?


💡 Concepts: modulus operator %, comparison operators, logical operators and/or

Q6 — The Username Validator

Ask the user to create a username. Check all these rules and print PASS ✅ or FAIL ❌ for each:

Must be between 5–15 characters long
Must start with a letter (not a number or symbol)
Must not contain spaces
Must be all lowercase

At the end, print whether the username is fully valid or not.

💡 Concepts: len(), string methods — isalpha(), islower(), startswith(), in operator, logical operators

Q7 — Temperature Converter

Ask the user:

Enter a temperature value
Enter the unit (C, F, or K)

Then convert it to the other two units and display all three.
Formulas:

°C to °F → (C × 9/5) + 32
°C to K  → C + 273.15
°F to °C → (F - 32) × 5/9


💡 Concepts: input(), float conversion, arithmetic operators, f-string formatting

⭐⭐⭐ Level 3 — Boss Level (Q8–Q10)

Q8 — The Bitwise Secrets Decoder

Ask the user for two integers. Then print a full report:

Result of &, |, ^, <<1, >>1 for both numbers
Whether each number is even or odd using bitwise & (NOT modulus!)
The larger of the two using only bitwise and comparison operators (no if statement allowed!)


💡 Concepts: bitwise operators, identity operators, arithmetic — all from the operators section

Q9 — The Data Type Detective

Ask the user to enter 5 different values one by one (they can type anything — numbers, decimals, words).
Your program must automatically detect and convert each input to the most appropriate type:

If it looks like an int → store as int
If it looks like a float → store as float
If it's "True" or "False" → store as bool
Otherwise → keep as str

At the end, print each value with its detected type and whether it is truthy or falsy.

💡 Concepts: type conversion, bool(), isinstance(), type(), string methods, membership operators

Q10 — The Mini Bank System

Build a simple bank account simulation in one single run (no loops needed):

Ask for the account holder's name and starting balance
Ask for a deposit amount — add it and show new balance
Ask for a withdrawal amount — subtract it, but if funds are insufficient, print a warning and don't deduct
Apply a 1.5% monthly interest on the final balance
Print a full account statement at the end with all transactions neatly formatted


💡 Concepts: input(), type conversion, arithmetic operators, comparison operators, f-string formatting, logical operators
# Discount System
# Ask the user to enter their total shopping bill. Apply discount:

# Above Rs. 5000 → 20% discount
# Above Rs. 2000 → 10% discount
# Otherwise → No discount

bill = float(input("Enter Your total shopping bill : "))

if bill >= 5000 :
  discount_amount = (20 / 100) * bill
  final_amount = bill - discount_amount
  print("You have got 20% Discount :" , final_amount)
elif bill > 2000 and bill < 5000:
  discount_amount = (10 / 100) * bill
  final_amount = bill - discount_amount
  print("You have got 10% Discount :" , final_amount)
else:
  print("Sorry ! You have got no discount on your shopping")

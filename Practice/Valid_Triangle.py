# Triangle Valid or Not
# Ask the user to enter three angles of a triangle. If they add up to 180, print "Valid Triangle" otherwise print "Invalid Triangle."

x = int(input("Enter angle X of the triangle : "))
y = int(input("Enter angle Y of the triangle : "))
z = int(input("Enter angle Z of the triangle : "))

if x+y+z == 180:
  print("Its a Valid Triangle")
else:
  print("Invalid Triangle")

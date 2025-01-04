from operator import truediv

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Base price
if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25
else:
    price = 9999
    print("\nError: Incompatible size.")

# Pepperoni?
if pepperoni == "Y":
   if size == "S":
       price += 2
   elif size == "M":
       price += 3
   elif size == "L":
       price += 3
   else:
       print("Error: Incompatible size.")

# Extra cheese?
if extra_cheese == "Y":
    price += 1

# Price print
print(f"Your final bill is: ${price}.")
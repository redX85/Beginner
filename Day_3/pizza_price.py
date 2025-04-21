print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

price=0
#the price for the different options for
#pizza sizes
if size == "S":
    price+=15
elif size == "M":
    price+=20
elif size == "L":
    price +=25
else:
    print("You didn't add the correct value")

if pepperoni == "Y" and size == "L":
    price += 3
elif pepperoni == "Y" and size == "M":
    price +=3
elif pepperoni == "Y" and size == "S":
    price += 2
else:
    price += 0

if extra_cheese == "Y":
    price += 1
else:
    price += 0
print(f"Your final bill is: ${price}.")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random
#I hashed some codes so that the processes occur in the "background"
alpha = random.choices(letters, k=nr_letters)
# print(alpha)
sym = random.choices(symbols, k=nr_symbols)
# print(sym)
num = random.choices(numbers, k=nr_numbers)
# print(num)
#now the values of the list are combined
a = alpha + sym + num
# print(a)
#let's shuffle the list
random.shuffle(a)
#then call it again to see the difference
# print(a)
#join combines the list elements of list a into a string
password = "".join(a)
print("This is your generated password:")
print(password)






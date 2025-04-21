print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n$"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15: \n"))
people = int(input("How many people to split the bill?\n"))

#this calculates the tip
tip_amount = bill*tip/100
#computes the amount each person will pay
each = (bill+tip_amount)/people
print(each)

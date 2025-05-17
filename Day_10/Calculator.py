def add(n1, n2):
    return n1 + n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def sub(n1, n2):
    return n1 - n2

operations = {
    "+": add, "*": mult,"/": div,"-": sub
}

# calculate = operations["+"](5,8)
# print(calculate)


import art
def calculator():
    restart = True
    while restart:
        print(art.logo)
        calculation = 0
        user_input_1 = float(input("what is the first number?: "))
        go_on = True
        while go_on:
            print( "+","\n-", "\n*", "\n/")
            sign = input("pick an operator: ")
            user_input_2 = float(input("what is the next number?: "))
            ans = operations[sign](user_input_1, user_input_2)
            calculation += ans
            print(f"{user_input_1} {sign} {user_input_2} = {ans}")
            should_we = input(f"Type 'y' to continue calculating with {calculation}, "
                        f"or type 'n' to start a new calculation: ").lower()
            if should_we == "n":
                go_on = False
                user_input_1 = 0
                restart = True
                print("\n"*20)
            else:
                user_input_1 = ans

calculator()

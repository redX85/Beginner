from art import logo
import random
print(logo)

# Create a number list
def chosen_number():
    number_list = []
    for i in range(101):
        number_list.append(i)
    to_guess = random.choice(number_list)
    print(f"The correct number is {to_guess}")
    return to_guess

# Choose difficulty
def difficultly():
    """For a chosen difficulty there will be an associated number of loops"""
    level = input("Choose your level, 'easy' or 'hard'? ")
    loops = 0
    if level == "easy":
        # you have 10 attempts
        loops = 10
        print(f"You have {loops} attempts left.")
        return loops
    elif level == "hard":
        # you have 5 attempts
        loops = 5
        print(f"You have {loops} attempts left.")
        return loops
    else:
        print("You have not chosen a difficulty!")

def guess_proximity(difficulty_function, chosen_from_list):
    value = chosen_from_list
    attempts = difficulty_function
    for i in range(attempts):
        try:
            guess = int(input("Choose a number: "))
            if attempts > 0:
                if guess > value:
                    print("The number is too high.")
                    attempts -= 1
                    print(f"You have {attempts} remaining attempts."+"\n"*1)
                    if attempts == 0:
                        print("You lost!")
                elif guess < value:
                    print("The number is too low.")
                    attempts -= 1
                    print(f"You have {attempts} remaining attempts."+"\n"*1)
                    if attempts == 0:
                        print("You lost!")
                else:
                    print(f"You got it the correct answer was {value}")
                    break
        except ValueError:
            print("You didn't add a number!")
            attempts -= 1
            print(f"You have {attempts} remaining attempts."+"\n"*1)
            if attempts == 0:
                print("You lost!")

guess_proximity(difficulty_function = difficultly(), chosen_from_list = chosen_number())
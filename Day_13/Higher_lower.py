import art
import game_data
import random

def game_page():
    """This is the front page of the game."""
    print(art.logo)

    # The first choice
    int_1 = random.randint(0, 49)
    name_1 = game_data.data[int_1].get("name")
    follower_count_1 = game_data.data[int_1].get("follower_count")
    description_1 = game_data.data[int_1].get("description")
    country_1 = game_data.data[int_1].get("country")

    # The second choice
    int_2 = random.randint(0, 49)
    name_2 = game_data.data[int_2].get("name")
    follower_count_2 = game_data.data[int_2].get("follower_count")
    description_2 = game_data.data[int_2].get("description")
    country_2 = game_data.data[int_2].get("country")

    # Display to user
    print(f"Compare A: {name_1}, a {description_1}, from {country_1}.")
    print(art.vs)
    print(f"Compare B: {name_2}, a {description_2}, from {country_2}.")

    return follower_count_1, follower_count_2

def follower_comparison(first, second):
    """Compares follower counts and returns 'a' or 'b'."""
    if first > second:
        return 'a'
    elif first < second:
        return 'b'
    else:
        return "none"

def my_guess_compare(comp, me):
    """Returns 'yes' if guess is correct, otherwise 'no'."""
    if me == comp:
        return "yes"
    else:
        return "no"

def score(guess, current_score):
    """Uses the game_page code to reproduce the initial page seen when initializing the game.
    The code also computes the score using an outer 'current_score' variable.\n
    The score will increase if the guess is correct and remain the same if not"""
    if guess == "yes":
        current_score += 1
        print("\n" * 20)
        print(art.logo)

        # New choices
        int_1 = random.randint(0, 49)
        name_1 = game_data.data[int_1].get("name")
        follower_count_1 = game_data.data[int_1].get("follower_count")
        description_1 = game_data.data[int_1].get("description")
        country_1 = game_data.data[int_1].get("country")

        int_2 = random.randint(0, 49)
        name_2 = game_data.data[int_2].get("name")
        follower_count_2 = game_data.data[int_2].get("follower_count")
        description_2 = game_data.data[int_2].get("description")
        country_2 = game_data.data[int_2].get("country")

        print(f"That's correct! Your current score: {current_score}")
        print(f"Compare A: {name_1}, a {description_1}, from {country_1}.")
        print(art.vs)
        print(f"Compare B: {name_2}, a {description_2}, from {country_2}.")

        # this returns the altered current score
        return current_score, follower_count_1, follower_count_2
    else:
        print("\n" * 20)
        print(art.logo)
        # This current_score remains the same as the one that would lie outside the function.
        print(f"You lose. Final score: {current_score}")
        return "no"

def game_play():
    x, y = game_page()
    # This is where the omitted score_total comes to chill
    # in the previous function it reset the score
    score_total = 0
    game_loop = True

    while game_loop:
        f_c = follower_comparison(first=x, second=y)
        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_input in ["a", "b"]:
            chosen = my_guess_compare(comp=f_c, me=user_input)
            result = score(guess=chosen, current_score=score_total)
            if result != "no":
                # Score_total is stored outside
                # x and y will be reused by the f_c code outside the loop
                score_total, x, y = result
            else:
                game_loop = False
        else:
            print("Type either 'a' or 'b'.")

game_play()

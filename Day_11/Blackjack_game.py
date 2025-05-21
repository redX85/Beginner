import random

import art

# Card list and starting hands
card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards = random.choices(card_list, k=2)
npc_cards = random.choices(card_list, k=2)

def calculate_score(cards):
    total = sum(cards)
    # Adjust for Aces (11 becomes 1 if needed)
    while total > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        total = sum(cards)
    return total

play = input("Do you want to play blackjack? Type 'y' or 'n': ")
if play == "y":
    # Game loop
    while True:
        my_score = calculate_score(my_cards)
        npc_score = calculate_score(npc_cards)

        print(art.logo)
        print(f"\nYour cards: {my_cards}, current score: {my_score}")
        print(f"Dealer's first card: {npc_cards[0]}")

        # Check for blackjack or bust
        if my_score == 21:
            print("Blackjack! You win!")
            break
        elif npc_score == 21:
            print(f"Dealer has {npc_cards}. Blackjack! You lose.")
            break
        elif my_score > 21:
            print("You went over 21. You lose.")
            break

        # Ask user if they want another card
        another_card = input("Do you want another card? (yes/no): ").lower()
        if another_card == "yes":
            my_cards.append(random.choice(card_list))
        else:
            # Dealer draws cards until they reach at least 17
            while npc_score < 17:
                npc_cards.append(random.choice(card_list))
                npc_score = calculate_score(npc_cards)

            print(f"\nYour final hand: {my_cards}, final score: {my_score}")
            print(f"Dealer's final hand: {npc_cards}, final score: {npc_score}")

            if npc_score > 21:
                print("Dealer busts! You win!")
            elif my_score > npc_score:
                print("You win!")
            elif my_score < npc_score:
                print("You lose!")
            else:
                print("It's a draw!")
            break
else:
    print("Bye!")
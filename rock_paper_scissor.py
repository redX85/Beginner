rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to the rock paper scissors Game \n The user inputs are 0 for rock, 1 for paper and 2 for scissors")
import random

#player art

player = int(input("Rock(0) Paper(1) or Scissors(2)? "))
if player == 0:
    print("player")
    print(rock)
elif player == 1:
    print("player")
    print(paper)
elif player == 2:
    print("player")
    print(scissors)
else:
    print("You didn't choose right")

#npc art
npc = random.randint(0,2)

if player == 0 or player == 1 or player == 2:

    if npc == 0:
        print("npc")
        print(rock)
    elif npc == 1:
        print("npc")
        print(paper)
    elif npc == 2:
        print("npc")
        print(scissors)
    else:
        print("try again!")

result = player - npc

# maths behind the game
# win condition
if result == -2 or result == 1:
    print("YOU WIN!")
# draw condition
elif result == 0:
    print("ITS A DRAW")
# loss condition
elif result == 2 or result == -1:
    print("YOU LOSE!")

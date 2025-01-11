# ASCII ART
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
###############
# appbrewery.github.io/python-day4-demo/
import random
computer = random.randint(0, 2)
# print(computer)

# Print human choice
human = int(input("What do you choose? 0 = Rock, 1 = Paper, 2 = Scissors.\n"))
if human == 0:
    print(rock)
elif human == 1:
    print(paper)
elif human == 2:
    print(scissors)
else:
    print("INVALID NUMBER")

# Computer Choice
print("The computer chose:")
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)

# computer = 0
# Who wins?

# Human Rock
if human == 0 and computer == 0:
    print("Its a Tie")
elif human == 0 and computer == 1:
    print("You Lose")
elif human == 0 and computer == 2:
    print("You Win")

# Human Paper
if human == 1 and computer == 0:
    print("You Win")
elif human == 1 and computer == 1:
    print("Its a Tie")
elif human == 1 and computer == 2:
    print("You Lose")

# Human Scissors
if human == 2 and computer == 0:
    print("You Lose")
elif human == 2 and computer == 1:
    print("You Win")
elif human == 2 and computer == 2:
    print("Its a Tie")

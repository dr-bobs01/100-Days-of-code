import random
import art

answer = random.randint(1, 100)
# print(answer)

lives = 0
finished = False

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
## user difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    lives = 1
    print("Invalid difficulty")

## actual game
while not finished:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    ## game logic
    if guess == answer:
        print("You Win!")
        finished = True
    elif guess > answer:
        print("Too big.")
        lives -= 1
    elif guess < answer:
        print("Too small.")
        lives -= 1
    if lives == 0:
        print("You Lose")
        finished = True

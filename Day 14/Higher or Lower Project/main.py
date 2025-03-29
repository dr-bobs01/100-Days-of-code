## import stuff
import random
import art
from game_data import data

## start stuff
print(art.logo)
score = 0
winner = ""
play = True

while play:
    # get the 2 people
    try:
        person1 = person2
        p1name = person1["name"]
        p1fol = person1["follower_count"]
        p1des = person1["description"]
        p1con = person1["country"]

    except NameError:
        person1 = random.choice(data)
        p1name = person1["name"]
        p1fol = person1["follower_count"]
        p1des = person1["description"]
        p1con = person1["country"]

    person2 = random.choice(data)
    p2name = person2["name"]
    p2fol = person2["follower_count"]
    p2des = person2["description"]
    p2con = person2["country"]

    # print them nice
    print(f"Person A: {p1name}, a {p1des}, from {p1con}")
    print(art.vs)
    print(f"Person B: {p2name}, a {p2des}, from {p2con}")

    # input awnser
    awnser = input("Who has more followers? Type 'A' or 'B': ").lower()
    # print(awnser)

    # clear screen
    print("\n"*20)
    print(art.logo)

    ## did ya win?
    # who better?
    if p1fol >= p2fol:
        winner = "a"
    else:
        winner = "b"
    # did player win?
    if awnser == winner:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        play = False

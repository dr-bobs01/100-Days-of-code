import random

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_check():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        return True
    else:
        return False

def card_show():
    print(f"Your cards {player_hand}, current score: {sum(player_hand)}")
    print(f"Computer's first card: {comp_hand[1]}")
    # print(player_hand)
    # print(comp_hand)
    # print(f"dev_comp: {sum(comp_hand)}")

play = play_check()
while play:
    hand_over = False
    player_hand = []
    comp_hand = []
    state = ""
    print(art.logo)
    ## Deal starting cards
    for i in range(0,2):
        player_hand.append(random.choice(cards))
        comp_hand.append(random.choice(cards))
    card_show()
    ## Check if player has blackjack ##
    if sum(player_hand) == 21:
        state = "win"
    ## Check if computer has blackjack ##
    elif sum(comp_hand) == 21:
        state = "lose"

    if state == "":
        more_card = input("Type 'y' to get another card, type 'n' to pass: ")

        while more_card == "y":
            player_hand.append(random.choice(cards))
            card_show()
            ## check if player has gone over 21
            if sum(player_hand) > 21:
                if 11 in player_hand:
                    if (sum(player_hand) - 10) > 21:
                        print("lose")
                else:
                    print("lose")
            more_card = input("Type 'y' to get another card, type 'n' to pass: ")

        ## computer plays
        while sum(comp_hand) < 17:
            ## Computer draws a card
            comp_hand.append(random.choice(cards))

        if sum(comp_hand) > 21:
            print("You win!")
        elif sum(player_hand) == sum(comp_hand):
            print("Draw!")
        elif sum(player_hand) > sum(comp_hand):
            print("You win!")
        elif sum(player_hand) < sum(comp_hand):
            print("You lose!")

    else:
        print(f"You {state}!")

    play = play_check()

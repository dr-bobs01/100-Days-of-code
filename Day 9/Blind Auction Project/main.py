# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

bids = {}

more_people = True
while more_people:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: £"))
    bids[name] = price
    if input("Are there any other bidders? Type 'yes or 'no'\n").lower() == "no":
        more_people = False
    else:
        print("\n" * 20)
    # print(bids)

highest_price = 0
winner = ""
for i in bids:
    person = i
    price = bids[i]
    if price > highest_price:
        highest_price = price
        winner = person

print(f"The winner is {winner} with a bid of £{highest_price}")

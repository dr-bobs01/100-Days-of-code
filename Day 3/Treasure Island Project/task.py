print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

a = input("Go left or right?\n")
if a == "Left" or a == "left":
    print("You come across a lake.")
    b = input("Type Wait to wait for a boat. type Swim to swim across\n")
    if b == "Wait" or b == "wait":
        print("You have arrived at the island. There are 3 doors")
        c = input("Which one do you go through? Red, Yellow or Blue\n")
        if c == "Red" or c == "red":
            print("The room was engulfed in flames! You died")
        elif c == "Blue" or c == "blue":
            print("The room was full of water and washed you away. You died")
        elif c == "Yellow" or c == "yellow":
            print("You found the treasure!You win!")
        else:
            print("That door doesn't exist. Game over")
    else:
        print("You drowned")
else:
    print("You fell in a hole and died.")
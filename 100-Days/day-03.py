# Day-03 [Control flow and logical operators]

# Exercise of voting system
# age = int(input("Enter your age : "))
# if age >= 18:
#     print("You can vote !!")
# else :
#     print("You can not vote !!")



# Final project of the day
# Final project of the day
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/____/___
*******************************************************************************
''')
print("Welcome to Treasure Island. \n")
print("Your mission is to find the treasure. \n")

choice1 = input("Choose 'left' or 'right': ").lower()
if choice1 ==  "left":
    print("You arrive at Treasure Island. \n")
    choice2 = input("Choose 'swim' or 'wait': ").lower()
    if choice2 == "wait":
        print("You arrive to next level \n")
        choice3 = input("which door : 'Red' or 'Blue' or 'Yellow' : ").lower()
        if choice3 == "red":
            print("Burned by fire!! \n")
            print("Game Over!\n")
        elif choice3 == "blue":
            print("Eaten by Beasts !! \n")
            print("Game Over!\n")
        elif choice3 == "yellow":
            print("You win !! \n")
        else:
            print("Game Over!! \n")
    else:
        print("Attacked by trout !! \n")
        print("Game Over!\n")
else:
    print("Fall into a hole !! \n")
    print("Game Over!\n")

print("Game Over!\n")
print("Game Over!\n")
print("Game Over!\n")
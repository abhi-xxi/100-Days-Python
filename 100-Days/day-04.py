#Randomisation
import random   # This import the random module  # You can import your own module || note -> try

random_num = random.randint(1, 10)   # Here a<=N<=b
print(random_num)

random_num_0_to_1 = random.random() * 10   # here 0<=N<1
print(random_num_0_to_1)

random_float_num = random.uniform(1, 10)   #
print(random_float_num)

#Exericse
#Heads and tail
random_choice = random.randint(1, 2)
if random_choice == 1:
    print("Head")
else :
    print("Tail")

# List -> Are the array of the python

name = ["Virat", "Dhoni", "Rohit", "Hardik" ]
print(name[0])
print(name[1])

# In list there are positive as well as negative index number
print(name[-1])

# Read about different functions of list like append, extend, etc

# Exercise - who will pay the bill ?

cust_name = ["abhi", "abhinav", "deadpool", "peter"]

choice = random.randint(0, 3)
print("Who will pay the bill ? ")
print("Answer = " + str(cust_name[choice]))

# Day- 04 final project
# Rock-Paper-Scissor Game
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
comp_choice = random.randint(0, 2)

rock = r'''
    _    
   | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
'''
paper = r'''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
'''
scissors = r'''
       (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
'''

Game = [rock, paper, scissors]

if user_choice < 0 or user_choice > 2:
    print("Invalid choice! You lose.")
else:
    print("You chose:\n", Game[user_choice])
    print("Computer chose:\n", Game[comp_choice])

    if user_choice == comp_choice:
        print("It's a draw!")
    elif (user_choice == 0 and comp_choice == 2) or \
         (user_choice == 1 and comp_choice == 0) or \
         (user_choice == 2 and comp_choice == 1):
        print("You win!")
    else:
        print("You lose!")

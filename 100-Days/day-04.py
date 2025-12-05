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


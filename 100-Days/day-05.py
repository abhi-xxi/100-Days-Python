# Loops
import random

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

student = [12, 3, 4, 5, 6, 75, 5,6 , 2, 45, 5,6 ,5, 6, 33, 34, 56, 3,4 , 5, 6, 7]

sum_using_function = sum(student)
print(sum_using_function)

total = 0
for score in student:
    total += score

print("Without using function : " )
print(total)

for num in range(1, 101, 1):
    if num % 3 == 0 :
        print("Fizz")
    elif num % 5 == 0 :
        print("Buzz")
    if num % 3 == 0 and num % 5 == 0 :
        print("FizzBuzz")
    print(num)


# Final Project of the day
# Password Generator
letters = []
for i in range(1, 27, 1):
    letters.append(chr(ord('a') + i - 1))

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
need_letters = int(input("How many letters would you like to generate? \n"))
need_numbers = int(input("How many numbers would you like? \n"))
need_symbols = int(input("How many symbols would you like? \n"))

#Easy level
# password = ""
# #need letters
# for char in range(0, need_numbers):
#     password = random.choice(letters)
#
# for char in range(0, need_symbols):
#     password += random.choice(symbols)
#
# for char in range(0, need_numbers):
#     password += random.choice(numbers)
#
# print(password)

#Hard level
password_list = []
for i in range(need_letters):
    password_list.append(random.choice(letters))
for i in range(need_numbers):
    password_list.append(random.choice(numbers))
for i in range(need_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is {password}")
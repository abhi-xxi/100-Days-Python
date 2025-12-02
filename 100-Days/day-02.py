# Subscripting
print("Hello"[0])

# String
print("123" + "345")

# Integer = Whole number
print(123 + 345)

# Large Integers
print(123_456_789)

# Float = Floating Print Number
print(3.14159)

# Boolean
print(True)
print(False)

# Type Checking using - type() function
print(type("Hello"))

# TypeCasting
print(int("123") + int("345"))

# Exercise
# BMI Calculator
height = 1.65
weight = 70
bmi = weight / height **2
print(bmi)

# Day-02 Final project
print("Welcome to the tip Calculator!")
bill = float(input("What was the total bill ? "))
tip = int(input("How much tip would you like ? 10, 12, or 15? "))
people = int(input("How many people to split the bill ?"))
bill_with_tip = tip / 100 * bill + bill 
print(bill_with_tip)

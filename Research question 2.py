# Research Question 2: Boolean-Returning Functions

# The lecture demonstrates functions that return Boolean values.

# a) Write a function multipleof3(x) that returns True if x is a multiple of 3, and False otherwise.
def multipleof3(x):
    return x % 3 == 0

print(multipleof3(9))
print(multipleof3(10))

# b) Write similar Boolean-returning functions for:
# is_even(n): Returns True if n is even
def is_even(n):
    return n % 2 == 0

print(is_even(8))
print(is_even(7))

# is_positive(n): Returns True if n > 0
def is_positive(n):
    return n > 0

print(is_positive(5))
print(is_positive(-3))

# is_valid_grade(grade): Returns True if grade is between 0 and 100
def is_valid_grade(grade):
    return 0 <= grade <= 100

print(is_valid_grade(85))
print(is_valid_grade(120))

# c) Research how Boolean-returning functions are used in if statements:
# python
# if is_even(number):
#    print("The number is even")
#--> Boolean-returning functions can be used directly in an if statement. If the function returns True, the code inside the if block executes.

def is_even(number):
    return number % 2 == 0

number = 6

if is_even(number):
    print("The number is even")
else:
    print("The number is odd")

# d) Write a program that uses Boolean-returning functions to validate user input.
# Deliverable: Working Boolean-returning functions and a validation program.

def is_positive(n):
    return n > 0

def is_valid_grade(grade):
    return 0 <= grade <= 100

age = int(input("Enter your age: "))
grade = float(input("Enter your grade: "))

if is_positive(age):
    print("Valid age")
else:
    print("Invalid age")

if is_valid_grade(grade):
    print("Valid grade")
else:
    print("Invalid grade")
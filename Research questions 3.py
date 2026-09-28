# Research Question 3: Function Composition and Reusability
# The lecture shows functions calling other functions and functions with multiple parameters.
# Tasks: a) Write a program that demonstrates function composition:

def function3():
    print("Function 3 is executed")

def function2():
    print("Function 2 is executed")
    function3()

def function1():
    print("Function 1 is executed")
    function2()

def main():
    function1()

main()

# b) Write a fruitful function calculate_grade(score) that returns a letter grade. Then write another function display_result(score) that calls calculate_grade and prints the result.
def calculate_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"
# c) Research the concept of modular programming. How do functions support modularity and code reuse?
# Definition

# -->Modular programming is a programming technique that divides a large program into smaller, independent functions or modules.

# How Functions Support Modularity and Code Reuse

#1. Improves readability

#2. Smaller functions are easier to understand.

#3. Reduces code duplication

#4. The same function can be reused multiple times.

#5. Simplifies testing

#6. Each function can be tested separately.

#7. Makes maintenance easier

#8. Changes can be made in one function without affecting the entire program.

#9. Promotes code reuse

#10. Functions written once can be used in different programs.

# d) Refactor a long, monolithic program (provided below) into smaller, reusable functions:
# python
def get_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2


def calculate_sum(num1, num2):
    return num1 + num2


def calculate_difference(num1, num2):
    return num1 - num2


def calculate_product(num1, num2):
    return num1 * num2


def main():
    num1, num2 = get_numbers()

    print("Sum:", calculate_sum(num1, num2))
    print("Difference:", calculate_difference(num1, num2))
    print("Product:", calculate_product(num1, num2))


main()

# Deliverable: Function composition program, grade calculator, and refactored modular program.
 
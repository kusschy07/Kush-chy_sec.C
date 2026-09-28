# Research Question 4: Practical Function Problems
# The programming lab contains practical function exercises

# Tasks: a) Write a function HowLongUntil() that (from the lab):


# Prompts the user for a month and day

from datetime import date


def HowLongUntil():
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    significance = input("Enter the significance of the date: ")

    today = date.today()

    target_date = date(today.year, month, day)

    # If the date has already passed this year,
    # use the date in the next year.
    if target_date < today:
        target_date = date(today.year + 1, month, day)

    days = (target_date - today).days

    return "It is " + str(days) + " days until " + significance


print(HowLongUntil())

# b) Write a function that implements the "Which Opera Character Are You?" flowchart (from the lab):
def opera_character():
    sociopath = input("Are you a sociopath? (yes/no): ").lower()

    if sociopath == "yes":
        power = input("Do you seek power? (yes/no): ").lower()

        if power == "yes":
            return "Scarpa"
        else:
            return "Don Giovanni"

    else:
        outgoing = input("Are you outgoing? (yes/no): ").lower()

        if outgoing == "yes":
            independent = input("Are you independent? (yes/no): ").lower()

            if independent == "yes":
                return "Carmen"
            else:
                return "Figaro"

        else:
            magical = input("Do you enjoy magic? (yes/no): ").lower()

            if magical == "yes":
                return "Queen of the Night"
            else:
                return "Mimi"

character = opera_character()
print("You are:", character)

# c) Write a function calculate_age(birth_month, birth_day, birth_year, current_month, current_day, current_year) that returns the person's age in years, accounting for whether their birthday has passed this year.

def calculate_age(birth_month, birth_day, birth_year,
                  current_month, current_day, current_year):

    age = current_year - birth_year

    # Check if birthday has not occurred yet this year
    if (current_month, current_day) < (birth_month, birth_day):
        age -= 1

    return age

# d) Write a function that determines if a given year is a leap year. A year is a leap year if:

def is_leap_year(year):

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(is_leap_year(2024))
print(is_leap_year(1900))
print(is_leap_year(2000))
print(is_leap_year(2025))
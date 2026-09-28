#a) Research the return statement in Python:

# Syntax: return [expression]
#-->The return statement is used inside a function to send a value back to the place where the function was called return.
# For example
def add(a, b):
    return a + b

# What happens when return is executed?
# -->The function immediately stops running.
# -->Any code after return is not executed.

# What happens if a function has no return statement?
# -->Python automatically returns None.

# b) Write functions that demonstrate:
# Returning a single value: return answer
def get_answer():
    answer = 42
    return answer

print(get_answer())

# Returning a computed value: return "The answer is " + str(answer)
#--> The function can return a calculation together with text

def add_numbers(x, y):
    answer = x + y
    return "The answer is " + str(answer)

result = add_numbers(10, 20)
print(result)

# Returning multiple values: return x, y (returns a tuple)
#--> A function can return more than one value. Python automatically groups them into a tuple.

def get_values():
    x = 10
    y = 20
    return x, y

result = get_values()
print(result)

# c) Compare the following:
# Sum3Nums(4,5,6) - prints result
def Sum3Nums(a, b, c):
    total = a + b + c
    print("Sum =", total)

Sum3Nums(4, 5, 6)

# FruitfulSum3Nums(1,2,3) - returns result

def FruitfulSum3Nums(a, b, c):
    answer = a + b + c
    return answer
result = FruitfulSum3Nums(1, 2, 3)
print(result)


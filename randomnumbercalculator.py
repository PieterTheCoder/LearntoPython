import random

n3 = random.randint(1,100)
n4 = random.randint(1,100)

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

operation = {
    "*": multiply,
    "/": divide,
    "+": add,
    "-": subtract
}

print("Welcome to the random calculator number generator")

op = random.choice(list(operation))
func = operation[op]
result = func(n3, n4)

print(f"{n3} {op} {n4} = {result}")

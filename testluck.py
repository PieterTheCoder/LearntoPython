import random
print("WELCOME TO THE LUCK TEST\nIn here we gonna test from 1-200 if you hit 100/200 that 100 pure luck")
number = random.choice(range(1, 201))
print(number)
if number == 100 and 200:
    print("Hooray, you are lucky.")
else:
    print("Try again till lucky.")
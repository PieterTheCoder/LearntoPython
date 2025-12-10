import string
import time
print("Loading...")
time.sleep(1)
print("Password Strength Checker")
password = input("Enter your password: ")
score = 0
if len(password) >= 8:
    score += 1
if any(char.isdigit() for char in password):
    score += 1
if any(char.islower() for char in password) and any(char.isupper() for char in password):
    score += 1
symbols = string.punctuation
if any(char in symbols for char in password):
    score += 1
if score <= 1:
    print("Strength: Weak")
elif score == 2:
    print("Strength: Medium")
else:
    print("Strength: Strong")

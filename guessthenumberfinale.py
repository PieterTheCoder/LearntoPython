import random

HARD = 5
EASY = 10

def compare(u_guess, c_guess, attempt):
    if u_guess > c_guess:
        print("Too high")
        return attempt - 1
    elif u_guess < c_guess:
        print("Too low")
        return attempt - 1
    else:
        print("You guessed correctly")

def choose_difficulty():
    diff = input("Choose a difficulty level 'easy' or 'hard' \n").lower()
    if diff == "easy":
        return EASY
    else:
        return HARD

def game():
    print(""" _____ _     _____ ____  ____    _____ _     _____   _      _     _      ____  _____ ____ 
    /  __// \ /\/  __// ___\/ ___\  /__ __Y \ /|/  __/  / \  /|/ \ /\/ \__/|/  _ \/  __//  __\
    | |  _| | |||  \  |    \|    \    / \ | |_|||  \    | |\ ||| | ||| |\/||| | //|  \  |  \/|
    | |_//| \_/||  /_ \___ |\___ |    | | | | |||  /_   | | \||| \_/|| |  ||| |_\\|  /_ |    /
    \____\\____/\____\\____/\____/    \_/ \_/ \|\____\  \_/  \|\____/\_/  \|\____/\____\\_/\_\
                                                                                              """)
    print("Welcome to Number Guessing Project")
    print("It will be 1 through 100")
    attempt = choose_difficulty()
    destination = random.randint(1, 101)

    guess = 0
    while guess != destination:
        print(f"You have {attempt} attempts remaining to guess the number")
        guess = int(input("Make a Guess: "))
        attempt = compare(guess, destination, attempt)
        if attempt == 0:
            print("You're run ot of attempt, You lose.")
            return
        elif guess != destination:
            print("Keep Guessing")

game()
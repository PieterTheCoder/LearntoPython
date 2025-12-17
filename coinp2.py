import random
print("=== Coin Flip ===")
choice = input('Choose a coin to flip (h/t)? ')
result = random.choice(['h', 't'])
if choice.lower() == result:
    print(f'You win! congrats {result}')
else:
    print(f'You lost! {result}')
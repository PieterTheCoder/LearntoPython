import random
print('=== Coin Flip ===')
input('Choose Heads or Tails (H/T)? ')
result = random.choice(['H', 'T'])
if choice.upper() == result:
    print(f'You win! Coin: {result}')
else:
    print('f'You lose! Coin: {result}')
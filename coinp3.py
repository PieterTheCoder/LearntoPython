import random
print('Mastering...')
choice = input('Choose a coin to flip [H/T]')
result = random.choice(['H', 'T'])
if choice.upper == result:
   print(f'You Win {result}')
else:
   print(f'You Lose {result}')
import random
print('Mastering...')
choice = input('Choose [H/T]')
result = random.choice(['H'/'T'])
if choice == result:
   print(f'You Win {result}')
else:
   print(f'You Lose {result}')
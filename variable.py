print('Simple score activity')
Score = 0
valid = True
print(f'You wake up from the sleep you are in bedroom at 22.00 PM. You bored and get some activity to help you. Score now: {Score}')
print('(A). Sleep Again')
print('(B). Play video game')
print('(C). Learn English')
choice = input('(A/B/C)')
if choice.upper() == 'A':
    Score -= 5
    print(f"You sleep alot. Score: {Score}")
elif choice.upper() == 'B':
    Score += 5
    print(f"You clear the stress and learn about the game mechanics and strategies. Score: {Score}")
elif choice.upper() == 'C':
    Score += 10
    print(f"You are mastering English. Score: {Score}")
else:
    print("Type A/B/C according to your instinct")
    valid = False

if valid:
    if Score >= 10:
        print("You are doing good with your choice 🔥")
    elif Score >= 0:
        print("You can do better than play game but its ok, because still training the brain inside your head 🙂")
    else:
        print("Come on you can still do better activities tho 😴")
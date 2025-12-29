import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock, Paper, Scissors its you against computer\n0 for rock 1 for paper 2 for scissors ")
decision = input()
if decision == "0":
    print(rock)
elif decision == "1":
    print(paper)
elif decision == "2":
    print(scissors)
computer_choice = random.randint(0,2)
if computer_choice == 0:
    print(f"computer choose:\n{rock}")
elif computer_choice == 1:
    print(f"computer choose:\n{paper}")
elif computer_choice == 2:
    print(f"computer choose:\n{scissors}")

if decision == "0" and computer_choice == 0:
    print("Draw")
elif decision == "1" and computer_choice == 1:
    print("Draw")
elif decision == "2" and computer_choice == 2:
    print("Draw")
elif decision == "2" and computer_choice == 1:
    print("You win")
elif decision == "2" and computer_choice == 0:
    print("You lose")
elif decision == "0" and computer_choice == 1:
    print("The computer win")
elif decision == "0" and computer_choice == 2:
    print("You win")
elif decision == "1" and computer_choice == 0:
    print("You win")
elif decision == "1" and computer_choice == 2:
    print("You lose")
else:
    print("Invalid Choice")
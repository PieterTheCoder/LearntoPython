choice = ""
score = 0
print("You wake up midnight and want to be productive because motivation 3 PM")
print("A. Sleep again")
print("B. Play some game")
print("C. Calisthenics and learn english")
while choice not in("A", "B", "C"):
    choice = input("Choose a choice (A, B, or C): ").upper()
if choice == "A":
    score -= 5
elif choice == "B":
    score += 5
elif choice == "C":
    score += 10
print(f"Your final score was {score}")

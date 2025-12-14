print("How is your mood today?")
print("Welcome to mood daily save.")
mood = input("Mood: ")
date = input("Date: ")
with open("mood.txt", "a") as file:
    file.write(date + " | Mood: " + mood + "\n")
print("Your mood has been saved")
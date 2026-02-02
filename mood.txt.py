print('Daily Mood Tracker')
date = input('Today date: ')
mood = input('Mood now: ')
with open ("mood.txt", "a") as file:
    file.write(date + "| Mood: " + mood + "\n")
print("Your mood has been saved")
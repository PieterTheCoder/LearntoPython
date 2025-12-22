import random
import time
activities = [ "Jogging", "Study", "Socializing", "Play with your friend", "Help Parents" ]
activity = random.choice(activities)
print("Roll a dice for your random activity this day...")
time.sleep(1)
print(activity)
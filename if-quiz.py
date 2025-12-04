import time

while True:
    print("Hello World!")
    Answer = input("Are speed limit at Indonesia highway is 100(Km/s)? (T/F): ")
    if  Answer.upper() == "T":
        print("You right, well done.")
        break
    elif Answer.upper() == "F":
        print("Wrong, be careful at the highway")
        break
    else:
        print("Just answer T/F")
    time.sleep(2)
import time

while True:
    Answer = input("Do you know who the creator of the anime One Piece is? (Y/N) ")

    if Answer.upper() == "Y":
        name = input("Who is it? ")
        if name.strip().lower() == "eiichiro oda":
            print("Congrats, You did it!")
            break
        else:
            print("Try again!")

    elif Answer.upper() == "N":
        print("It's Eiichiro Oda")
        break

    else:
        print("Read and try typing Y/N to the best of your ability. Y means Yes, so you already know. N means No, so you don't know yet.")

time.sleep(2)

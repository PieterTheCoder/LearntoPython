print("WELCOME TO WHILE TRUE.PY")
while True:
    choice = input("I want you to choice from a to c\n").lower()
    if choice not in ("a", "b", "c"):
        print("Invalid Choice")
    else:
        print("You did it")
        break
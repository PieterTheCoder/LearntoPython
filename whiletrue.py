while True:
    print("WELCOME TO WHILE TRUE.PY")
    choice = input("I want you to choice from a to c").lower()
    if choice not in ("a", "b", "c"):
        print("Invalid Choice")
    else:
        print("You did it")

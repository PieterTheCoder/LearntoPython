import time
hp = 100
stage = 1
print("Welcome to the Mini Story!")
print("\nYou wake up at a city as resident.")
print("You wake up with a fit, strong body and bright emotions.")
print("You are also an athlete from krav maga")
print(f"Your HP = {hp} ")
time.sleep(2)

while hp > 0:
    if stage == 1:
        print("\nYou walk across the city and you see something strange at the end of the road.")
        print("(T)  Check the strange thing at the end of the road")
        print("(F)  Pretend not to know and just pass, by like nothing is strange.")
        choice = input('You got two choice pick it (T/F)? ')

        if choice.upper() == 'T':
            stage = 2

        elif choice.upper() == 'F':
            stage = 3
            print("\nYou keep walking. A detective later finds your fingerprints. You're safe for now.")
            continue

        else:
            print("\nPick the two option.")
            continue

    if stage == 2:
        print("\nYou found someone get bullied by two person that bring a knife.")
        print("(K)  Call Police.")
        print("(L)  Run and look for the police who are on the road.")
        print("(P)  Fight the bullies")
        consequence = input("You get three choice pick it (K/L/P)")

        if consequence.upper() == 'K':
            hp -= 70
            print("\nYou step back and secretly call the police. But the bullies notice your movements. They chase you, "
                  "forcing you to run for your life. You escape, but the victim is taken away.")
            time.sleep(1)
            print(f"You manage to escape but you're badly wounded. HP now = {hp}")
            stage = 3
            continue

        elif consequence.upper() == 'L':
            hp -= 50
            print("\nYou sprint down the road looking for help. The street is nearly empty—until two men appear. But instead"
                  " of helping, they block your way; they're part of the same gang. You’re outnumbered and get captured")
            time.sleep(1)
            print(f"They shock you with a taser before you escape. HP now = {hp}")
            stage = 3
            continue

        elif consequence.upper() == 'P':
            print("\nYou assess the situation quickly. Using your krav maga training, you lure the bullies into a narrow"
                  " alley. There, you grab a discarded crowbar and neutralize them after that you call the Police and the"
                  " Police sent them to prison. For the victim he's now on hospital")
            stage = 3
            continue

        else:
            print("\nPick the three option.")
            continue

if stage == 3:
    print("\n ~ End of Chapter 1 ~")

if hp <= 0:
    print('\nYou collapse from your injuries... Game Over')
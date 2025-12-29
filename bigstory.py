print('''                   _.--.    
                 ."  ."      ".  ".
                ;  ."    /\    ".  ;
                ;  '._,-/  \-,_.`  ;
                \  ,`  / /\ \  `,  /
                 \/    \/  \/    \/
                 ,=_    \/\/    _=,
                 |  "_   \/   _"  |
                 |_   '"-..-"'   _|
                 | "-.        .-" |
                 |    "\    /"    |
                 |      |  |      |
         ___     |      |  |      |     ___
     _,-",  ",   '_     |  |     _'   ,"  ,"-,_
   _(  \  \   \"=--"-.  |  |  .-"--="/   /  /  )_
 ,"  \  \  \   \      "-'--'-"      /   /  /  /  ".
!     \  \  \   \                  /   /  /  /     !
:      \  \  \   \                /   /  /  /      :
''')
print("As a knight you get command from your king to explore dungeon.\nThe further you explore the dungeon you see mysterious person bargaining you think...")
print("You are curious about that mysterious person but, you know the consequences.\nYou have two choice. But there is a secret ending if you type the first letter of my name.")
decision = input("  1. Leave the mysterious person and continue your exploration.\n  2. Go to the mysterious person.\n    Type 1 or 2\n    ")
if decision == "1":
    print("You get chased by the mysterious person offering you some potion. You feel kinda strange....")
    choice = input("  1. Take the offer.\n  2. Reject the offer.\n    Type 1 or 2\n    ")
    if choice == "1":
        print("You keep the potion and find some bandit that looks at your armor.\n Wounded because the bandit,you take out the potion he offered.")
        potion = input("  1. Drink it.\n  2. Throw the potion.\n    Type 1 or 2\n    ")
        if potion == "1":
            print("You get poisoned and dead because you drink the potion. The bandit rob you and steal your armor.")
        elif potion == "2":
            print("You get killed by the bandit that wanted your item. I think you should drink it?")
        else:
            print("Invalid choice")
    elif choice == "2":
        print("You get hunted by the dungeon people. Why?\nBecause the mysterious person place the bounty on you.\nHe want your armor and the item you have, You survive the massacre but it won't last long...")
    else:
        print("Invalid choice")
elif decision == "2":
    print("You get killed by the mysterious person. He steal all your item.")
elif decision == "P":
    print('''                                      \_/
                                    --(_)--
                                      / \
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^           ^^^^^
|||                |||||||||||||||    ,-.    |||||
     ^`````````.       |||||||||||_.-'  \\_.-|||||
    / \         \           ||||||           |||||
   / ! \  ``     \              ||           |||||
  / "!  \     ``  \                  )
 /___!___\_________\                (
                                    __      @==)
                                   (_))    @_@__)
                                   ''``   @@_@___)''')
    print("You disobeyed the king's orders and lived a happy life because you worked in the devil's kingdom.")
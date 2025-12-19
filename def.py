def damaged(hp):
    hp -= 20
    return hp

hp = 100
hp = damaged(hp)
print('HP now:', hp)
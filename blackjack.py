import random
def deal_cards():
    """Generate random cards and return them"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """calculate score of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose. Computer has blackjack."
    elif u_score == 0:
        return "Win with a blackjack."
    elif u_score > 21:
        return "You went over. You lose."
    elif c_score > 21:
        return "Computer went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"
def restart_game():
    print(r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    run = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not run:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} and the total score {user_score}")
        print(f"Computer first card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            run = True
        else:
            draw_card = input("'y' to draw another card 'n' to pass: ").lower()
            if draw_card == 'y':
                user_cards.append(deal_cards())
            else:
                run = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards} and the final score: {user_score}")
    print(f"Computer final hand: {computer_cards} and the final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play the game, type 'y' or 'n'").lower() == 'y':
    print("\n" * 20)
    restart_game()

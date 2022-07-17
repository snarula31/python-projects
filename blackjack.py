import random


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    score = sum(cards)
#    return score

    if score == 21 and len(cards) == 2:
        return 0

    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        return score


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer has Blackjack, You lose!"
    elif user_score == 0:
        return "Blackjack, You Win!!"
    elif user_score > 21:
        return "You lose!"
    elif computer_score > 21:
        return "You Win!!"
    elif user_score > computer_score:
        return "You win!!"
    else:
        return "You lose"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User's cards: {user_cards}, current score is: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Type 'y' to draw a card or 'n' to halt: ")
            if choice == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_scores = calculate_score(computer_cards)
    print(
        f" Your final hand is:{user_cards} and your final score is {user_score} ")
    print(
        f"Computer's final hand is {computer_cards} and it's final score is {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of blackjack?(Type 'y' or 'n': "):
    play_game()

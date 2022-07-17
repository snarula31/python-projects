from art import logo, vs
import random
from game_data import data
import os


def format_data(account):
    """ format the game data in a representable form."""
    account_name = account['name']
    account_descrip = account['description']
    account_place = account['country']
    return f"{account_name}, a {account_descrip}, from {account_place}"


def evaulate(guess, a_followers, b_followers):
    """ check if user's guess is correct"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


# add art
# print(logo)
score = 0
account_b = random.choice(data)
game_should_continue = True

while game_should_continue:

    # generate random account from game data
    account_a = account_b
    account_b = random.choice(data)
    # if account_b == account_a:
    #    account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # ask user for guess
    user_guess = input("Who has more followers?: ").lower()
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_corret = evaulate(user_guess, a_follower_count, b_follower_count)

    os.system('cls')
    print(logo)
    # evaluation
    if is_corret:
        score += 1
        print(f"You're correct!. Current score is {score}.")
    else:
        game_should_continue = False
        print(f"You got wrong!. Final score is {score}")
        # score keeping

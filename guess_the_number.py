from random import randint

EASY_LEVEL_TURNS =10
HARD_LEVEL_TURNS = 5

def evaluation(guess, answer, turns):
    if guess>answer:
        print("Too High")
        return turns - 1
    elif guess<answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You guessed the correct ans!")


def difficulty():
    #SETS difficulty level of the game
    level = input("Choose difficulty of the game(type 'easy' of 'hard'): ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the NUMBER GUESSING GAME!")
    print("I'm thinking of a number between 1-100")
    answer = randint(0,100)
    print(f"The correct answer is {answer}")

    turns = difficulty()
    
    guess = 0

    while guess!= answer:
        print(f"You have {turns} attempts remaining to guess the answer.")

        guess = int(input("make a guess: "))
        turns = evaluation(guess,answer,turns)
        if turns == 0:
            print("You have run out of guesses, you lose!")
            return


game()

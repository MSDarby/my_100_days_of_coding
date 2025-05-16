import random
import guessinggame_art

EASY_LEVEL = 10
HARD_LEVEL = 5

def guessing(number, guesses, turns):
    if number > guesses:
        print("Too Low")
        return turns - 1
    elif number < guesses:
        print("Too high")
        return turns - 1
    else:
        print(f"You git it! The answer was {number}")


def difficulty():
    game_type = input("Choose a difficulty - type 'hard' or 'easy':").lower()
    if game_type == 'hard':
        return HARD_LEVEL
    elif game_type == 'easy':
        return EASY_LEVEL
    else:
        print("incorrect input. game over!")


def game():
    print(guessinggame_art.logo)
    print("Welcome to my Number Guessing Game!")
    print("I am thinking about a number between 1 and 100.\n"
          "Can you guess what number it is?")

    num = random.randrange(100)
    turn = difficulty()

    while turn > 0:
        print(f"You have {turn} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turn = guessing(num, guess, turn)

        if turn == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != num:
            print("Guess again.")


game()

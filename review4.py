"""
Splitting the functions to increase readability and follow the SOLID principles
"""

import random


def _exit_from_the_game(message):
    print(message)
    exit()


def ask_if_player_wants_to_play():

    print(
        "Hello! Welcome to Bee's Number Guessing Game!\nIn this game, you'll have "
        "to try to guess the number I'm thinking of.\nYou have three tries to "
        "guess correctly, in three different levels of difficulty.\nAre you ready "
        "to play?"
    )
    return {
        "YES": lambda: print("Great! Let's get started!"),
        "NO": lambda: _exit_from_the_game("Aw, that's too bad. ): Maybe next time!"),
    }.get(
        input("Please type 'YES' or 'NO' to continue: "),
        lambda: _exit_from_the_game(
            "Oops! You put an invalid option. Please try again."
        ),
    )()


def _check_ser_guess(current_tries, max_guess):
    user_guess_2 = int(input("Guess: "))
    comp_guess_2 = random.randint(1, max_guess)
    did_user_guessed = user_guess_2 == comp_guess_2

    if did_user_guessed:
        print("Correct! Onto the next level.")
        return (current_tries, current_tries > 0 and not did_user_guessed)

    print("Sorry! That's not correct. Please try again.")
    current_tries -= 1
    print(f"You have {current_tries} tries left.")
    return (current_tries, current_tries > 0 and not did_user_guessed)


def _ask_for_next_guess(current_tries, max_guess):
    have_not_guessed = True

    try:
        return _check_ser_guess(current_tries, max_guess)

    except ValueError:
        print("Sorry! That's an invalid number. Please try again.")
        current_tries -= 1
        print(f"You have {current_tries} tries left.")
        return (current_tries, current_tries > 0 and have_not_guessed)


def start_next_level(level_introduction, max_guess):
    print(level_introduction)

    tries = 3
    have_not_guessed_and_have_tries_left = True

    while have_not_guessed_and_have_tries_left:
        tries, have_not_guessed_and_have_tries_left = _ask_for_next_guess(
            tries, max_guess
        )

    if not tries:
        print("Sorry! You're out of tries. Restart the program to play again!.")
        exit()


def main():
    ask_if_player_wants_to_play()
    start_next_level(
        "Hello! Welcome to Bee's Number Guessing Game!\nIn this game, you'll have "
        "to try to guess the number I'm thinking of.\nYou have three tries to "
        "guess correctly, in three different levels of difficulty.\nAre you ready "
        "to play?",
        5,
    )
    start_next_level(
        "For level 2, I'm thinking of a number between 1-10 (no decimals).\nCan "
        "you guess it? Please enter your guess down below.",
        10,
    )
    start_next_level(
        "For level 3, the FINAL level...I'm thinking of a number between 1-20 (no "
        "decimals).\nCan you guess it? Please enter your guess down below.",
        20,
    )
    print("YO WIN!!!! LES GOOOOOOOOOO")


if __name__ == "__main__":
    main()

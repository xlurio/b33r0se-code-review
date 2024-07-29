"""
Reduced code duplication with a single reusable function to increase maintainability and
follow the DRY principle
"""

import random


def ask_if_player_wants_to_play():
    print(
        "Hello! Welcome to Bee's Number Guessing Game!\nIn this game, you'll have "
        "to try to guess the number I'm thinking of.\nYou have three tries to "
        "guess correctly, in three different levels of difficulty.\nAre you ready "
        "to play?"
    )
    user_yes_no = input("Please type 'YES' or 'NO' to continue: ")
    if user_yes_no.upper() == "YES":
        print("Great! Let's get started!")
    elif user_yes_no.upper() == "NO":
        print("Aw, that's too bad. ): Maybe next time!")
        exit()
    else:
        print("Oops! You put an invalid option. Please try again.")
        exit()


def render_level(level_introduction, max_guess):
    print(level_introduction)

    tries = 3
    have_not_guessed = True
    have_not_guessed_and_have_tries_left = tries > 0 and have_not_guessed

    while have_not_guessed_and_have_tries_left:
        try:
            user_guess_2 = int(input("Guess: "))
        except ValueError:
            print("Sorry! That's an invalid number. Please try again.")
            tries -= 1
            print(f"You have {tries} tries left.")
        else:
            comp_guess_2 = random.randint(1, max_guess)
            if user_guess_2 == comp_guess_2:
                print("Correct! Onto the next level.")
                have_not_guessed = False
            elif user_guess_2 != comp_guess_2:
                print("Sorry! That's not correct. Please try again.")
                tries -= 1
                print(f"You have {tries} tries left.")

        have_not_guessed_and_have_tries_left = tries > 0 and have_not_guessed

    if not tries:
        print("Sorry! You're out of tries. Restart the program to play again!.")
        exit()


def main():
    ask_if_player_wants_to_play()
    render_level(
        "Hello! Welcome to Bee's Number Guessing Game!\nIn this game, you'll have "
        "to try to guess the number I'm thinking of.\nYou have three tries to "
        "guess correctly, in three different levels of difficulty.\nAre you ready "
        "to play?",
        5,
    )
    render_level(
        "For level 2, I'm thinking of a number between 1-10 (no decimals).\nCan "
        "you guess it? Please enter your guess down below.",
        10,
    )
    render_level(
        "For level 3, the FINAL level...I'm thinking of a number between 1-20 (no "
        "decimals).\nCan you guess it? Please enter your guess down below.",
        20,
    )
    print("YO WIN!!!! LES GOOOOOOOOOO")


if __name__ == "__main__":
    main()

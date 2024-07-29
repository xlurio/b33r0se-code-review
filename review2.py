"""
1. Functions are supposed to be reusable, which would be impossible if you declare them
    inside another function (look for "scope in programming" to learn more). Hence this
    is considered an antipattern.
2. I introduced a common pattern used in Python. When the module is being used as an
    entry point for the program, Python sets the global variable `__name__` to the value
    "__main__". So we check if `__name__ == "__main__"` to guarantee that we don't run
    the `main` function when this module is imported by another.
3. Exchange the string concatenations by f-strings to increase readability
"""

import random


def lvl_1():
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
    print(
        "For the first level, I'm thinking of a number between 1-5 (no decimals)."
        "\nCan you guess it? Please enter your guess down below."
    )

    tries = 3
    have_not_guessed = True
    have_not_guessed_and_have_tries_left = tries > 0 and have_not_guessed

    while have_not_guessed_and_have_tries_left:
        try:
            user_guess_1 = int(input("Guess: "))
        except ValueError:
            print("Sorry! That's an invalid number. Please try again.")
            tries -= 1
            print(f"You have {tries} tries left.")
        else:
            comp_guess_1 = random.randint(1, 10)
            if user_guess_1 == comp_guess_1:
                print("Correct! Onto the next level.")
                have_not_guessed = False
            elif user_guess_1 != comp_guess_1:
                print("Sorry! That's not correct. Please try again.")
                tries -= 1
                print(f"You have {tries} tries left.")

        have_not_guessed_and_have_tries_left = tries > 0 and have_not_guessed

    if not tries:
        print("Sorry! You're out of tries. Restart the program to play again!.")
        exit()


def lvl_2():
    print(
        "For level 2, I'm thinking of a number between 1-10 (no decimals).\nCan "
        "you guess it? Please enter your guess down below."
    )

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
            comp_guess_2 = random.randint(1, 10)
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


def lvl_3():
    print(
        "For level 3, the FINAL level...I'm thinking of a number between 1-20 (no "
        "decimals).\nCan you guess it? Please enter your guess down below."
    )
    tries = 3
    while tries:
        try:
            user_guess_3 = int(input("Guess: "))
        except ValueError:
            print("Sorry! That's an invalid number. Please try again.")
            tries -= 1
            print(f"You have {tries} tries left.")
        else:
            comp_guess_3 = random.randint(1, 20)
            if user_guess_3 == comp_guess_3:
                print("YO WIN!!!! LES GOOOOOOOOOO")
                exit()
            elif user_guess_3 != comp_guess_3:
                print("Sorry! That's not correct. Please try again.")
                tries -= 1
                print(f"You have {tries} tries left.")
    if not tries:
        print("Sorry! You're out of tries. Restart the program to play again!.")
        exit()


def main():
    lvl_1()
    lvl_2()
    lvl_3()


if __name__ == "__main__":
    main()

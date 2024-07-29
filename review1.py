"""
1. `lvl_3` wasnt't doing nothing but declaring a function there were never called
2. The levels 1 and 2 were repeating forever while you were guessing correctly
3. You would never guess the number. The `input` function returns a `str` (string).
    `randint` function returns an `int` (integer). Since `str`s and `int` will never be
    equal, the program would always say your guess is incorrect.
4. Level 3 was supposed to be a guess between 1-20 but it was 1-10
"""

import random


def num_guessing_game():
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
                user_guess_1 = int(
                    input("Guess: ")
                )  # Parse the input value to int before
                # comparing to the computer guess.
            except ValueError:
                print("Sorry! That's an invalid number. Please try again.")
                tries -= 1
                print("You have " + str(tries) + " tries left.")
            else:
                comp_guess_1 = random.randint(1, 10)
                if user_guess_1 == comp_guess_1:
                    print("Correct! Onto the next level.")
                    have_not_guessed = False  # Stop the loop if the guess was correct
                elif user_guess_1 != comp_guess_1:
                    print("Sorry! That's not correct. Please try again.")
                    tries -= 1
                    print("You have " + str(tries) + " tries left.")

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
                user_guess_2 = int(
                    input("Guess: ")
                )  # Parse the input value to int before
                # comparing to the computer guess.
            except ValueError:
                print("Sorry! That's an invalid number. Please try again.")
                tries -= 1
                print("You have " + str(tries) + " tries left.")
            else:
                comp_guess_2 = random.randint(1, 10)
                if user_guess_2 == comp_guess_2:
                    print("Correct! Onto the next level.")
                    have_not_guessed = False  # Stop the loop if the guess was correct
                elif user_guess_2 != comp_guess_2:
                    print("Sorry! That's not correct. Please try again.")
                    tries -= 1
                    print("You have " + str(tries) + " tries left.")

            have_not_guessed_and_have_tries_left = tries > 0 and have_not_guessed

        if not tries:
            print("Sorry! You're out of tries. Restart the program to play again!.")
            exit()

    def lvl_3():
        # `lvl_3` wasnt't doing nothing but declaring a function there were never called
        print(
            "For level 3, the FINAL level...I'm thinking of a number between 1-20 (no "
            "decimals).\nCan you guess it? Please enter your guess down below."
        )
        tries = 3
        while tries:
            try:
                user_guess_3 = int(
                    input("Guess: ")
                )  # Parse the input value to int before
                # comparing to the computer guess.
            except ValueError:
                print("Sorry! That's an invalid number. Please try again.")
                tries -= 1
                print("You have " + str(tries) + " tries left.")
            else:
                comp_guess_3 = random.randint(
                    1, 20
                )  # This level was supposed to be a guess
                # between 1-20, but it 1-10
                if user_guess_3 == comp_guess_3:
                    print("YO WIN!!!! LES GOOOOOOOOOO")
                    exit()
                elif user_guess_3 != comp_guess_3:
                    print("Sorry! That's not correct. Please try again.")
                    tries -= 1
                    print("You have " + str(tries) + " tries left.")
        if not tries:
            print("Sorry! You're out of tries. Restart the program to play again!.")
            exit()

    lvl_1()
    lvl_2()
    lvl_3()


num_guessing_game()

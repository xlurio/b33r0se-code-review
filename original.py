"""
Original program
"""
import random


def num_guessing_game():
    def lvl_1():
        print(
            "Hello! Welcome to Bee's Number Guessing Game!\nIn this game, you'll have to try to guess the number I'm thinking of.\nYou have three tries to guess correctly, in three different levels of difficulty.\nAre you ready to play?"
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
        tries = 3
        print(
            "For the first level, I'm thinking of a number between 1-5 (no decimals).\nCan you guess it? Please enter your guess down below."
        )
        while tries:
            user_guess_1 = input("Guess: ")
            comp_guess_1 = random.randint(1, 5)
            if user_guess_1 == comp_guess_1:
                print("Correct! Onto the next level.")
            elif user_guess_1 != comp_guess_1:
                try:
                    user_guess_1 = int(user_guess_1)
                    print("Sorry! That's not correct. Please try again.")
                    tries -= 1
                    print("You have " + str(tries) + " tries left.")
                except ValueError:
                    print("Sorry! That's an invalid number. Please try again.")
                    tries -= 1
                    print("You have " + str(tries) + " tries left.")
        if not tries:
            print("Sorry! You're out of tries. Restart the program to play again!.")
            exit()

    def lvl_2():
        print(
            "For level 2, I'm thinking of a number between 1-10 (no decimals).\nCan you guess it? Please enter your guess down below."
        )
        tries = 3
        while tries:
            user_guess_2 = input("Guess: ")
            comp_guess_2 = random.randint(1, 10)
            if user_guess_2 == comp_guess_2:
                print("Correct! Onto the next level.")
            elif user_guess_2 != comp_guess_2:
                try:
                    user_guess_2 = int(user_guess_2)
                    print("Sorry! That's not correct. Please try again.")
                    tries -= 1
                    print("You have " + str(tries) + " tries left.")
                except ValueError:
                    print("Sorry! That's an invalid number. Please try again.")
                    tries -= 1
                    print("You have " + str(tries) + " tries left.")
        if not tries:
            print("Sorry! You're out of tries. Restart the program to play again!.")
            exit()

    def lvl_3():
        def lvl_2():
            print(
                "For level 3, the FINAL level...I'm thinking of a number between 1-20 (no decimals).\nCan you guess it? Please enter your guess down below."
            )
            tries = 3
            while tries:
                user_guess_3 = input("Guess: ")
                comp_guess_3 = random.randint(1, 10)
                if user_guess_3 == comp_guess_3:
                    print("YO WIN!!!! LES GOOOOOOOOOO")
                    exit()
                elif user_guess_3 != comp_guess_3:
                    try:
                        user_guess_3 = int(user_guess_3)
                        print("Sorry! That's not correct. Please try again.")
                        tries -= 1
                        print("You have " + str(tries) + " tries left.")
                    except ValueError:
                        print("Sorry! That's an invalid number. Please try again.")
                        tries -= 1
                        print("You have " + str(tries) + " tries left.")
            if not tries:
                print("Sorry! You're out of tries. Restart the program to play again!.")
                exit()

    lvl_1()
    lvl_2()
    lvl_3()


num_guessing_game()

"""
Using object-oriented programming (OOP) principles to improve the previous revision
"""

import random


class LevelState:

    def __init__(self, curr_num_of_tries=3, have_user_not_guessed=True):
        self.__curr_num_of_tries = curr_num_of_tries
        self.__have_user_not_guessed = have_user_not_guessed

    def get_curr_num_of_tries(self):
        return self.__curr_num_of_tries

    def have_not_guessed_and_have_tries_left(self):
        return self.__have_tries_left() and self.__have_user_not_guessed

    def have_no_tries_left(self):
        return not self.__have_tries_left()

    def __have_tries_left(self):
        return self.__curr_num_of_tries > 0


class Level:

    def __init__(self, level_introduction, max_guess):
        self.__level_introduction = level_introduction
        self.__max_guess = max_guess
        self.__state = LevelState()

    def start(self):
        print(self.__level_introduction)

        while self.__state.have_not_guessed_and_have_tries_left():
            self.__state = self.__ask_for_the_next_guess()

        if self.__state.have_no_tries_left():
            print("Sorry! You're out of tries. Restart the program to play again!.")
            exit()

    def __ask_for_the_next_guess(self):
        try:
            return self.__check_user_guess()

        except ValueError:
            print("Sorry! That's an invalid number. Please try again.")
            current_tries = self.__state.get_curr_num_of_tries() - 1
            print(f"You have {current_tries} tries left.")
            return LevelState(current_tries, have_user_not_guessed=True)

    def __check_user_guess(self):
        did_user_guessed = int(input("Guess: ")) == random.randint(1, self.__max_guess)

        if did_user_guessed:
            print("Correct! Onto the next level.")
            return LevelState(
                self.__state.get_curr_num_of_tries(), not did_user_guessed
            )

        print("Sorry! That's not correct. Please try again.")
        current_tries = self.__state.get_curr_num_of_tries() - 1
        print(f"You have {current_tries} tries left.")
        return LevelState(current_tries, not did_user_guessed)


class Game:
    def __init__(self, levels):
        self.__levels = levels

    def start(self):
        """Starts the game"""
        self.__ask_if_player_wants_to_play()

        for level in self.__levels:
            level.start()

        print("YO WIN!!!! LES GOOOOOOOOOO")

    def __ask_if_player_wants_to_play(self):
        print(
            "Hello! Welcome to Bee's Number Guessing Game!\nIn this game, you'll have "
            "to try to guess the number I'm thinking of.\nYou have three tries to "
            "guess correctly, in three different levels of difficulty.\nAre you ready "
            "to play?"
        )
        return {
            "YES": lambda: print("Great! Let's get started!"),
            "NO": lambda: self.__exit_from_the_game(
                "Aw, that's too bad. ): Maybe next time!"
            ),
        }.get(
            input("Please type 'YES' or 'NO' to continue: "),
            lambda: self.__exit_from_the_game(
                "Oops! You put an invalid option. Please try again."
            ),
        )()

    def __exit_from_the_game(self, message):
        print(message)
        exit()


def main():
    levels = (
        Level(
            "Hello! Welcome to Bee's Number Guessing Game!\nIn this game, you'll have "
            "to try to guess the number I'm thinking of.\nYou have three tries to "
            "guess correctly, in three different levels of difficulty.\nAre you ready "
            "to play?",
            5,
        ),
        Level(
            "For level 2, I'm thinking of a number between 1-10 (no decimals).\nCan "
            "you guess it? Please enter your guess down below.",
            10,
        ),
        Level(
            "For level 3, the FINAL level...I'm thinking of a number between 1-20 (no "
            "decimals).\nCan you guess it? Please enter your guess down below.",
            20,
        ),
    )
    Game(levels).start()
    print("YO WIN!!!! LES GOOOOOOOOOO")


if __name__ == "__main__":
    main()

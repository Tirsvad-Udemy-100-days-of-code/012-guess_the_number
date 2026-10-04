## @file game.py
#  @brief Game logic for the Number Guessing Game.

import random

from guess_the_number.constants import (
    EASY_ATTEMPTS,
    EASY_CHOICE,
    HARD_ATTEMPTS,
    HARD_CHOICE,
    LOGO,
    MAX_NUMBER,
    MIN_NUMBER,
)


def set_difficulty(level: str) -> int:
    """!
    @brief Convert a difficulty level into a number of attempts.
    @param level Either "easy" or "hard" (case-insensitive).
    @return 10 attempts for easy, 5 for hard.
    @throws ValueError If the level is not recognised.
    """
    level = level.strip().lower()
    if level == EASY_CHOICE:
        return EASY_ATTEMPTS
    if level == HARD_CHOICE:
        return HARD_ATTEMPTS
    raise ValueError(f"Unknown difficulty: {level!r}")


def check_answer(guess: int, answer: int, attempts: int) -> int:
    """!
    @brief Compare a guess with the answer and print feedback.
    @param guess The player's guess.
    @param answer The number to find.
    @param attempts Attempts left before this guess.
    @return Attempts left after this guess (unchanged if the guess is correct).
    """
    if guess > answer:
        print("Too high.")
        return attempts - 1
    if guess < answer:
        print("Too low.")
        return attempts - 1
    print(f"You got it! The answer was {answer}.")
    return attempts


def _ask_difficulty() -> int:
    """!
    @brief Prompt until the player picks a valid difficulty.
    @return The number of attempts for the chosen level.
    """
    while True:
        try:
            return set_difficulty(input(f"Choose a difficulty. Type '{EASY_CHOICE}' or '{HARD_CHOICE}': "))
        except ValueError:
            print("Please type 'easy' or 'hard'.")


def _ask_guess() -> int:
    """!
    @brief Prompt until the player enters a whole number in range.
    @return The guess.
    """
    while True:
        raw = input("Make a guess: ").strip()
        if raw.lstrip("-").isdigit() and MIN_NUMBER <= int(raw) <= MAX_NUMBER:
            return int(raw)
        print(f"Enter a whole number between {MIN_NUMBER} and {MAX_NUMBER}.")


def play_game() -> None:
    """!
    @brief Run one full game in the terminal.
    """
    print(LOGO)
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    answer = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = _ask_difficulty()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = _ask_guess()
        if guess == answer:
            check_answer(guess, answer, attempts)
            return
        attempts = check_answer(guess, answer, attempts)
        if attempts > 0:
            print("Guess again.")

    print(f"You've run out of guesses. The answer was {answer}. You lose.")

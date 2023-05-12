"""
Original code for Project 2.
Source linK:   youtube.com/watch?v=5x6iAKdJB6U
"""

import random

with open('wordlist', 'r') as f:
    words = f.readlines()

word = random.choice(words)[:-1]

allowed_errors = 7
guesses = []
done = False

while not done:  # sets up game board
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"allowed Errors Left {allowed_errors}, Next Guess: ")  # user enters guess
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break

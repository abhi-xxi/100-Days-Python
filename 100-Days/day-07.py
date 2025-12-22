# Hangman Project
import random

# List of words
words = ["python", "hangman", "computer", "programming", "developer"]

# Hangman ASCII stages
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

# Choose random word
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = len(hangman_stages) - 1

print("🎯 Welcome to Hangman!")

while wrong_guesses < max_wrong:
    print(hangman_stages[wrong_guesses])

    # Display word progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word)

    # Check win
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print("❌ Wrong guess!")

# Game over
if wrong_guesses == max_wrong:
    print(hangman_stages[wrong_guesses])
    print("💀 Game Over! The word was:", word)

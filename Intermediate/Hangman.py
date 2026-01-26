import random

hangman = [
    """
     ------
     |    |
     |
     |
     |
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ------
    """
]

words = ["python", "computer", "program", "keyboard", "internet"]

def play_hangman():
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_attempts = len(hangman) - 1

    print("\n🎯 Welcome to Hangman!")

    while wrong_guesses < max_attempts:
        print(hangman[wrong_guesses])

        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        print("Word:", display)

        if "_" not in display:
            print("🎉 You guessed the word:", word)
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠ Already guessed.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("❌ Wrong guess!")
            wrong_guesses += 1
        else:
            print("✅ Correct guess!")

    print(hangman[wrong_guesses])
    print("💀 Game Over! The word was:", word)


while True:
    play_hangman()
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing 👋")
        break

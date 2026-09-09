import random
import nltk
from nltk.corpus import words

# Download word database silently
nltk.download("words", quiet=True)

# Get a random word
word_list = words.words()
random_word = random.choice(word_list).lower()


# Visual stages
HANGMANPICS = [
r"""
   +-------+
   |       |
   |       |
   |       |
   |       |
===========
  Lives: 6
""",

r"""
   +-------+
   |   ⚠   |
   |       |
   |       |
   |       |
===========
  Lives: 5
""",

r"""
   +-------+
   |   ⚠   |
   |  ⚠ ⚠  |
   |       |
   |       |
===========
  Lives: 4
""",

r"""
   +-------+
   |   ⚠   |
   |  ⚠ ⚠  |
   |   ⚠   |
   |       |
===========
  Lives: 3
""",

r"""
   +-------+
   | ⚠ ⚠ ⚠ |
   |  ⚠ ⚠  |
   |   ⚠   |
   |       |
===========
  Lives: 2
""",

r"""
   +-------+
   | ⚠ ⚠ ⚠ |
   |  ⚠ ⚠  |
   | ⚠ ⚠ ⚠ |
   |   ⚠   |
===========
  Lives: 1
""",

r"""
   +-------+
   | XXXXX |
   | GAME  |
   | OVER  |
   | XXXXX |
===========
  Lives: 0
"""
]


# Game header
print(r"""
==================================================
                  🎯 HANGMAN GAME
==================================================

Welcome to Hangman!

A secret word has been chosen.
Your mission is to reveal it one letter at a time.

Be careful...

You have only 6 lives. ❤️ ❤️ ❤️ ❤️ ❤️ ❤️

Every wrong guess costs you one life.

Can you discover the word before your lives run out?

Good luck! 🍀

==================================================
""")


# Hidden word
display = ["_"] * len(random_word)

# Player lives
lives = 6


# Main game loop
while "_" in display and lives > 0:

    print("\n" + "─" * 50)

    # Shows the current visual stage
    print(HANGMANPICS[6 - lives])

    print("WORD:")
    print(" ".join(display))

    print(f"\n❤️ Lives remaining: {lives}")

    print("─" * 50)

    user_guess = input("\n🔤 Guess a letter: ").lower()


    # Correct guess
    if user_guess in random_word:

        for position, letter in enumerate(random_word):

            if letter == user_guess:
                display[position] = user_guess

        print(f"\n✅ Correct! The letter '{user_guess}' is in the word!")


    # Wrong guess
    else:

        lives -= 1

        print(f"\n❌ Wrong guess! There is no '{user_guess}' in the word.")
        print(f"❤️ Lives remaining: {lives}")


# Final screen
print("\n" + "=" * 50)

# Shows the final visual stage
print(HANGMANPICS[6 - lives])

print("Final word:")
print(" ".join(display))


# Win or lose
if lives == 0:

    print("\n❌ GAME OVER!")
    print(f"The secret word was: {random_word}")

else:

    print("\n🏆 YOU WIN!")
    print(f"You discovered the word: {random_word}")


print("\nThanks for playing Hangman! 👋")
print("=" * 50)
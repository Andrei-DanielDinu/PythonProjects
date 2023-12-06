import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "pineapple", "watermelon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word

def hangman():
    attempts = 6
    guessed_letters = []
    word = choose_word()
    word_guessed = False

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0 and not word_guessed:
        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in word:
                print("Good guess!")
                guessed_letters.append(guess)
                displayed = display_word(word, guessed_letters)
                print(displayed)
                if "_ " not in displayed:
                    word_guessed = True
            else:
                print("Wrong guess!")
                attempts -= 1
                print(f"Attempts left: {attempts}")
        else:
            print("Invalid input. Please enter a single letter.")

    if word_guessed:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Sorry, you're out of attempts. The word was '{word}'.")

hangman()

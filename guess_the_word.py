# Joe Collier
# CIS256 Fall 2025
# EX 4

import random

# Dictionary to store words
word_dictionary = {"engine":"6 letters",
                    "brakes":"6 letters",
                    "axle":"4 letters",
                    "tires":"5 letters",
                    "seat":"4 letters",
                    "pedal":"5 letters"
                    }

def choose_word(word_dictionary):
    return random.choice(list(word_dictionary.items()))

def guess_process(word, guess, word_display, attempts, guessed_letters):

    # Add the letter geussed to the guessed_letters set list
    guessed_letters.add(guess)

    # Check for correct guess
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                word_display[i] = guess
    else:
        attempts -= 1 # Remove 1 from attempts
    return word_display, attempts, guessed_letters

def word_guesser():
    word, hint = choose_word(word_dictionary) # Word picker
    word_display = ["_" if letter.isalpha() else letter for letter in word] # Displays each letter if picked
    attempts = 6 # Variable to set number of attempts
    guessed_letters = set() # Set the letters guessed

    print("\nWelcome to the word guessing game.")
    print("The words are parts of cars.\n")
    print(f"Hint: The word selected has {hint}.")
    print(f"You have {attempts} attempts.\n")
    
    # Game loop
    while attempts > 0 and "_" in word_display:
        print("Word:", " ".join(word_display)) # Displays the correctly guessed letters in which order they appear in the word
        print("Guessed letters:", " ".join(sorted(guessed_letters))) # Displays the guessed letteres in alphabetical order
        guess = input("\nGuess a letter:")

        # Check for incorrect input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        # Check for guessed letters
        if guess in guessed_letters:
            print("That letter has already been guessed.\n")
            continue
        
        word_display, attempts, guessed_letters = guess_process(word, guess, word_display, attempts, guessed_letters)
 
        if guess in word:
            print("The letter you guessed is correct.")
        else:
            print(f"The letter you guessed is not correct. You have {attempts} attempts left.\n")

    # End game
    if "_" not in word_display:
        print(f"\nYou guessed the word correctly. The word was '{word}'.\n")
    else:
        print(f"You are out of attempts. The word was '{word}'.\n")

# Run Game
if __name__ == "__main__":
    word_guesser()
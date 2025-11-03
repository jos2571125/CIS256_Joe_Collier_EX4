# Joe Collier
# CIS 256 Fall 2025
# EX 4 Test

from guess_the_word import choose_word, word_dictionary

# Function to test if the random word generator is pulling from the word_dictionary
def test_choose_word_dictionary():

    word, hint = choose_word(word_dictionary)

    assert word in word_dictionary, f"{word} was not found in the dictionary"
    assert hint == word_dictionary[word], f"Hint for {word} does not match expected value"

from guess_the_word import guess_process

# Function to test correct guess
def test_correct_guess_updates_display():
    word = "tires"
    guess = "i"
    word_display = ["_", "_", "_", "_", "_"]
    attempts = 6
    guessed_letters = set()

    new_display, new_attempts, new_guessed = guess_process(word, guess, word_display, attempts, guessed_letters)

    assert new_display == ["_", "i", "_", "_", "_"]  
    assert new_attempts == 6
    assert guess in new_guessed

# Function to test incorrect guesss
def test_incorrect_guess_decrements_attempts():
    word = "seat"
    guess = "x"
    word_display = ["_", "_", "_", "_"]
    attempts = 6
    guessed_letters = set()

    new_display, new_attempts, new_guessed = guess_process(word, guess, word_display, attempts, guessed_letters)

    assert new_display == ["_", "_", "_", "_"]
    assert new_attempts == 5
    assert guess in new_guessed


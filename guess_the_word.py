# Joe Collier
# CIS256 Fall 2025
# EX 4

import random

# Function to create the dictionary and 
def word_guesser():
    word_dictionary = {"engine":"6 letters",
                       "brakes":"6 letters",
                       "axle":"4 letters",
                       "tires":"5 letters",
                       "seat":"4 letters",
                       "pedal":"5 letters"
                       }

    character, hint = random.choice(list(word_dictionary.items())) # Word picker
    word_display = ["_" if letter.isalpha() else letter for letter in character] # Displays each letter if picked
    attempts = 6 # Variable to set number of attempts
    guessed_letters = set() # Set the letters guessed
from hangman_words import word_list
import random
from hangman_art import stages, logo

chosen_word = random.choice(word_list).lower()

def blank_space(word):
    word_to_guess = ""
    for letter in word:
        word_to_guess += "_"
    return word_to_guess

def guessing(blank, word):
    attempts = 6
    guessed_letters = []
    word_to_guess = ""
    game = True
    print(stages[6])
    while game:
        word_to_guess = ""
        print(f"You have {attempts} attempts left")
        print(f"word to guess : {blank}")
        user_guess = input("Guess a word: ")

        if user_guess in word:
            for letter in word:
                if user_guess == letter:
                    word_to_guess += user_guess
                    guessed_letters.append(user_guess)
                elif letter in guessed_letters:
                    word_to_guess += letter
                else:
                    word_to_guess += "_"
        else:
            attempts -= 1
        if attempts == 0:
            return f"You lose the word was {chosen_word}"
        print(stages[attempts])

        print(word_to_guess)
        if word_to_guess == word:
            game = False
    return "Congratulations!"
blanks = blank_space(chosen_word)
print(chosen_word)
print(logo)
print(guessing(blanks, chosen_word))
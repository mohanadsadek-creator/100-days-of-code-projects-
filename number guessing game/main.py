import art
import random

def guessing_game(guess, number):
    if guess == number:
        return True
    elif guess > number:
        print("Too high")
        return False
    elif guess < number:
        print("Too low")
        return False

def guessing(number, mode):
    if mode == "easy":
        attempts = 10
    elif mode == "hard":
        attempts = 5
    else:
        print("Please choose either 'easy' or 'hard'")
    print(f"You have {attempts} attempts left")
    user_guess = int(input("Guess the number"))
    while not guessing_game(user_guess, number):
        if attempts == 0:
            print("Game over")
            return
        attempts -= 1
        user_guess = int(input("Guess the number"))
        print(f"you have {attempts} attempts left")
    print("Congratulations, you guessed the number")


def number_game():
    print(art.logo)
    print("Welcome to Number Guessing Game\nI am thinking of a number between 1 and 100")
    number_to_guess = random.randint(1,100)
    difficulty = input("choose a difficulty type 'easy' or 'hard': ")
    guessing(number_to_guess, difficulty)
Game = True
while Game:
    number_game()
    play_again = input("would you like to play again  type 'y' or 'n'")
    if play_again == "n":
        Game = False
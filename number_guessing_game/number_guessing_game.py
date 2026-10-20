import random
print("Welcome to the Number Guessing Game\n")
print("I am thinking of a number between 1 and 100\n")
difficulty = input("Choose to play on easy or hard mode").lower()
numbers_list = []
for number in range(100):
    numbers_list.append(number)
def easy_mode():
    number_to_guess = random.choice(numbers_list)
    attempts = 10
    user_guess = 0
    game_over = False
    while not game_over:
        print(f"You have {attempts} attempts remaining\n")
        user_guess = int(input("Make a guess : "))
        if user_guess == number_to_guess:
            print(f"You won\nThe number was:{number_to_guess}\n")
            return
        elif user_guess > number_to_guess:
            print("Too high")
            attempts -= 1
        elif user_guess < number_to_guess:
            print("Too low")
            attempts -= 1
        if attempts == 0:
            print("You ran out of attempts")
            game_over = True
def hard_mode():
    number_to_guess = random.choice(numbers_list)
    attempts = 5
    user_guess = 0
    game_over = False
    while not game_over:
        print(f"You have {attempts} attempts remaining\n")
        user_guess = int(input("Make a guess : "))
        if user_guess == number_to_guess:
            print(f"You won\nThe number was:{number_to_guess}\n")
            return
        elif user_guess > number_to_guess:
            print("Too high")
            attempts -= 1
        elif user_guess < number_to_guess:
            print("Too low")
            attempts -= 1
        if attempts == 0:
            print("You ran out of attempts")
            game_over = True




if difficulty == "easy":
    easy_mode()

elif difficulty == "hard":
    hard_mode()
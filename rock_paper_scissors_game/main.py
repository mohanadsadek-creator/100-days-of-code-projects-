import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def rps():
    game = [rock, paper, scissors]
    user_turn = int(input("Press 0 for rock 1 for paper or press 2 for scissors: "))
    computer_turn = random.randint(0,2)
    user_choice = game[user_turn]
    computer_choice = game[computer_turn]
    print(f"user choice : {user_choice}")
    print(f"computer choice : {computer_choice}")
    if user_choice == computer_choice:
        print("its a tie")
    if user_turn > computer_turn:
        if computer_turn == 0:
            print("you lose")
        else:
            print("you win")
    if computer_turn > user_turn:
        if user_turn == 0:
            print("you win")
        else:
            print("you lose")

print("Play Rock Paper Scissors")
play_again = True
while play_again:
    rps()
    want_to_play = input("Do you want to play again y or n")
    if want_to_play == "n":
        play_again = False
    elif want_to_play == "y":
        print("\n" * 20)

import art
import game_data
import random
print(art.logo)
# assign two variables to choose which accounts to compare
first_account = random.choice(game_data.data)
#Initialize current score
current_score = 0
def second_account(first):
    another_account = random.choice(game_data.data)
    while another_account == first:
        another_account = random.choice(game_data.data)
    return another_account
def compare_followers(first, second):
    #create variable for follower count
    first_account_followers = int(first["follower_count"])
    second_account_followers = int(second["follower_count"])
    # create an empty variable for the highest followed user
    highest_followed_account = max(first_account_followers, second_account_followers)
    return highest_followed_account
def game(first, second):
    while first == second:
        second = second_account(first)
    print("Compare A :" + first["name"] + ", " + first["description"] + ", " + first["country"])
    print(art.vs)
    print("Against B :" + second["name"] + ",  " + second["description"] + ", " + second["country"])
    #Make the user choose between first and second
    user_choice = input("Guess who has the highest followed account 'A' or 'B' ")
    #Make a variable for the account selected and assign it to the first choice
    selected_account = first
    #if user selects the second choice assign selected account to second account
    if user_choice == "B":
        selected_account = second
    #if user selected the same account as the highest follower account he is correct add to the score and print it
    #play the game again
    if int(selected_account["follower_count"]) == compare_followers(first, second):
        global current_score
        current_score += 1
        print(f"You are correct! your current score is {current_score}")
        game(second, second_account(second))
    else:
        print(f"You are incorrect! your final score is {current_score}")
        return
game(first_account, second_account(first_account))
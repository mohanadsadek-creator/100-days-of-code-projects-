import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(card_list):
    card_list_sum = sum(card_list)
    if 11 in card_list:
        if card_list_sum  > 21:
            card_list.remove(11)
            card_list.append(1)
            card_list_sum = sum(card_list)
    if card_list_sum == 21:
        return 0
    elif card_list_sum > 21:
        return 1
    else:
        return card_list_sum

def compare(score1, score2):
    if score1 == score2:
        return "its a tie"
    elif score2 == 21:
        return "computer wins"
    elif score1 == 21:
        return "you win"
    elif score1 > 21:
        return "computer wins"
    elif score2 > 21:
        return "you win"
    elif score1 > score2:
        return "user wins"
    else:
        return "computer wins"

def black_jack():
    user_cards = []
    computer_cards = []
    print(art.logo)
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"{user_cards} \n {[computer_cards[0]]}")
    if user_score == 0:
        print(f"{user_cards} \n {[computer_cards]}")
        print("You win!")
        return
    elif computer_score == 0:
        print(f"{user_cards} \n {[computer_cards]}")
        print("Computer wins!")
        return
    else:
        another_card = input("Would you like to draw another card?'y' or 'n': ")
        while another_card == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            if user_score == 0:
                print(f"{user_cards} \n {[computer_cards]}")
                print("You win!")
                return
            elif user_score == 1:
                print("Computer wins!")
                print(f"{user_cards} \n {[computer_cards]}")
                return
            else:
                print(f"{user_cards} \n {[computer_cards[0]]}")
                another_card = input("Would you like to draw another card?")
        computer_score = calculate_score(computer_cards)
        while sum(computer_cards) < 17:
            print(f"{user_cards} \n {[computer_cards]}")
            computer_cards.append(deal_card())
        print(compare(user_score, computer_score))
        return

Game = True
while Game:
    black_jack()
    play_again = input("Do you want to play again?'y' or 'n': ")
    if play_again == "y":
        print("\n" * 20)
    else:
        Game = False

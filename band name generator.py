import random
def band_name_generator(items_list):
    first_name = random.choice(items_list)
    second_name = random.choice(items_list)
    while first_name == second_name:
        second_name = random.choice(items_list)
    print(first_name + second_name)
    try_again = input("would you like another name? enter yes or no\n").lower()
    if try_again == "yes":
        band_name_generator(items_list)


print("Welcome to the band name generator")
user_city = input("What is the city you grew up in?\n")
user_pet = input("What is your pet name?\n")
user_favourite_food = input("What is your favourite food?\n")
user_favourite_car = input("What is your favourite car?\n")
user_favourite_movie = input("What is your favourite movie?\n")
items = [user_city, user_pet, user_favourite_food, user_favourite_car, user_favourite_movie]
band_name_generator(items)
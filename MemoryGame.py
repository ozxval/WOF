
from random import randint
from time import sleep
import os


def check_input(num):
    try:
        num = int(num)
        if 0 < num < 101:
            return True
        else:
            return False
    except:
        return False


def generate_sequence(difficulty_level):
    random_list = []
    for i in range(difficulty_level):
        random_list.insert(i, randint(1, 101))
    return random_list


def get_list_from_user(difficulty_level):
    print("Enter the number in the right order:\n")
    user_list = []
    for i in range(difficulty_level):
        temp = input(f"enter the number in place {(i + 1)}: \n")
        checker = check_input(temp)
        while not checker:
            print("You enter wrong number or an character")
            temp = input(f"enter the number in place {(i + 1)}")
            checker = check_input(temp)
        user_list.insert(i, int(temp))
    return user_list


def is_list_equal(player_list, game_list):
    for i in range(len(player_list)):
        if player_list[i] != game_list[i]:
            return False
    return True


def play(difficulty_level):
    print("Remember this number in the right order!")
    sleep(2)
    game_list = generate_sequence(difficulty_level)
    print(game_list)
    sleep(0.7)
    print("\n" * 50)
    print("Lets see if remember it all!")
    plyer_list = get_list_from_user(difficulty_level)
    return is_list_equal(plyer_list, game_list)



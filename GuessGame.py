from random import randint


def generate_number(difficulty_level):
    return randint(1, difficulty_level)


def get_guess_from_user(difficulty_level):
    flag = False
    while not flag:
        number = input("Please enter number between 1 - %s: " % difficulty_level)
        try:
            number = int(number)
            if 0 < number < (difficulty_level + 1):
                return number
            else:
                print("Wrong input!")
        except:
            print("Wrong input!")


def compare_results(random_number, player_guess):
    if random_number is player_guess:
        return True
    else:
        return False


def play(difficulty):
    return compare_results(generate_number(difficulty), get_guess_from_user(difficulty))


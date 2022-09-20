import CurrencyRouletteGame
import GuessGame
import MemoryGame
import Score
import Utils

games_amount = 3
max_difficulty = 5


def number_check(num, max_number):
    try:
        num = int(num)
        if 0 < num < (max_number + 1):
            return True
        else:
            return False
    except:
        return False


def welcome(name):
    return "Hello %s and welcome to the World of Games (WoG). \nHere you can find many cool games to play." % name


def load_game():
    print("Please choose a game to play: \n"
          "\t 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back"
          "\n\t 2. Guess Game - guess a number and see if you chose like the computer"
          "\n\t 3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    chosen_game = input(f"Please choose game! enter number between 1-{games_amount} - ")
    input_check = number_check(chosen_game, games_amount)
    while not input_check:
        chosen_game = input(f"You need to enter A  CORRECT NUMBER!  Please enter number between 1-{games_amount} - ")
        input_check = number_check(chosen_game, games_amount)
    difficulty = input(f"Great! Please choose the game difficulty. Enter number between 1 - {max_difficulty} :  ")
    input_check = number_check(difficulty, max_difficulty)
    while not input_check:
        difficulty = input(f"You need to enter A  CORRECT NUMBER!  Please enter number between 1-{max_difficulty} - ")
        input_check = number_check(difficulty, max_difficulty)
    chosen_game = int(chosen_game)
    difficulty = int(difficulty)
    play = True   # while "play" is true, the game will repeat
    while play:
        result = start_game(chosen_game, difficulty)
        if result:
            Score.add_score(difficulty)
            print(f"You WIN! Your total score is: {Score.show_score()}")
        else:
            print(f"You Lose... Your total score is: {Score.show_score()}")
        play = play_again()


def start_game(chosen_game, difficulty):
    if chosen_game == 1:
        return MemoryGame.play(difficulty)
    elif chosen_game == 2:
        return GuessGame.play(difficulty)
    elif chosen_game == 3:
        return CurrencyRouletteGame.play(difficulty)


def play_again():
    print("\n\n\n")
    to_play_again = input("Do you want to play this game again? Yes/No: ")
    input_check = yes_or_no(to_play_again)
    while not input_check:
        to_play_again = input("You enter wrong answer! Do you want to play this game again (same difficulty)? Yes/No: ")
        input_check = yes_or_no(to_play_again)
    if to_play_again.upper() == "YES":
        Utils.Screen_cleaner()
        return True
    else:
        to_play_again = input("Do you want to play different game? Yes/No: ")
        input_check = yes_or_no(to_play_again)
        while not input_check:
            to_play_again = input("You enter wrong answer! Do you want to play different game? Yes/No: ")
            input_check = yes_or_no(to_play_again)
        if to_play_again.upper() == "YES":
            load_game()
        else:
            print("GoodBye!")
            return False


def yes_or_no(string):
    string = string.upper()
    if string == "YES" or string == "NO":
        return True
    else:
        return False

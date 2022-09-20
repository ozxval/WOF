import requests
from datetime import date
from random import randint


def get_ils_currency():
    base_currency = 'USD'
    out_currency = 'ILS'
    time = date.today()
    url = "https://api.exchangerate.host/timeseries?base={0}&start_date={1}&end_date={2}&symbols={3}".format(base_currency, time, time, out_currency)
    res = requests.get(url)
    data = res.json()
    res.close()
    rate = data['rates']
    str_time = str(time)
    ils_currency = rate[str_time]
    return float(ils_currency[out_currency])


def get_money_interval(difficulty_level, amount):
    amount *= get_ils_currency()
    print(amount)
    return (amount - (5 - difficulty_level)), (amount + (5 - difficulty_level))


def get_guess_from_user():
    flag = False
    while not flag:
        player_guess = input("Please enter your guess: ")
        try:
            player_guess = float(player_guess)
            return player_guess
        except:
            print("You need to enter a NUMBER!")


def play(difficulty_level):
    print("Please try to guess what the value of this amunt of US Dollar in IL Shekels:")
    random_number = randint(1, 100)
    print(random_number)
    player_guess = get_guess_from_user()
    min_range, max_range = get_money_interval(difficulty_level, random_number)
    if min_range <= player_guess <= max_range:
        return True
    else:
        return False



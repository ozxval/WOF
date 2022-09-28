import Utils
import webbrowser
import os
import requests


def add_score(difficulty):
    score_file = open(Utils.SCORES_FILE_NAME, "r")
    file_data = score_file.read()
    if file_data == "":
        file_data = "0"
    score = int(file_data)
    score_file.close()
    points_of_winning = difficulty * 3 + 5
    score += points_of_winning
    score_file = open(Utils.SCORES_FILE_NAME, "w")
    score_file.write(str(score))
    score_file.close()


def restart_score():
    score_file = open(Utils.SCORES_FILE_NAME, "w")
    score_file.write("0")
    score_file.close()


def show_score():
    score_file = open(Utils.SCORES_FILE_NAME, "r")
    score = str(score_file.read())
    score_file.close()
    return score



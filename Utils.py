import os

SCORES_FILE_NAME = "Scores.txt"  # This represents the file that contain the user total score
BAD_RETURN_CODE = -99


def Screen_cleaner():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

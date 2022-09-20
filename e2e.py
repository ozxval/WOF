from selenium.webdriver import common
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.chrome.webdriver import ChromiumDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import MainScores
import sys


def test_scores_service():
    MainScores.score_server()
    url = 'http://127.0.0.1:5001/'
    my_driver = webdriver.chrome(executable_path=r"D:\chromedriver_win32\chromedriver.exe")
    my_driver.get(url)
    my_score = int(my_driver.find_element_by_id("score").text)
    webdriver.ChromiumDriver.close(my_driver)
    my_driver.close()
    if 0 > my_score > 1001:
        return True
    else:
        return False


def main_function():
    test_scores_service()
    if test_scores_service():
        return sys.exit(0)
    else:
        return sys.exit(-1)





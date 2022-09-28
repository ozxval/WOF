from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Utils


def test_scores_service(url):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 20)
    driver.get(url)
    get_score = int(wait.until(EC.visibility_of_element_located((By.ID, "score"))).text)
    driver.close()
    if 0 < get_score < 1001:
        return True
    else:
        return False


def main_function():
    if test_scores_service(Utils.server_address):
        return exit(0)
    else:
        return exit(-1)


main_function()

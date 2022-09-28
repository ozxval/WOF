from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_score():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 20)
    driver.get("http://127.0.0.1:5001")
    get_score = int(wait.until(EC.visibility_of_element_located((By.ID, "score"))).text)
    # get_score = int(driver.find_element(By.ID, "score").text)
    #assert (get_score >= 1) and (get_score <= 1000) is True
    driver.close()
    if 0 < get_score < 1001:
        return True
    else:
        return False


print(test_check_score())

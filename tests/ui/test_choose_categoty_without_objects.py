import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


@pytest.mark.amazonui
def test_check_search_on_page():
    driver = webdriver.Chrome(
        service=Service(r"c:/Users/PavelQA/qa_auto_course/" + "chromedriver.exe")
    )

    driver.get("https://www.amazon.com/")

    search_elem = driver.find_element(By.ID, "desktop-grid-1").find_element(
        By.LINK_TEXT, "Keyboards"
    )

    search_elem.click()
    assert driver.title == "Amazon.com : gaming keyboard"
    time.sleep(3)

    driver.close()

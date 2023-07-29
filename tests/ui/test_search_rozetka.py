import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui
def test_check_search_on_page():
    driver = webdriver.Chrome(
        service=Service(r"c:/Users/PavelQA/qa_auto_course/" + "chromedriver.exe")
    )

    driver.get("https://rozetka.com.ua/")

    search_elem = driver.find_element(By.NAME, "search")

    search_elem.send_keys("ноутбуки")

    btn_elem = driver.find_element(By.CLASS_NAME, "search-form__submit")

    btn_elem.click()
    assert (
        driver.title
        == "Ноутбуки - ROZETKA | Купити ноутбук в Києві: ціна, відгуки, продаж, вибір ноутбуків в Україні"
    )
    time.sleep(3)

    driver.close()

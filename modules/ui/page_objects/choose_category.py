from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class ChooseCategoryAmazon(BasePage):
    URL = "https://www.amazon.com/"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(ChooseCategoryAmazon.URL)

    def click_on_category_card(self, id):
        category_card = self.driver.find_element(By.ID, id)
        category_card.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title

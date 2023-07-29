from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchCategoryRozetka(BasePage):
    URL = "https://rozetka.com.ua/"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(SearchCategoryRozetka.URL)

    def enter_in_search_field(self, text_value):
        search_elem = self.driver.find_element(By.NAME, "search")

        search_elem.send_keys(text_value)

        btn_search = self.driver.find_element(By.CLASS_NAME, "search-form__submit")

        btn_search.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title


class SearchCategoryAmazon(BasePage):
    URL = "https://www.amazon.com/"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(SearchCategoryAmazon.URL)

    def enter_text_in_search_field(self, text_value):
        search_field_elem = self.driver.find_element(By.ID, "twotabsearchtextbox")

        search_field_elem.send_keys(text_value)

        btn_search = self.driver.find_element(By.ID, "nav-search-submit-button")

        btn_search.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title

from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class OpenRegistrationPage(BasePage):
    URL = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%3Fpd_rd_w%3DB7n4T%26content-id%3Damzn1.sym.705c9054-02c9-45b2-811a-9ce311c366a5%3Aamzn1.sym.705c9054-02c9-45b2-811a-9ce311c366a5%26pf_rd_p%3D705c9054-02c9-45b2-811a-9ce311c366a5%26pf_rd_r%3D16CT259XHZV5SF51AE4N%26pd_rd_wg%3DoGzvK%26pd_rd_r%3De800c352-b7d6-42ed-8e87-1d83b29df6cf%26qid%3D1690634818%26ref%3Dsxts_aspa_qna%26c_c%3D-389386241&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(OpenRegistrationPage.URL)

    def click_on_new_account_btn(self):
        btn_elem = self.driver.find_element(By.ID, "createAccountSubmit")

        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title

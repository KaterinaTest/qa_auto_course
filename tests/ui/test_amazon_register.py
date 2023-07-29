from modules.ui.page_objects.amazon_registration import OpenRegistrationPage
import pytest
import time


@pytest.mark.amazonui
def test_check_open_regist_page():
    open_register_page = OpenRegistrationPage()

    open_register_page.go_to()
    open_register_page.click_on_new_account_btn()

    assert open_register_page.check_title("Amazon Registration")

    time.sleep(3)

    open_register_page.close()

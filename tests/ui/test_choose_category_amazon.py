from modules.ui.page_objects.choose_category import ChooseCategoryAmazon
import pytest
import time


@pytest.mark.amazonui
def check_ability_choose_category():
    check_ability_choose_category = ChooseCategoryAmazon()

    check_ability_choose_category.go_to()

    check_ability_choose_category.click_on_category_card(
        "CardInstanceuHqSHaQCVK7YQ9-HLx0uqQ"
    )

    assert check_ability_choose_category.check_title("Aazon.com : gaming keyboard")

    check_ability_choose_category.close()

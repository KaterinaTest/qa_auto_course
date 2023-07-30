from modules.ui.page_objects.choose_category import ChooseCategoryAmazon
import pytest


@pytest.mark.amazonui
def check_ability_choose_category():
    check_ability_choose_category = ChooseCategoryAmazon()

    check_ability_choose_category.go_to()

    check_ability_choose_category.click_on_category_card("desktop-grid-1", "Keyboards")

    assert check_ability_choose_category.check_title("Amazon.com : gaming keyboard")

    check_ability_choose_category.close()

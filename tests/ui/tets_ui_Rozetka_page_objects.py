from modules.ui.page_objects.search_category import SearchCategoryRozetka
import pytest
import time


@pytest.mark.rozetkaui
def test_check_search_category():
    search_category = SearchCategoryRozetka()

    search_category.go_to()

    search_category.enter_in_search_field("ноутбуки")

    assert search_category.check_title(
        "Ноутбуки - ROZETKA | Купити ноутбук в Києві: ціна, відгуки, продаж, вибір ноутбуків в Україні"
    )

    time.sleep(3)

    search_category.close()

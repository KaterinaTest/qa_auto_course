from modules.ui.page_objects.search_category import SearchCategoryAmazon
import pytest


@pytest.mark.amazonui
def test_check_search_on_main_page():
    check_search = SearchCategoryAmazon()

    check_search.go_to()

    check_search.enter_text_in_search_field("pencil")

    assert check_search.check_title("Amazon.com : pencil")

    check_search.close()

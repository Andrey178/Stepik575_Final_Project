import time

import pytest


def test_add_to_basket_button_is_present(browser, link):
    browser.get(link)
    time.sleep(30)
    answer = browser.find_elements_by_xpath("//button[contains(@class, 'btn-add-to-basket')]")
    assert answer, "No 'Add to basket' button"

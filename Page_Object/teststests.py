from labirintPages import SearchHelper
from NegativeAuthPage import NegativeAuthorizationHelper
from AughPage import AuthorizationHelper
from AddbookPage import AddBookHelper
import time
import pytest

def test_main_present(browser):
    labirint_main_2021 = AddBookHelper(browser)
    labirint_main_2021.go_to_site()
    labirint_main_2021.click_on_the_main_2021()
    labirint_main_2021.click_on_the_main_present()
    elements = labirint_main_2021.check_navigation_main_present()
    assert "Топ-10 подарочных изданий в октябре" in elements


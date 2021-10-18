from BaseApp import BasePage
from selenium.webdriver.common.by import By

class LabirintSeacrhLocators:
    LOCATOR_LABIRINT_SEARCH_FIELD = (By.ID, "search-field")
    LOCATOR_LABIRINT_SEARCH_BUTTON = (By.CLASS_NAME, "b-header-b-search-e-btn")
    LOCATOR_LABIRINT_NAVIGATION_BAR = (By.CLASS_NAME, "navisort-item__content")
    LOCATOR_LABIRINT_NAVIGATION_BAR_WRONG_WORLD = (By.CSS_SELECTOR, "#search > div.search-error > h1")


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(LabirintSeacrhLocators.LOCATOR_LABIRINT_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(LabirintSeacrhLocators.LOCATOR_LABIRINT_SEARCH_BUTTON, time=10).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(LabirintSeacrhLocators.LOCATOR_LABIRINT_NAVIGATION_BAR, time=10)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def check_navigation_bar_negative_world(self):
        all_list = self.find_elements(LabirintSeacrhLocators.LOCATOR_LABIRINT_NAVIGATION_BAR_WRONG_WORLD, time=10)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

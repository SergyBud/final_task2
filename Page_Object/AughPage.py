from BaseApp import BasePage
from selenium.webdriver.common.by import By

class LabirintAughhLocators:
    LOCATOR_LABIRINT_BTN_ONE = (By.CSS_SELECTOR, "#minwidth > div.top-header > div.b-header-outer > div.b-header "
                                                 "> div.b-header-b-personal.col-xs-6.col-sm-9.col-md-5.col-md-push-"
                                                 "5.col-lg-push-6.col-lg-4.col-xxl-push-7.col-xxl-3.js-toggle-menu-"
                                                 "block > div > ul > li.b-header-b-personal-e-list-item.have-dropdown."
                                                 "b-header-b-personal-e-list-item_cabinet > a")
    LOCATOR_LABIRINT_CODE = (By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/form[1]/div[3]/input")
    LOCATOR_LABIRINT_BTN_TWO = (By.ID, "g-recap-0-btn")
    LOCATOR_LABIRINT_BTN_THREE = (By.CLASS_NAME, "#minwidth > div.top-header > div > div.b-header > div.b-header-b"
                                                 "-personal.col-xs-6.col-sm-9.col-md-5.col-md-push-5.col-lg-push-6"
                                                 ".col-lg-4.col-xxl-push-7.col-xxl-3.js-toggle-menu-block > div"
                                                 " > ul > li.b-header-b-personal-e-list-item.have-dropdown.b-header"
                                                 "-b-personal-e-list-item_cabinet > a > span.b-header-b-personal"
                                                 "-e-text.b-header-b-personal-e-text-m-overflow > span.js-b-autofade"
                                                 "-text > span")
    LOCATOR_LABIRINT_CONTAIN_WORDS = (By.XPATH, "/html/body/div[1]/div[6]/div[3]/div[1]/div/div[1]/div/span[2]")

class AuthorizationHelper(BasePage):

    def click_on_the_augh_button_one(self):
        return self.find_element(LabirintAughhLocators.LOCATOR_LABIRINT_BTN_ONE, time=15).click()

    def enter_code(self, code):
        code_field = self.find_element(LabirintAughhLocators.LOCATOR_LABIRINT_CODE)
        code_field.click()
        code_field.clear()
        code_field.send_keys(code)
        return code_field

    def click_on_the_augh_button_two(self):
        return self.find_element(LabirintAughhLocators.LOCATOR_LABIRINT_BTN_TWO, time=10).click()

    def click_on_the_augh_button_three(self):
        return self.find_element(LabirintAughhLocators.LOCATOR_LABIRINT_BTN_THREE, time=10).click()

    def check_page_contain_words(self):
        all_list = self.find_elements(LabirintAughhLocators.LOCATOR_LABIRINT_CONTAIN_WORDS, time=10)
        contain_words = [x.text for x in all_list if len(x.text) > 0]
        return contain_words


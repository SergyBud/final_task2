from BaseApp import BasePage
from selenium.webdriver.common.by import By


class LabirintNegativeAughhLocators:
    LOCATOR_LABIRINT_BTN_ONE = (By.XPATH, "/html/body/div[1]/div[5]/div[4]/div[1]/div[1]/div[2]/div/ul/li[4]/a")
    LOCATOR_LABIRINT_CODE = (By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/form[1]/div[3]/input")
    LOCATOR_LABIRINT_BTN_TWO = (By.ID, "g-recap-0-btn")
    LOCATOR_LABIRINT_CONTAIN_NEGATIVE_WORDS = (By.XPATH, "/html/body/div[1]/div[1]/div/div/div/"
                                                         "div/div[1]/form[1]/div[3]/span[3]/small")

class NegativeAuthorizationHelper(BasePage):

    def click_on_the_auth_button_one(self):
        return self.find_element(LabirintNegativeAughhLocators.LOCATOR_LABIRINT_BTN_ONE, time=15).click()

    def enter_negative_code(self, code):
        code_field = self.find_element(LabirintNegativeAughhLocators.LOCATOR_LABIRINT_CODE)
        code_field.click()
        code_field.clear()
        code_field.send_keys(code)
        return code_field

    def click_on_the_auth_button_two(self):
        return self.find_element(LabirintNegativeAughhLocators.LOCATOR_LABIRINT_BTN_TWO, time=10).click()

    def check_page_contain_negative_words(self):
        all_list = self.find_elements(LabirintNegativeAughhLocators.LOCATOR_LABIRINT_CONTAIN_NEGATIVE_WORDS, time=10)
        contain_neg_words = [x.text for x in all_list if len(x.text) > 0]
        return contain_neg_words



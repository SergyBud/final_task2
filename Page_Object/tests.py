from labirintPages import SearchHelper
from NegativeAuthPage import NegativeAuthorizationHelper
from AughPage import AuthorizationHelper
from AddbookPage import AddBookHelper
import time
import pytest

@pytest.mark.parametrize("word", [("Машина"), ("Car"), ("ЛЕРМОНТОВ"), ("2OOFJJVN73638"), ("Лермонто!")])
def test_yandex_search(browser, word):
    labirint_main_page = SearchHelper(browser)
    labirint_main_page.go_to_site()
    labirint_main_page.enter_word(word)
    labirint_main_page.click_on_the_search_button()
    elements = labirint_main_page.check_navigation_bar()
    assert "ТИП ТОВАРА" in elements

@pytest.mark.parametrize("wrongword", [("AAAAAAAAAAAAAAAAAAAAAAA"), ("794949494949")])
def test_yandex_search_wrong_word(browser, wrongword):
    labirint_main_page_two= SearchHelper(browser)
    labirint_main_page_two.go_to_site()
    labirint_main_page_two.enter_word(wrongword)
    labirint_main_page_two.click_on_the_search_button()
    elements = labirint_main_page_two.check_navigation_bar_negative_world()
    assert "Мы ничего не нашли по вашему запросу! Что делать?" in elements

@pytest.mark.parametrize("code", [("A112126343E-43C0-8CC2"), ("A16E-48C0-7d"), ("Sergeyyyyyyy"),
                                 ("2OOFJJVN73638")])
def test_auth_page(browser, code):
    labirint_auth_page = NegativeAuthorizationHelper(browser)
    labirint_auth_page.go_to_site()
    labirint_auth_page.click_on_the_auth_button_one()
    labirint_auth_page.enter_negative_code(code)
    labirint_auth_page.click_on_the_auth_button_two()
    false_message = labirint_auth_page.check_page_contain_negative_words()
    assert false_message
    time.sleep(4)

def test_augh_page(browser):
    labirint_augh_page = AuthorizationHelper(browser)
    labirint_augh_page.go_to_site()
    labirint_augh_page.click_on_the_augh_button_one()
    labirint_augh_page.enter_code("A16E-43C0-8CC2")
    labirint_augh_page.click_on_the_augh_button_two()
    labirint_augh_page.click_on_the_augh_button_three()
    words = labirint_augh_page.check_page_contain_words()
    assert "Код скидки A16E-43C0-8CC2" in words
    time.sleep(4)

def test_add_cart(browser):
    labirint_add_book = AddBookHelper(browser)
    labirint_add_book.go_to_site()
    labirint_add_book.enter_word("Экспансия")
    labirint_add_book.click_on_the_search_button()
    labirint_add_book.click_on_the_book()
    labirint_add_book.click_on_the_add_button()
    labirint_add_book.click_on_the_cart_button()
    elements = labirint_add_book.check_navigation_bar_cart()
    assert "Начать оформление" in elements

def test_hold_book(browser):
    labirint_hold_book = AddBookHelper(browser)
    labirint_hold_book.go_to_site()
    labirint_hold_book.enter_word("Пушкин")
    labirint_hold_book.click_on_the_search_button()
    labirint_hold_book.click_on_the_two_book()
    labirint_hold_book.click_on_the_hold_over_button()
    labirint_hold_book.click_on_the_hold_button()
    elements = labirint_hold_book.check_navigation_bar_hold()
    assert "Пушкин. Сказки" in elements

def test_history(browser):
    labirint_history = AddBookHelper(browser)
    labirint_history.go_to_site()
    labirint_history.enter_word("Пушкин")
    labirint_history.click_on_the_search_button()
    labirint_history.click_on_the_two_book()
    labirint_history.click_on_the_hold_over_button()
    labirint_history.click_on_the_button_my_cab()
    labirint_history.click_on_the_history_button()
    elements = labirint_history.check_navigation_history()
    assert "Вы недавно смотрели" in elements

def test_order_history(browser):
    labirint_order_history = AddBookHelper(browser)
    labirint_order_history.go_to_site()
    labirint_order_history.click_on_the_button_my_cab()
    labirint_order_history.click_on_the_button_order()
    elements = labirint_order_history.check_navigation_order_history()
    assert elements

def test_coupons(browser):
    labirint_coupon = AddBookHelper(browser)
    labirint_coupon.go_to_site()
    labirint_coupon.click_on_the_button_my_cab()
    labirint_coupon.click_on_the_button_coupon()
    elements = labirint_coupon.check_navigation_coupon()
    assert "КУПОН" in elements

def test_balance(browser):
    labirint_balance = AddBookHelper(browser)
    labirint_balance.go_to_site()
    labirint_balance.click_on_the_button_my_cab()
    labirint_balance.click_on_the_button_balance()
    elements = labirint_balance.check_navigation_balance()
    assert "За что начислена сумма" in elements

def test_recommendations(browser):
    labirint_recommendations = AddBookHelper(browser)
    labirint_recommendations.go_to_site()
    labirint_recommendations.click_on_the_button_my_cab()
    labirint_recommendations.click_on_the_button_recommendations()
    elements = labirint_recommendations.check_navigation_recommendations()
    assert "Сегодня" in elements

def test_comparison(browser):
    labirint_comparison = AddBookHelper(browser)
    labirint_comparison.go_to_site()
    labirint_comparison.click_on_the_button_my_cab()
    labirint_comparison.click_on_the_button_comparison()
    elements = labirint_comparison.check_navigation_comparison()
    assert "Сравнение товаров" in elements

def test_reviews(browser):
    labirint_reviews = AddBookHelper(browser)
    labirint_reviews.go_to_site()
    labirint_reviews.click_on_the_button_my_cab()
    labirint_reviews.click_on_the_button_reviews()
    elements = labirint_reviews.check_navigation_reviews()
    assert "Читатели выбирают сегодня" in elements

def test_settings(browser):
    labirint_settings = AddBookHelper(browser)
    labirint_settings.go_to_site()
    labirint_settings.click_on_the_button_my_cab()
    labirint_settings.click_on_the_button_settings()
    elements = labirint_settings.check_navigation_settings()
    assert "Персональная информация" in elements

@pytest.mark.parametrize("name", [("Сергей"), ("SERGEY"), ("Sergeyyyyyyy"),
                                 ("2OOFJJVN73638")])
def test_negaive_settings_change_name(browser, name):
    labirint_change_settings = AddBookHelper(browser)
    labirint_change_settings.go_to_site()
    labirint_change_settings.click_on_the_button_my_cab()
    labirint_change_settings.click_on_the_button_settings()
    labirint_change_settings.enter_name_setting(name)
    labirint_change_settings.click_on_the_button_save_settings()
    elements = labirint_change_settings.check_navigation_settings()
    assert elements

@pytest.mark.parametrize("lname", [("ivanov"), ("ИВАНОВ"), ("Петрррррров"), ("Петрррррров")])
def test_negaive_settings_change_lname(browser, lname):
    labirint_change_lname_settings = AddBookHelper(browser)
    labirint_change_lname_settings.go_to_site()
    labirint_change_lname_settings.click_on_the_button_my_cab()
    labirint_change_lname_settings.click_on_the_button_settings()
    labirint_change_lname_settings.enter_surname_setting(lname)
    labirint_change_lname_settings.click_on_the_button_save_settings()
    elements = labirint_change_lname_settings.check_navigation_settings()
    assert elements

@pytest.mark.parametrize("midname", [("ivanovich"), ("ИВАНОВИЧ"), ("Петррррррович")])
def test_negaive_settings_change_midname(browser, midname):
    labirint_change_midname_settings = AddBookHelper(browser)
    labirint_change_midname_settings.go_to_site()
    labirint_change_midname_settings.click_on_the_button_my_cab()
    labirint_change_midname_settings.click_on_the_button_settings()
    labirint_change_midname_settings.enter_patronymic_setting(midname)
    labirint_change_midname_settings.click_on_the_button_save_settings()
    elements = labirint_change_midname_settings.check_navigation_settings()
    assert elements

@pytest.mark.parametrize("dbirth", [("10.10.1991"), ("10102020"), ("одинадцатое")])
def test_negaive_settings_change_dbirth(browser, dbirth):
    labirint_change_dbirth_settings = AddBookHelper(browser)
    labirint_change_dbirth_settings.go_to_site()
    labirint_change_dbirth_settings.click_on_the_button_my_cab()
    labirint_change_dbirth_settings.click_on_the_button_settings()
    labirint_change_dbirth_settings.enter_date_of_birth_setting(dbirth)
    labirint_change_dbirth_settings.click_on_the_button_save_settings()
    elements = labirint_change_dbirth_settings.check_navigation_settings()
    assert elements

@pytest.mark.parametrize("login", [("Serg"), ("10102020serg"), ("10102020"), ("Сергей")])
def test_negaive_settings_change_login(browser, login):
    labirint_change_login_settings = AddBookHelper(browser)
    labirint_change_login_settings.go_to_site()
    labirint_change_login_settings.click_on_the_button_my_cab()
    labirint_change_login_settings.click_on_the_button_settings()
    labirint_change_login_settings.enter_login_setting(login)
    labirint_change_login_settings.click_on_the_button_save_settings()
    elements = labirint_change_login_settings.check_navigation_settings()
    assert elements

@pytest.mark.parametrize("phone", [("89149214590"), ("79659315762"), ("+79821145698")])
def test_negaive_settings_change_phone(browser, phone):
    labirint_change_phone_settings = AddBookHelper(browser)
    labirint_change_phone_settings.go_to_site()
    labirint_change_phone_settings.click_on_the_button_my_cab()
    labirint_change_phone_settings.click_on_the_button_settings()
    labirint_change_phone_settings.enter_login_setting(phone)
    labirint_change_phone_settings.click_on_the_button_save_settings()
    elements = labirint_change_phone_settings.check_navigation_settings()
    assert elements

def test_support(browser):
    labirint_support = AddBookHelper(browser)
    labirint_support.go_to_site()
    labirint_support.click_on_the_button_support()
    elements = labirint_support.check_navigation_support()
    assert "Задать вопрос" in elements

def test_sales(browser):
    labirint_sales = AddBookHelper(browser)
    labirint_sales.go_to_site()
    labirint_sales.click_on_the_button_sales()
    elements = labirint_sales.check_navigation_sales()
    assert "Все акции сегодня" in elements

@pytest.mark.parametrize("name", [("Сергей"), ("SERGEY")])
@pytest.mark.parametrize("lname", [("ivanov"), ("сидоров")])
@pytest.mark.parametrize("midname", [("ivanovich"), ("ИВАНОВИЧ")])
@pytest.mark.parametrize("dbirth", [("10.10.1991"), ("10102020")])
@pytest.mark.parametrize("login", [("Serg"), ("10102020serg")])
@pytest.mark.parametrize("phone", [("89149214590"), ("79659315762")])
def test_negaive_settings_change_info(browser, name, lname, midname, dbirth, login, phone):
    labirint_change_all_settings = AddBookHelper(browser)
    labirint_change_all_settings.go_to_site()
    labirint_change_all_settings.click_on_the_button_my_cab()
    labirint_change_all_settings.click_on_the_button_settings()
    labirint_change_all_settings.enter_name_setting(name)
    labirint_change_all_settings.enter_surname_setting(lname)
    labirint_change_all_settings.enter_patronymic_setting(midname)
    labirint_change_all_settings.enter_date_of_birth_setting(dbirth)
    labirint_change_all_settings.enter_login_setting(phone)
    labirint_change_all_settings.enter_login_setting(login)
    labirint_change_all_settings.click_on_the_button_save_settings()
    elements = labirint_change_all_settings.check_navigation_settings()
    assert elements

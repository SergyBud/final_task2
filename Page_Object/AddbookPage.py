from BaseApp import BasePage
from selenium.webdriver.common.by import By

class LabirintCartLocators:
    LOCATOR_LABIRINT_SEARCH_FIELD = (By.ID, "search-field")
    LOCATOR_LABIRINT_SEARCH_BUTTON = (By.CLASS_NAME, "b-header-b-search-e-btn")
    LOCATOR_LABIRINT_OPEN_BOOK = (By.CSS_SELECTOR, "#rubric-tab > div.b-search-page-content > div:nth-child(1)"
                                                   " > div.products-row-outer.responsive-cards "
                                                   "> div > div:nth-child(2) > div > div.product-cover > a > span")
    LOCATOR_LABIRINT_ADD_CART_BTN = (By.CSS_SELECTOR, "#buyingbtns708301 > a > span")
    LOCATOR_LABIRINT_CART_BTN = (By.CSS_SELECTOR, "#minwidth > div.top-header > div > div.b-header > div.b-header-b-"
                                                  "personal.col-xs-6.col-sm-9.col-md-5.col-md-push-5.col-lg-push-"
                                                  "6.col-lg-4.col-xxl-push-7.col-xxl-3.js-toggle-menu-block > div > ul "
                                                  "> li.b-header-b-personal-e-list-item.have-dropdown.last-child > a")
    LOCATOR_LABIRINT_NAVIGATION_BAR_CART = (By.XPATH, "/html/body/div[1]/div[4]/div[3]/div/div/div/div/div/div[2]/"
                                                      "div/div[3]/div/div/div/div/div[1]/form/div[4]/div[3]/div/button")
    LOCATOR_LABIRINT_OPEN_BOOK_TWO = (By.CSS_SELECTOR, "#rubric-tab > div.b-search-page-content > div:nth-child(1) "
                                                       "> div.products-row-outer.responsive-cards > div > div:nth-"
                                                       "child(2) > div > div.product-cover > a > span")
    LOCATOR_LABIRINT_HOLD_OVER_BTN = (By.CSS_SELECTOR, "#buyingbtns694583 > div.product-icons > a.fave > span")
    LOCATOR_LABIRINT_HOLD_BTN = (By.XPATH, "#minwidth > div.top-header > div > div.b-header > div.b-header-b-personal."
                                           "col-xs-6.col-sm-9.col-md-5.col-md-push-5.col-lg-push-6.col-lg-4.col-xxl-"
                                           "push-7.col-xxl-3.js-toggle-menu-block > div > ul > li:nth-child(5) > a")
    LOCATOR_LABIRINT_NAVIGATION_BAR_HOLD = (By.CSS_SELECTOR, "#right-inner > div:nth-child(2) > div > form > div."
                                                             "products-row-outer > div > div.product.need-watch."
                                                             "product_labeled.product-cart.watched > div > div.product"
                                                             "-cover.short-title > a.cover > span.product-title")
    LOCATOR_LABIRINT_BTN_MY_CAB = (By.CSS_SELECTOR, "#minwidth > div.top-header > div > div.b-header > div.b-header-b-"
                                             "personal.col-xs-6.col-sm-9.col-md-5.col-md-push-5.col-lg-push-6."
                                             "col-lg-4.col-xxl-push-7.col-xxl-3.js-toggle-menu-block > div > ul"
                                             " > li.b-header-b-personal-e-list-item.have-dropdown.b-header-b-personal"
                                             "-e-list-item_cabinet > a")
    LOCATOR_LABIRINT_HISTORY_BTN = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div > div."
                                                     "cabinet-menu.swiper-container-initialized.swiper-container-"
                                                     "horizontal.swiper-container-free-mode > ul > li.cabinet-menu__"
                                                     "tab.cabinet-menu__tab_active > a > span")
    LOCATOR_LABIRINT_NAVIGATION_BAR_HISTORY = (By.XPATH, "/html/body/div[7]/div[1]/div[2]/div/div[1]")
    LOCATOR_LABIRINT_BTN_ORDER = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div > div."
                                                   "cabinet-menu.swiper-container-initialized.swiper-container"
                                                   "-horizontal.swiper-container-free-mode > ul > li.cabinet-menu"
                                                   "__tab.cabinet-menu__tab_active.swiper-slide-next > a")
    LOCATOR_LABIRINT_NAVIGATION_ORDER_HISTORY = (By.XPATH, "/html/body/div[1]/div[6]/div[3]/div[2]/div/div/div/div"
                                                           "/div[2]/div/div/div[4]/form/div/div[1]/span")
    LOCATOR_LABIRINT_BTN_COUPON = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div > div.cabinet"
                                                    "-menu.swiper-container-initialized.swiper-container-horizontal"
                                                    ".swiper-container-free-mode > ul > li:nth-child(3) > a")
    LOCATOR_LABIRINT_NAVIGATION_COUPON = (By.CSS_SELECTOR, "#right-inner > div > div > div:nth-child(1)")
    LOCATOR_LABIRINT_BTN_BALANCE = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div > div.cabinet"
                                                     "-menu.swiper-container-initialized.swiper-container-horizontal."
                                                     "swiper-container-free-mode > ul > li:nth-child(4) > a")
    LOCATOR_LABIRINT_NAVIGATION_BALANCE = (By.CSS_SELECTOR, "#cabinet > div.mr20.table-container-responsive > table"
                                                            " > tbody > tr.headers_Balance_hist > td:nth-child(2)")
    LOCATOR_LABIRINT_BTN_RECOMMENDATIONS = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div "
                                                             "> div.cabinet-menu.swiper-container-initialized.swiper"
                                                             "-container-horizontal.swiper-container-free-mode > ul"
                                                             " > li:nth-child(5) > a")
    LOCATOR_LABIRINT_NAVIGATION_RECOMMENDATIONS = (By.CSS_SELECTOR, "#right-inner > div > div:nth-child(2)")
    LOCATOR_LABIRINT_BTN_COMPARISON = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div > div."
                                                        "cabinet-menu.swiper-container-initialized.swiper-container"
                                                        "-horizontal.swiper-container-free-mode > ul > li:nth-child(8)"
                                                        " > a > span")
    LOCATOR_LABIRINT_NAVIGATION_COMPARISON = (By.CSS_SELECTOR, "#right-inner > h1")
    LOCATOR_LABIRINT_BTN_REVIEWS = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div > div.cabinet"
                                                     "-menu.swiper-container-initialized.swiper-container-horizontal."
                                                     "swiper-container-free-mode > ul > li:nth-child(9) > a")
    LOCATOR_LABIRINT_NAVIGATION_REVIEWS = (By.CSS_SELECTOR, "#cabinet > div > div.onmain-bestbooks-block.bestsellers"
                                                            " > div.h2 > a")
    LOCATOR_LABIRINT_BTN_SETTINGS = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div > div.cabinet"
                                                      "-menu.swiper-container-initialized.swiper-container-horizontal."
                                                      "swiper-container-free-mode > ul > li:nth-child(10) > a > span")
    LOCATOR_LABIRINT_NAVIGATION_SETTINGS = (By.CSS_SELECTOR, "#info_form > div.page-contact-info--form-right-left-"
                                                             "block > div.page-contact-info--form-left-block > "
                                                             "div.page-contact-info--header-left-block-form")
    LOCATOR_LABIRINT_NAME_SETTINGS = (By.CSS_SELECTOR, "#firstname")
    LOCATOR_LABIRINT_SURNAME_SETTINGS = (By.CSS_SELECTOR, "#lastname")
    LOCATOR_LABIRINT_PATRONYMIC_SETTINGS = (By.CSS_SELECTOR, "#middlename")
    LOCATOR_LABIRINT_DATE_OF_BIRTH_SETTINGS = (By.CSS_SELECTOR, "#bday")
    LOCATOR_LABIRINT_LOGIN_SETTINGS = (By.CSS_SELECTOR, "#nick")
    LOCATOR_LABIRINT_PHONE_SETTINGS = (By.CSS_SELECTOR, "#user_add_number_mobile")
    LOCATOR_LABIRINT_BTN_SAVE_SETTINGS = (By.CSS_SELECTOR, "#info_form > div.mt20.mb30 > input")
    LOCATOR_LABIRINT_NAVIGATION_CHANGE_SETTINGS = (By.CSS_SELECTOR, "#formvalidate-labellastname > span."
                                                                    "formvalidate-error-label-e-text")
    LOCATOR_LABIRINT_BTN_CONTACTS = (By.XPATH, "/html/body/div[1]/div[4]/div[4]/div/div[2]/div/ul/li[9]/a")
    LOCATOR_LABIRINT_NAVIGATION_CONTACTS = (By.CSS_SELECTOR, "#right-inner > div > h1:nth-child(1)")
    LOCATOR_LABIRINT_BTN_SUPPORT = (By.CSS_SELECTOR, "#minwidth > div.top-header > div > div.b-header-b-sec-menu."
                                                     "col-md-12 > div > ul > li:nth-child(10) > a")
    LOCATOR_LABIRINT_NAVIGATION_SUPPORT = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div > "
                                                            "div:nth-child(1) > div > div > a")
    LOCATOR_LABIRINT_BTN_SALES = (By.CSS_SELECTOR, "#minwidth > div.top-header > div > div.b-header-b-sec-"
                                                   "menu.col-md-12 > div > ul > li:nth-child(5) > a")
    LOCATOR_LABIRINT_NAVIGATION_SALES = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div.content"
                                                          "-block > div > div.h2.relative.main-block-"
                                                          "carousel-title-outer > a")
    LOCATOR_LABIRINT_BTN_BOOKS = (By.CSS_SELECTOR, "#minwidth > div.top-header > div.b-header-outer > div.b-header "
                                                   "> div.b-header-b-menu.col-xs-12.col-sm-12.col-md-10.js-toggle-"
                                                   "menu-block > div > div.js-b-header-b-menu-e-slider > ul > li:nth"
                                                   "-child(1) > span > a")
    LOCATOR_LABIRINT_NAVIGATION_BOOKS = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > "
                                                          "div:nth-child(3) > div > h1")
    LOCATOR_LABIRINT_BTN_MAIN_2021 = (By.CSS_SELECTOR, "#minwidth > div.top-header > div.b-header-outer > div.b-header"
                                                       " > div.b-header-b-menu.col-xs-12.col-sm-12.col-md-10.js-toggle"
                                                       "-menu-block > div > div.js-b-header-b-menu-e-slider > ul >"
                                                       " li:nth-child(2) > span > a")
    LOCATOR_LABIRINT_NAVIGATION_MAIN_2021 = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div.top"
                                                              "-b-contaner.best-page-container > div.top-b-header >"
                                                              " div > h1")
    LOCATOR_LABIRINT_BTN_SCHOOL = (By.CSS_SELECTOR, "#minwidth > div.top-header > div.b-header-outer > div.b-header "
                                                    "> div.b-header-b-menu.col-xs-12.col-sm-12.col-md-10.js-toggle-"
                                                    "menu-block > div > div.js-b-header-b-menu-e-slider > ul > li:nth"
                                                    "-child(3) > span > a")
    LOCATOR_LABIRINT_NAVIGATION_SCHOOL = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div.school"
                                                           "-cap.school-cap_background > h1")
    LOCATOR_LABIRINT_BTN_TOYS = (By.CSS_SELECTOR, "#minwidth > div.top-header > div.b-header-outer > div.b-header > "
                                                  "div.b-header-b-menu.col-xs-12.col-sm-12.col-md-10.js-toggle-menu-"
                                                  "block > div > div.js-b-header-b-menu-e-slider > ul > li:nth-child(4)"
                                                  " > span > a")
    LOCATOR_LABIRINT_NAVIGATION_TOYS = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div.content-"
                                                         "block-outer.genre-header-color > div > h1")
    LOCATOR_LABIRINT_BTN_STATIONERY = (By.CSS_SELECTOR, "#minwidth > div.top-header > div.b-header-outer > div.b-header"
                                                        " > div.b-header-b-menu.col-xs-12.col-sm-12.col-md-10.js-"
                                                        "toggle-menu-block > div > div.js-b-header-b-menu-e-slider "
                                                        "> ul > li:nth-child(5) > span > a")
    LOCATOR_LABIRINT_NAVIGATION_STATIONERY = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div."
                                                               "content-block-outer.genre-header-color > div > h1")
    LOCATOR_LABIRINT_BTN_CLUB = (By.CSS_SELECTOR, "#minwidth > div.top-header > div.b-header-outer > div.b-header > "
                                                  "div.b-header-b-menu.col-xs-12.col-sm-12.col-md-10.js-toggle-menu"
                                                  "-block > div > div.js-b-header-b-menu-e-slider > ul > li:nth-"
                                                  "child(11) > span > a")
    LOCATOR_LABIRINT_NAVIGATION_CLUB = (By.CSS_SELECTOR, "#right-inner > h1")
    LOCATOR_LABIRINT_BTN_CLUB_NOW = (By.CSS_SELECTOR, "#minwidth > div.top-submenu > div > div > div > ul > li:nth"
                                                      "-child(2) > a")
    LOCATOR_LABIRINT_NAVIGATION_CLUB_NOW = (By.CSS_SELECTOR, "#begin > div.b-goodssets-list.js-b-goodssets-list >"
                                                             " div.mt40.b-goodssets-row > h2")
    LOCATOR_LABIRINT_BTN_CLUB_KID_NAVI = (By.CSS_SELECTOR, "#minwidth > div.top-submenu > div > div > div > ul > "
                                                           "li:nth-child(3) > a")
    LOCATOR_LABIRINT_NAVIGATION_CLUB_KID_NAVI = (By.CSS_SELECTOR, "#right-inner > div.b-goodssets-head.b-goodssets-"
                                                                  "head-m-tm > div > div > div > div.b-goodssets-"
                                                                  "head-inner > div > div.b-goodssets-head-e-title.b"
                                                                  "-goodssets-head-e-title-m-tm")
    LOCATOR_LABIRINT_BTN_CLUB_JOURNALS = (By.CSS_SELECTOR, "#minwidth > div.top-submenu > div > div > div > ul >"
                                                           " li:nth-child(4) > a")
    LOCATOR_LABIRINT_NAVIGATION_CLUB_JOURNALS = (By.CSS_SELECTOR, "#right-inner > div > h1")
    LOCATOR_LABIRINT_BTN_CLUB_REVIEWS = (By.CSS_SELECTOR, "#minwidth > div.top-submenu > div > div > div > ul >"
                                                          " li:nth-child(5) > a")
    LOCATOR_LABIRINT_NAVIGATION_CLUB_REVIEWS = (By.CSS_SELECTOR, "#newslist > div.ratingmenu > div")
    LOCATOR_LABIRINT_BTN_CLUB_REVIEWS_TWO = (By.CSS_SELECTOR, "#minwidth > div.top-submenu > div > div > div > ul "
                                                              "> li:nth-child(6) > a")
    LOCATOR_LABIRINT_NAVIGATION_CLUB_REVIEWS_TWO = (By.CSS_SELECTOR, "#stab-slider-frame > ul > li.b-stab-e-slider-"
                                                                     "item.b-stab-e-slider-item-m-active > a > span")
    LOCATOR_LABIRINT_BTN_CLUB_COMPILATIONS = (By.CSS_SELECTOR, "#minwidth > div.top-submenu > div > div > div > ul"
                                                               " > li:nth-child(7) > a")
    LOCATOR_LABIRINT_NAVIGATION_CLUB_COMPILATIONS = (By.CSS_SELECTOR, "#right-inner > div:nth-child(1) > table "
                                                                      "> tbody > tr:nth-child(1) > td:nth-child(1) "
                                                                      "> div > h2")
    LOCATOR_LABIRINT_BTN_CLUB_LITTESTS = (By.CSS_SELECTOR, "#minwidth > div.top-submenu > div > div > div > ul >"
                                                           " li:nth-child(8) > a")
    LOCATOR_LABIRINT_NAVIGATION_CLUB_LITTESTS = (By.CSS_SELECTOR, "#contests > h1")
    LOCATOR_LABIRINT_BTN_CLUB_CONTESTS = (By.CSS_SELECTOR, "#minwidth > div.top-submenu > div > div > div > ul"
                                                           " > li:nth-child(9) > a")
    LOCATOR_LABIRINT_NAVIGATION_CLUB_CONTESTS = (By.CSS_SELECTOR, "#contests > h1")
    LOCATOR_LABIRINT_BTN_STATIONERY_ACCESORIES = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > "
                                                                   "div:nth-child(2) > div > div.subgenres > ul "
                                                                   "> li:nth-child(1) > a")
    LOCATOR_LABIRINT_NAVIGATION_STATIONERY_ACCESORIES = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content"
                                                                          " > div.content-block-outer.genre-header"
                                                                          "-color > div > h1")
    LOCATOR_LABIRINT_BTN_STATIONERY_OFFICE = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div:"
                                                               "nth-child(2) > div > div.subgenres > ul > "
                                                               "li:nth-child(4) > a")
    LOCATOR_LABIRINT_NAVIGATION_STATIONERY_OFFICE = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content "
                                                                      "> div.content-block-outer.genre-header-color "
                                                                      "> div > h1")
    LOCATOR_LABIRINT_BTN_STATIONERY_DRAWING = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > "
                                                                "div:nth-child(2) > div > div.subgenres > ul "
                                                                "> li:nth-child(7) > a")
    LOCATOR_LABIRINT_NAVIGATION_STATIONERY_DRAWING = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content "
                                                                       "> div.content-block-outer.genre-header-color "
                                                                       "> div > h1")
    LOCATOR_LABIRINT_BTN_STATIONERY_GOODS = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > "
                                                              "div:nth-child(2) > div > div.subgenres > ul > "
                                                              "li:nth-child(10) > a")
    LOCATOR_LABIRINT_NAVIGATION_STATIONERY_GOODS = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content "
                                                                     "> div.content-block-outer.genre-header-color "
                                                                     "> div > h1")
    LOCATOR_LABIRINT_BTN_STATIONERY_GLOBES = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > "
                                                               "div:nth-child(2) > div > div.subgenres > ul "
                                                               "> li:nth-child(2) > a")
    LOCATOR_LABIRINT_NAVIGATION_STATIONERY_GLOBES = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content "
                                                                      "> div.content-block-outer.genre-header-color "
                                                                      "> div > h1")
    LOCATOR_LABIRINT_BTN_STATIONERY_FOLDERS = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > "
                                                                "div:nth-child(4) > div > div.subgenres > ul > "
                                                                "li:nth-child(5) > a")
    LOCATOR_LABIRINT_NAVIGATION_STATIONERY_FOLDERS = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content "
                                                                       "> div.content-block-outer.genre-header-color "
                                                                       "> div > h1")
    LOCATOR_LABIRINT_BTN_STATIONERY_PAINTING = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > "
                                                                 "div:nth-child(4) > div > div.subgenres > "
                                                                 "ul > li:nth-child(8) > a")
    LOCATOR_LABIRINT_NAVIGATION_STATIONERY_PAINTING = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content >"
                                                                        " div.content-block-outer.genre-header-color "
                                                                        "> div > h1")
    LOCATOR_LABIRINT_BTN_STATIONERY_DOCUMENTS = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div:"
                                                                  "nth-child(4) > div > div.subgenres > ul > "
                                                                  "li:nth-child(3) > a")
    LOCATOR_LABIRINT_NAVIGATION_STATIONERY_DOCUMENTS = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content"
                                                                         " > div.content-block-outer.genre-header-color"
                                                                         " > div > h1")
    LOCATOR_LABIRINT_BTN_STATIONERY_WRITING = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > "
                                                                "div:nth-child(4) > div > div.subgenres > ul "
                                                                "> li:nth-child(6) > a")
    LOCATOR_LABIRINT_NAVIGATION_STATIONERY_WRITING = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content "
                                                                       "> div.content-block-outer.genre-header-color "
                                                                       "> div > h1")
    LOCATOR_LABIRINT_BTN_STATIONERY_BAGS = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div:nth-ch"
                                                             "ild(4) > div > div.subgenres > ul > li:nth-child(9) > a")
    LOCATOR_LABIRINT_NAVIGATION_STATIONERY_BAGS = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > "
                                                                    "div.content-block-outer.genre-header-color > "
                                                                    "div > h1")
    LOCATOR_LABIRINT_BTN_MAIN_TODAY = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div.top-b-"
                                                        "contaner.best-page-container > div:nth-child(2) > div > "
                                                        "ul > li.swiper-slide.swiper-slide-next > a")
    LOCATOR_LABIRINT_NAVIGATION_MAIN_TODAY = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > "
                                                               "div.best-catalog > div.content-block-outer > div > div")
    LOCATOR_LABIRINT_BTN_MAIN_CHILDREN = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div.top-b-"
                                                           "contaner.best-page-container > div.content-block > div "
                                                           "> ul > li:nth-child(3) > a")
    LOCATOR_LABIRINT_NAVIGATION_MAIN_CHILDREN = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > "
                                                                  "div.top-b-contaner.best-page-container > div.top"
                                                                  "-b-backgroud > div > div.only_desc > h1")
    LOCATOR_LABIRINT_BTN_MAIN_LITERATURE = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div.top-"
                                                             "b-contaner.best-page-container > div.content-block "
                                                             "> div > ul > li:nth-child(4) > a")
    LOCATOR_LABIRINT_NAVIGATION_MAIN_LITERATURE = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > "
                                                                    "div.top-b-contaner.best-page-container > div."
                                                                    "top-b-backgroud > div > h1")
    LOCATOR_LABIRINT_BTN_MAIN_NONFIK = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div.top-b-"
                                                         "contaner.best-page-container > div:nth-child(2) > div "
                                                         "> ul > li:nth-child(5) > a")
    LOCATOR_LABIRINT_NAVIGATION_MAIN_NONFIK = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div"
                                                                ".top-b-contaner.best-page-container > div.top-b"
                                                                "-backgroud > div > h1")
    LOCATOR_LABIRINT_BTN_MAIN_PRESENT = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div.top-b-"
                                                          "contaner.best-page-container > div:nth-child(2) > "
                                                          "div > ul > li:nth-child(6) > a")
    LOCATOR_LABIRINT_NAVIGATION_MAIN_PRESENT = (By.CSS_SELECTOR, "#minwidth > div.top-margin > div.top-content > div."
                                                                 "top-b-contaner.best-page-container >"
                                                                 " div.top-b-backgroud > div > h1")


class AddBookHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_SEARCH_BUTTON, time=10).click()

    def click_on_the_book(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_OPEN_BOOK, time=10).click()

    def click_on_the_add_button(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_ADD_CART_BTN, time=10).click()

    def click_on_the_cart_button(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_CART_BTN, time=10).click()

    def check_navigation_bar_cart(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_BAR_CART, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_two_book(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_OPEN_BOOK_TWO, time=10).click()

    def click_on_the_hold_over_button(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_HOLD_OVER_BTN, time=10).click()

    def click_on_the_hold_button(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_HOLD_BTN, time=10).click()

    def check_navigation_bar_hold(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_BAR_HOLD, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_button_my_cab(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_MY_CAB, time=10).click()

    def click_on_the_history_button(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_HISTORY_BTN, time=10).click()

    def check_navigation_history(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_BAR_HISTORY, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_button_order(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_ORDER, time=10).click()

    def check_navigation_order_history(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_ORDER_HISTORY, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_button_coupon(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_COUPON, time=10).click()

    def check_navigation_coupon(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_COUPON, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_button_balance(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_BALANCE, time=10).click()

    def check_navigation_balance(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_BALANCE, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_button_recommendations(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_RECOMMENDATIONS, time=10).click()

    def check_navigation_recommendations(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_RECOMMENDATIONS, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_button_comparison(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_COMPARISON, time=10).click()

    def check_navigation_comparison(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_COMPARISON, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_button_reviews(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_REVIEWS, time=10).click()

    def check_navigation_reviews(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_REVIEWS, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_button_settings(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_SETTINGS, time=10).click()

    def check_navigation_settings(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_SETTINGS, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def enter_name_setting(self, name):
        search_field = self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_NAME_SETTINGS)
        search_field.click()
        search_field.send_keys(name)
        return search_field

    def enter_surname_setting(self, lname):
        search_field = self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_SURNAME_SETTINGS)
        search_field.click()
        search_field.send_keys(lname)
        return search_field

    def enter_patronymic_setting(self, midname):
        search_field = self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_PATRONYMIC_SETTINGS)
        search_field.click()
        search_field.send_keys(midname)
        return search_field

    def enter_date_of_birth_setting(self, dbirth):
        search_field = self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_DATE_OF_BIRTH_SETTINGS)
        search_field.click()
        search_field.send_keys(dbirth)
        return search_field

    def enter_login_setting(self, login):
        search_field = self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_LOGIN_SETTINGS)
        search_field.click()
        search_field.send_keys(login)
        return search_field

    def enter_phone_setting(self, phone):
        search_field = self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_PHONE_SETTINGS)
        search_field.click()
        search_field.send_keys(phone)
        return search_field


    def click_on_the_button_save_settings(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_SAVE_SETTINGS, time=10).click()

    def check_navigation_change_settings(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_CHANGE_SETTINGS, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_button_contacts(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_CONTACTS, time=10).click()

    def check_navigation_contacts(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_CONTACTS, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_button_support(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_SUPPORT, time=10).click()

    def check_navigation_support(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_SUPPORT, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_button_sales(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_SALES, time=10).click()

    def check_navigation_sales(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_SALES, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_books(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_BOOKS, time=10).click()

    def check_navigation_books(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_BOOKS, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_main_2021(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_MAIN_2021, time=10).click()

    def check_navigation_main_2021(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_MAIN_2021, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_school(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_SCHOOL, time=10).click()

    def check_navigation_school(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_SCHOOL, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_toys(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_TOYS, time=10).click()

    def check_navigation_toys(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_TOYS, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_stationery(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_STATIONERY, time=10).click()

    def check_navigation_stationery(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_STATIONERY, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_club(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_CLUB, time=10).click()

    def check_navigation_club(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_CLUB, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_club_now(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_CLUB_NOW, time=10).click()

    def check_navigation_club_now(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_CLUB_NOW, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_club_kid_navi(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_CLUB_KID_NAVI, time=10).click()

    def check_navigation_club_kid_navi(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_CLUB_KID_NAVI, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_club_journals(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_CLUB_JOURNALS, time=10).click()

    def check_navigation_club_journals(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_CLUB_JOURNALS, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_club_reviews(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_CLUB_REVIEWS, time=10).click()

    def check_navigation_club_reviews(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_CLUB_REVIEWS, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_club_reviews_two(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_CLUB_REVIEWS_TWO, time=10).click()

    def check_navigation_club_reviews_two(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_CLUB_REVIEWS_TWO, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_club_compilations(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_CLUB_COMPILATIONS, time=10).click()

    def check_navigation_club_compilations(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_CLUB_COMPILATIONS, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_club_littests(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_CLUB_LITTESTS, time=10).click()

    def check_navigation_club_littests(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_CLUB_LITTESTS, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_club_contests(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_CLUB_CONTESTS, time=10).click()

    def check_navigation_club_contests(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_CLUB_CONTESTS, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_stationery_accessories(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_STATIONERY_ACCESORIES, time=10).click()

    def check_navigation_stationery_accessories(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_STATIONERY_ACCESORIES, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_stationery_office(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_STATIONERY_OFFICE, time=10).click()

    def check_navigation_stationery_office(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_STATIONERY_OFFICE, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_stationery_drawing(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_STATIONERY_DRAWING, time=10).click()

    def check_navigation_stationery_drawing(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_STATIONERY_DRAWING, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_stationery_goods(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_STATIONERY_GOODS, time=10).click()

    def check_navigation_stationery_goods(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_STATIONERY_GOODS, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_stationery_globes(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_STATIONERY_GLOBES, time=10).click()

    def check_navigation_stationery_globes(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_STATIONERY_GLOBES, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_stationery_folders(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_STATIONERY_FOLDERS, time=10).click()

    def check_navigation_stationery_folders(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_STATIONERY_FOLDERS, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_stationery_painting(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_STATIONERY_PAINTING, time=10).click()

    def check_navigation_stationery_painting(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_STATIONERY_PAINTING, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_stationery_documents(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_STATIONERY_DOCUMENTS, time=10).click()

    def check_navigation_stationery_documents(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_STATIONERY_DOCUMENTS, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_stationery_writing(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_STATIONERY_WRITING, time=10).click()

    def check_navigation_stationery_writing(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_STATIONERY_WRITING, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_stationery_bags(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_STATIONERY_BAGS, time=10).click()

    def check_navigation_stationery_bags(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_STATIONERY_BAGS, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_main_today(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_MAIN_TODAY, time=10).click()

    def check_navigation_main_today(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_MAIN_TODAY, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_main_children(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_MAIN_CHILDREN, time=10).click()

    def check_navigation_main_children(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_MAIN_CHILDREN, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_main_literature(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_MAIN_LITERATURE, time=10).click()

    def check_navigation_main_literature(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_MAIN_LITERATURE, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_main_nonfikn(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_MAIN_NONFIK, time=10).click()

    def check_navigation_main_nonfikn(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_MAIN_NONFIK, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

    def click_on_the_main_present(self):
        return self.find_element(LabirintCartLocators.LOCATOR_LABIRINT_BTN_MAIN_PRESENT, time=10).click()

    def check_navigation_main_present(self):
        all_list = self.find_elements(LabirintCartLocators.LOCATOR_LABIRINT_NAVIGATION_MAIN_PRESENT, time=10)
        nav_bar_cart_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_cart_menu

from labirintPages import SearchHelper
from NegativeAuthPage import NegativeAuthorizationHelper
from AughPage import AuthorizationHelper
from AddbookPage import AddBookHelper
import time
import pytest
import mouse

def test_books(browser):
    labirint_books = AddBookHelper(browser)
    labirint_books.go_to_site()
    labirint_books.click_on_the_books()
    elements = labirint_books.check_navigation_books()
    assert "Книги" in elements

def test_main_2021(browser):
    labirint_main_2021 = AddBookHelper(browser)
    labirint_main_2021.go_to_site()
    labirint_main_2021.click_on_the_main_2021()
    elements = labirint_main_2021.check_navigation_main_2021()
    assert "Главные книги 2021" in elements

def test_school(browser):
    labirint_school = AddBookHelper(browser)
    labirint_school.go_to_site()
    labirint_school.click_on_the_school()
    elements = labirint_school.check_navigation_school()
    assert "Все учебники в Лабиринте" in elements

def test_toys(browser):
    labirint_toys = AddBookHelper(browser)
    labirint_toys.go_to_site()
    labirint_toys.click_on_the_toys()
    elements = labirint_toys.check_navigation_toys()
    assert "Игры и игрушки" in elements

def test_stationery(browser):
    labirint_stationery = AddBookHelper(browser)
    labirint_stationery.go_to_site()
    labirint_stationery.click_on_the_stationery()
    elements = labirint_stationery.check_navigation_stationery()
    assert "Канцелярские товары" in elements

def test_club(browser):
    labirint_club = AddBookHelper(browser)
    labirint_club.go_to_site()
    labirint_club.click_on_the_club()
    elements = labirint_club.check_navigation_club()
    assert "Клуб" in elements

def test_club_now(browser):
    labirint_club = AddBookHelper(browser)
    labirint_club.go_to_site()
    labirint_club.click_on_the_club()
    labirint_club.click_on_the_club_now()
    elements = labirint_club.check_navigation_club_now()
    assert "Упомянутые книги" in elements

def test_club_kid_navi(browser):
    labirint_club = AddBookHelper(browser)
    labirint_club.go_to_site()
    labirint_club.click_on_the_club()
    labirint_club.click_on_the_club_kid_navi()
    elements = labirint_club.check_navigation_club_kid_navi()
    assert "От «Алисы» до «Шерлока». Об интерактивных книгах «Лабиринт Пресс»" in elements

def test_club_journals(browser):
    labirint_club = AddBookHelper(browser)
    labirint_club.go_to_site()
    labirint_club.click_on_the_club()
    labirint_club.click_on_the_club_journals()
    elements = labirint_club.check_navigation_club_journals()
    assert "Журнальный лабиринт" in elements

def test_club_reviews(browser):
    labirint_club = AddBookHelper(browser)
    labirint_club.go_to_site()
    labirint_club.click_on_the_club()
    labirint_club.click_on_the_club_reviews()
    elements = labirint_club.check_navigation_club_reviews()
    assert "Книжные обзоры и рецензии" in elements

def test_club_reviews_two(browser):
    labirint_club = AddBookHelper(browser)
    labirint_club.go_to_site()
    labirint_club.click_on_the_club()
    labirint_club.click_on_the_club_reviews_two()
    elements = labirint_club.check_navigation_club_reviews_two()
    assert "Рецензии" in elements

def test_club_compilations(browser):
    labirint_club = AddBookHelper(browser)
    labirint_club.go_to_site()
    labirint_club.click_on_the_club()
    labirint_club.click_on_the_club_compilations()
    elements = labirint_club.check_navigation_club_compilations()
    assert "Ребенку для чтения" in elements

def test_club_littests(browser):
    labirint_club = AddBookHelper(browser)
    labirint_club.go_to_site()
    labirint_club.click_on_the_club()
    labirint_club.click_on_the_club_littests()
    elements = labirint_club.check_navigation_club_littests()
    assert "Литературные тесты" in elements

def test_club_contests(browser):
    labirint_club = AddBookHelper(browser)
    labirint_club.go_to_site()
    labirint_club.click_on_the_club()
    labirint_club.click_on_the_club_contests()
    elements = labirint_club.check_navigation_club_contests()
    assert "Конкурсы" in elements

def test_stationery_accessories(browser):
    labirint_stationery = AddBookHelper(browser)
    labirint_stationery.go_to_site()
    labirint_stationery.click_on_the_stationery()
    labirint_stationery.click_on_the_stationery_accessories()
    elements = labirint_stationery.check_navigation_stationery_accessories()
    assert "Аксессуары для книг" in elements

def test_stationery_office(browser):
    labirint_stationery = AddBookHelper(browser)
    labirint_stationery.go_to_site()
    labirint_stationery.click_on_the_stationery()
    labirint_stationery.click_on_the_stationery_office()
    elements = labirint_stationery.check_navigation_stationery_office()
    assert "Офисная канцелярия" in elements

def test_stationery_office(browser):
    labirint_stationery = AddBookHelper(browser)
    labirint_stationery.go_to_site()
    labirint_stationery.click_on_the_stationery()
    labirint_stationery.click_on_the_stationery_drawing()
    elements = labirint_stationery.check_navigation_stationery_drawing()
    assert "Принадлежности для черчения" in elements

def test_stationery_goods(browser):
    labirint_stationery = AddBookHelper(browser)
    labirint_stationery.go_to_site()
    labirint_stationery.click_on_the_stationery()
    labirint_stationery.click_on_the_stationery_goods()
    elements = labirint_stationery.check_navigation_stationery_goods()
    assert "Товары для школы" in elements

def test_stationery_globes(browser):
    labirint_stationery = AddBookHelper(browser)
    labirint_stationery.go_to_site()
    labirint_stationery.click_on_the_stationery()
    labirint_stationery.click_on_the_stationery_globes()
    elements = labirint_stationery.check_navigation_stationery_globes()
    assert "Глобусы" in elements

def test_stationery_folders(browser):
    labirint_stationery = AddBookHelper(browser)
    labirint_stationery.go_to_site()
    labirint_stationery.click_on_the_stationery()
    labirint_stationery.click_on_the_stationery_folders()
    elements = labirint_stationery.check_navigation_stationery_folders()
    assert "Папки, скоросшиватели, разделители" in elements

def test_stationery_painting(browser):
    labirint_stationery = AddBookHelper(browser)
    labirint_stationery.go_to_site()
    labirint_stationery.click_on_the_stationery()
    labirint_stationery.click_on_the_stationery_painting()
    elements = labirint_stationery.check_navigation_stationery_painting()
    assert "Рисование" in elements

def test_stationery_documents(browser):
    labirint_stationery = AddBookHelper(browser)
    labirint_stationery.go_to_site()
    labirint_stationery.click_on_the_stationery()
    labirint_stationery.click_on_the_stationery_documents()
    elements = labirint_stationery.check_navigation_stationery_documents()
    assert "Обложки для документов" in elements

def test_stationery_writing(browser):
    labirint_stationery = AddBookHelper(browser)
    labirint_stationery.go_to_site()
    labirint_stationery.click_on_the_stationery()
    labirint_stationery.click_on_the_stationery_writing()
    elements = labirint_stationery.check_navigation_stationery_writing()
    assert "Письменные принадлежности" in elements

def test_stationery_bags(browser):
    labirint_stationery = AddBookHelper(browser)
    labirint_stationery.go_to_site()
    labirint_stationery.click_on_the_stationery()
    labirint_stationery.click_on_the_stationery_bags()
    elements = labirint_stationery.check_navigation_stationery_bags()
    assert "Сумки" in elements

def test_main_2021(browser):
    labirint_main_2021 = AddBookHelper(browser)
    labirint_main_2021.go_to_site()
    labirint_main_2021.click_on_the_main_2021()
    labirint_main_2021.click_on_the_main_today()
    elements = labirint_main_2021.check_navigation_main_today()
    assert "Весь каталог" in elements

def test_main_children(browser):
    labirint_main_2021 = AddBookHelper(browser)
    labirint_main_2021.go_to_site()
    labirint_main_2021.click_on_the_main_2021()
    labirint_main_2021.click_on_the_main_children()
    elements = labirint_main_2021.check_navigation_main_children()
    assert "Читатели выбирают сегодня" in elements

def test_main_literature(browser):
    labirint_main_2021 = AddBookHelper(browser)
    labirint_main_2021.go_to_site()
    labirint_main_2021.click_on_the_main_2021()
    labirint_main_2021.click_on_the_main_literature()
    elements = labirint_main_2021.check_navigation_main_literature()
    assert "Топ-10 художественной литературы в октябре" in elements

def test_main_nonfikn(browser):
    labirint_main_2021 = AddBookHelper(browser)
    labirint_main_2021.go_to_site()
    labirint_main_2021.click_on_the_main_2021()
    labirint_main_2021.click_on_the_main_nonfikn()
    elements = labirint_main_2021.check_navigation_main_nonfikn()
    assert "Топ-10 нон-фикшн в  октябре" in elements

def test_main_present(browser):
    labirint_main_2021 = AddBookHelper(browser)
    labirint_main_2021.go_to_site()
    labirint_main_2021.click_on_the_main_2021()
    labirint_main_2021.click_on_the_main_present()
    elements = labirint_main_2021.check_navigation_main_present()
    assert "Топ-10 подарочных изданий в октябре" in elements






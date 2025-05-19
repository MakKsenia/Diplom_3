import allure
from locators.main_functionality_locators import MainFunctionalityLocators
from pages.main_functionality_page import MainFunctionalityPage
import data
from data import user_data

@allure.title('Проверка основного функционала')
class TestMainFunctionalityPage:
    @allure.title('Проверка Переход по клику на «Лента заказов»')
    def test_go_to_feed_order(self, driver):
        page_element = MainFunctionalityPage(driver)
        page_element.main_page_loading_wait()
        page_element.feed_order_click()
        assert page_element.get_current_url() == data.ORDER_FEED

    @allure.title('Проверка переход по клику на «Конструктор»')
    def test_go_to_constructor(self, driver):
        page_element = MainFunctionalityPage(driver)
        page_element.main_page_loading_wait()
        page_element.feed_order_click()
        page_element.main_page_loading_wait()
        page_element.constructor_click()
        assert page_element.get_current_url() == data.MAIN_URL

    @allure.title('Проверка, если кликнуть на ингредиент, появится всплывающее окно с деталями»')
    def test_go_to_details_feed(self, driver):
        page_element = MainFunctionalityPage(driver)
        page_element.main_page_loading_wait()
        page_element.crater_bun_click()
        page_element.main_page_loading_wait()
        page_element.wait_for_element_details_feed(MainFunctionalityLocators.CRATER_DETAILS_FIELD)
        page_element = MainFunctionalityPage(driver)
        assert page_element.is_element_details_feed_displayed

    @allure.title('Проверка, что всплывающее окно Детали заказа закрывается кликом по крестику')
    def test_close_details_field(self, driver):
        page_element = MainFunctionalityPage(driver)
        page_element.main_page_loading_wait()
        page_element.crater_bun_click()
        page_element.main_page_loading_wait()
        page_element.wait_for_element_details_feed(MainFunctionalityLocators.CRATER_DETAILS_FIELD)
        page_element.main_page_loading_wait()
        page_element.details_feed_close_click()
        page_element = MainFunctionalityPage(driver)
        assert page_element.is_element_crater_bun_displayed

    @allure.title('Проверка, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_ingredient_counter_increased(self, driver):
        page_element = MainFunctionalityPage(driver)
        page_element.main_page_loading_wait()
        page_element.put_ingredient_into_order()
        page_element.main_page_loading_wait()
        assert page_element.get_ingredient_count() == 2

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    def test_logined_user_able_to_make_order(self, driver):
        page_element = MainFunctionalityPage(driver)
        page_element.main_page_loading_wait()
        page_element.put_ingredient_into_order()
        page_element.main_page_loading_wait()
        page_element.account_login_bun_click()
        page_element.main_page_loading_wait()
        email = user_data['email']
        page_element.set_email_input(email)
        password = user_data['password']
        page_element.set_password_input(password)
        page_element.main_page_loading_wait()
        page_element.account_login_bun_click()
        page_element.main_page_loading_wait()
        page_element.make_order_click()
        assert page_element.is_element_order_id_displayed


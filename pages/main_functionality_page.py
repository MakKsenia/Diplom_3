
from locators.personal_cabinet_locators import PersonalCabinetLocators
from pages.base_page import BasePage
import allure
from locators.main_functionality_locators import MainFunctionalityLocators

class MainFunctionalityPage(BasePage):

    @allure.step('Ждем загрузки главной')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(PersonalCabinetLocators.OVERLAY)

    @allure.step('Нажимаем на кнопку Лента заказов')
    def feed_order_click(self):
        self.click(MainFunctionalityLocators.ORDER_FEED_BUTTON)

    @allure.step('Нажимаем на кнопку Конструктор')
    def constructor_click(self):
        self.click(MainFunctionalityLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Нажимаем на кнопку Краторная булка')
    def crater_bun_click(self):
        self.click(MainFunctionalityLocators.CRATER_BUN)

    @allure.step('Ожидаем появления поля Детали ингредиента')
    def wait_for_element_details_feed(self, locator):
        self.wait_and_find_element(MainFunctionalityLocators.CRATER_DETAILS_FIELD)

    @allure.step("Проверка отображения поля Детали ингредиента")
    def is_element_details_feed_displayed(self):
        return self.is_element_displayed(MainFunctionalityLocators.CRATER_DETAILS_FIELD)

    @allure.step('Нажимаем на крестик в поле Детали ингредиента')
    def details_feed_close_click(self):
        self.click(MainFunctionalityLocators.CLOSE_DETAILS_FIELD)

    @allure.step("Проверка отображения поля Детали ингредиента")
    def is_element_crater_bun_displayed(self):
        return self.is_element_displayed(MainFunctionalityLocators.CRATER_BUN)

    @allure.step('Нажимаем на кнопку Войти в аккаунт')
    def account_login_bun_click(self):
        self.click(MainFunctionalityLocators.ACCOUNT_LOGIN_BUTTON)

    @allure.step('Вводим в поле Email электронную почту для входа в личный кабинет')
    def set_email_input(self, email):
        email_input = self.wait_and_find_element(PersonalCabinetLocators.EMAIL_FIELD)
        email_input.send_keys(email)

    @allure.step('Вводим в поле Пароль пароль для входа в личный кабинет')
    def set_password_input(self, password):
        email_input = self.wait_and_find_element(PersonalCabinetLocators.PASSWORD_INPUT_FIElD)
        email_input.send_keys(password)

    @allure.step('Нажимаем на кнопку Войти после ввода логина и пароля')
    def account_login_bun_click(self):
        self.click(PersonalCabinetLocators.LOGIN_BUTTON)

    @allure.step('Нажимаем на кнопку Оформить заказ')
    def make_order_click(self):
        self.click(MainFunctionalityLocators.MAKE_ORDER_BUTTON)

    @allure.step('Ожидаем появления кнопки Краторная булка')
    def wait_for_element_bun(self):
        self.wait_and_find_element(MainFunctionalityLocators.CRATER_BUN)

    @allure.step('Ожидаем появления поля Булки в заказе')
    def wait_for_element_bun_in_order(self):
        self.wait_and_find_element(MainFunctionalityLocators.BUN_FIELD_IN_ORDER)

    @allure.step('Перетащить элемент в заказ')
    def put_ingredient_into_order(self):
        self.drag_and_drop_element(MainFunctionalityLocators.CRATER_BUN, MainFunctionalityLocators.BUN_FIELD_IN_ORDER)

    @allure.step('Перетащить элемент в заказ')
    def put_ingredient_into_order(self):
        self.main_page_loading_wait()
        ingredient = self.wait_and_find_element(locator=MainFunctionalityLocators.CRATER_BUN)
        basket = self.wait_and_find_element(locator=MainFunctionalityLocators.BUN_FIELD_IN_ORDER)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step("Получение количества добавленных ингредиентов")
    def get_ingredient_count(self):
        return int(self.get_text(MainFunctionalityLocators.INGREDIENT_COUNTER))

    @allure.step("Проверка отображения поля с идентификатором заказа")
    def is_element_order_id_displayed(self):
        return self.is_element_displayed(MainFunctionalityLocators.ID_ORDER_FIELD)

    @allure.step('Запрашиваем URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url
from pages.base_page import BasePage
import allure
from locators.personal_cabinet_locators import PersonalCabinetLocators

class PersonalCabinetPage(BasePage):

    @allure.step('Ждем загрузки главной')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(PersonalCabinetLocators.OVERLAY)

    @allure.step('Запрашиваем URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url


    @allure.step('Нажимаем на кнопку Личный кабинет')
    def personal_cabinet_click(self):
        self.click(PersonalCabinetLocators.PERSONAL_ACCOUNT)

    @allure.step('Нажимаем на кнопку Войти')
    def personal_cabinet_enter_click(self):
        self.click(PersonalCabinetLocators.LOGIN_BUTTON)

    @allure.step('Вводим в поле Email электронную почту для входа в личный кабинет')
    def set_email_input(self, email):
        email_input = self.wait_and_find_element(PersonalCabinetLocators.EMAIL_FIELD)
        email_input.send_keys(email)

    @allure.step('Вводим в поле Пароль пароль для входа в личный кабинет')
    def set_password_input(self, password):
        email_input = self.wait_and_find_element(PersonalCabinetLocators.PASSWORD_INPUT_FIElD)
        email_input.send_keys(password)

    @allure.step('Скроллим на до элемента Личный кабинет по локатору')
    def scroll_personal_cabinet(self):
        element = self.driver.find_element(PersonalCabinetLocators.PERSONAL_ACCOUNT)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    @allure.step('Ожидаем появления кнопки история заказов')
    def wait_for_element_order_history(self):
        self.wait_and_find_element(PersonalCabinetLocators.ORDER_HISTORY_FIELD)

    @allure.step('Нажимаем на кнопку История Заказов')
    def order_history_button_click(self):
        self.click(PersonalCabinetLocators.ORDER_HISTORY_FIELD)

    @allure.step('Нажимаем на кнопку Выход')
    def logout_button_click(self):
        self.click(PersonalCabinetLocators.LOGOUT_BUTTON)

    @allure.step('Ожидаем появления кнопки Войти')
    def wait_for_element_login(self):
        self.wait_and_find_element(PersonalCabinetLocators.LOGIN_BUTTON)

    @allure.step("Получение последнего заказа в истории заказов")
    def get_last_order_in_history(self):
        self.wait_until_visible(PersonalCabinetLocators.ORDER_HISTORY_LIST)
        return self.get_text(PersonalCabinetLocators.LAST_ORDER_NUMBER)


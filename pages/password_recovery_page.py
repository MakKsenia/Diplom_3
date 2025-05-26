from pages.base_page import BasePage
import allure
from locators.password_recovery_locators import PasswordRecoveryLocators

class PasswordRecoveryPage(BasePage):

    @allure.step('Ждем загрузки главной')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(PasswordRecoveryLocators.OVERLAY)

    @allure.step('Нажимаем на кнопку Личный кабинет')
    def personal_cabinet_click(self):
        self.click(PasswordRecoveryLocators.PERSONAL_ACCOUNT)

    @allure.step('Нажимаем на кнопку Восстановить пароль на странице Личного кабинета')
    def password_recovery_button_click(self):
        self.click(PasswordRecoveryLocators.RESTORE_PASSWORD_BUTTON)

    @allure.step('Ожидаем появление элемента кнопка Восстановить')
    def wait_and_find_element_recovery_appears(self):
        self.wait_and_find_element(PasswordRecoveryLocators.RESTORE_BUTTON)

    @allure.step('Вводим в поле Email электронную почту для восстановления пароля')
    def set_email_input(self,email ):
        email_input = self.wait_and_find_element(PasswordRecoveryLocators.RESTORE_PASSWORD_EMAIL_INPUT)
        email_input.send_keys(email)

    @allure.step('Нажимаем на кнопку Восстановить')
    def restore_button_click(self):
        self.click(PasswordRecoveryLocators.RESTORE_BUTTON)

    @allure.step('Ожидаем появления Поле ввода пароля для восстановления')
    def wait_for_element_password_field_appears(self):
        self.wait_and_find_element(PasswordRecoveryLocators.RESET_PASSWORD_PASSWORD_INPUT)

    @allure.step('Ожидаем появление элемента Кнопка показать/скрыть пароль')
    def wait_and_find_element_icon_action(self):
        self.wait_and_find_element(PasswordRecoveryLocators.ICON_ACTION_BUTTON)

    @allure.step('Нажимаем Кнопка показать/скрыть пароль')
    def icon_action_button_click(self):
        self.click(PasswordRecoveryLocators.ICON_ACTION_BUTTON)

    @allure.step('Ожидаем появления активности (подсвечивания) Поля пароль после клика по кнопке показать/скрыть')
    def wait_for_element_active_field_appears(self):
        self.wait_and_find_element(PasswordRecoveryLocators.ACTIVE_PASSWORD_FIELD_FRAME)

    @allure.step('Проверить, что значение поля password отображается')
    def check_displaying_password_value(self):
        return self.wait_and_find_element(PasswordRecoveryLocators.ACTIVE_PASSWORD_FIELD_FRAME)

    @allure.step('Запрашиваем URL текущей страницы')
    def get_current_url(self):
        return super().get_current_url()
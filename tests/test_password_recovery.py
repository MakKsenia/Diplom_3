import allure

import urls
from pages.password_recovery_page import PasswordRecoveryPage
from data import user_data

@allure.title('Проверка восстановления пароля')
class TestPasswordRecoveryPage:
    @allure.title('Проверка Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_recovery_page(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.main_page_loading_wait()
        password_recovery_page.personal_cabinet_click()
        password_recovery_page.main_page_loading_wait()
        password_recovery_page.password_recovery_button_click()
        password_recovery_page.main_page_loading_wait()
        assert password_recovery_page.get_current_url() == urls.FORGOT_PASSWORD_PAGE

    @allure.title('Проверка "Ввод почты и клик по кнопке «Восстановить»"')
    def test_input_email_and_go_to_recovery_button(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.main_page_loading_wait()
        password_recovery_page.personal_cabinet_click()
        password_recovery_page.password_recovery_button_click()
        email = user_data['email']
        password_recovery_page.set_email_input(email)
        password_recovery_page.main_page_loading_wait()
        password_recovery_page.restore_button_click()
        password_recovery_page.main_page_loading_wait()
        assert password_recovery_page.get_current_url() == urls.RESET_PASSWORD_PAGE

    @allure.title('Проверка "Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его"')
    def test_active_password_field_frame(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.main_page_loading_wait()
        password_recovery_page.personal_cabinet_click()
        password_recovery_page.main_page_loading_wait()
        password_recovery_page.password_recovery_button_click()
        email = user_data['email']
        password_recovery_page.set_email_input(email)
        password_recovery_page.main_page_loading_wait()
        password_recovery_page.restore_button_click()
        password_recovery_page.main_page_loading_wait()
        password_recovery_page.wait_and_find_element_icon_action()
        password_recovery_page.main_page_loading_wait()
        password_recovery_page.icon_action_button_click()
        password_recovery_page.main_page_loading_wait()
        assert password_recovery_page.check_displaying_password_value()




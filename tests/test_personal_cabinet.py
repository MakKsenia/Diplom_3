import allure
from pages.personal_cabinet_page import PersonalCabinetPage
import data
from data import user_data

@allure.title('Личный кабинет')
class TestPasswordRecoveryPage:
    @allure.title('Проверка переход по клику на «Личный кабинет»,')
    def test_go_to_personal_cabinet(self, driver):
        personal_cabinet_page = PersonalCabinetPage(driver)
        personal_cabinet_page.main_page_loading_wait()
        personal_cabinet_page.personal_cabinet_click()
        personal_cabinet_page.personal_cabinet_click()
        assert personal_cabinet_page.get_current_url() == data.LOGIN_PAGE

    @allure.title('Проверка "переход в раздел «История заказов"')
    def test_go_to_order_history(self, driver):
        personal_cabinet_page = PersonalCabinetPage(driver)
        personal_cabinet_page.main_page_loading_wait()
        personal_cabinet_page.personal_cabinet_click()
        email = user_data['email']
        personal_cabinet_page.set_email_input(email)
        password = user_data['password']
        personal_cabinet_page.set_password_input(password)
        personal_cabinet_page.personal_cabinet_enter_click()
        personal_cabinet_page.main_page_loading_wait()
        personal_cabinet_page.personal_cabinet_click()
        personal_cabinet_page.wait_for_element_order_history()
        personal_cabinet_page.main_page_loading_wait()
        personal_cabinet_page.order_history_button_click()
        personal_cabinet_page.main_page_loading_wait()
        assert personal_cabinet_page.get_current_url() == data.ORDER_HISTORY

    @allure.title('Проверка "Выход из аккаунта"')
    def test_log_out_personal_logout(self, driver):
        personal_cabinet_page = PersonalCabinetPage(driver)
        personal_cabinet_page.main_page_loading_wait()
        personal_cabinet_page.personal_cabinet_click()
        email = user_data['email']
        personal_cabinet_page.set_email_input(email)
        password = user_data['password']
        personal_cabinet_page.set_password_input(password)
        personal_cabinet_page.personal_cabinet_enter_click()
        personal_cabinet_page.main_page_loading_wait()
        personal_cabinet_page.personal_cabinet_click()
        personal_cabinet_page.wait_for_element_order_history()
        personal_cabinet_page.main_page_loading_wait()
        personal_cabinet_page.order_history_button_click()
        personal_cabinet_page.main_page_loading_wait()
        personal_cabinet_page.logout_button_click()
        personal_cabinet_page.main_page_loading_wait()
        assert personal_cabinet_page.get_current_url() == data.LOGIN_PAGE



import allure

from locators.order_feed_locators import OrderFeedLocators
from pages.main_functionality_page import MainFunctionalityPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_cabinet_page import PersonalCabinetPage
from data import user_data

@allure.title('Проверка раздела «Лента заказов»')
class TestOrderFeedPage:
    @allure.title('Проверка, что если кликнуть на заказ, откроется всплывающее окно с деталями»')
    def test_go_to_feed_order(self, driver):
        page_element = OrderFeedPage(driver)
        page_element.main_page_loading_wait()
        page_element.feed_order_click()
        page_element.main_page_loading_wait()
        page_element.wait_for_element_order_feed(OrderFeedLocators.FIRST_ORDER_BUTTON)
        page_element.main_page_loading_wait()
        page_element.first_order_click()
        page_element.main_page_loading_wait()
        assert page_element.is_modal_order_displayed()

    @allure.title('Проверка, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов')
    def test_user_orders_history_visible_in_order_feed(self, driver):
        personal_cabinet_page = PersonalCabinetPage(driver)
        order_feed_page = OrderFeedPage(driver)
        personal_cabinet_page.main_page_loading_wait()
        personal_cabinet_page.personal_cabinet_click()
        personal_cabinet_page.main_page_loading_wait()
        email = user_data['email']
        personal_cabinet_page.set_email_input(email)
        personal_cabinet_page.main_page_loading_wait()
        password = user_data['password']
        personal_cabinet_page.set_password_input(password)
        personal_cabinet_page.main_page_loading_wait()
        personal_cabinet_page.personal_cabinet_enter_click()
        personal_cabinet_page.main_page_loading_wait()
        personal_cabinet_page.personal_cabinet_click()
        personal_cabinet_page.main_page_loading_wait()
        personal_cabinet_page.wait_for_element_order_history()
        personal_cabinet_page.main_page_loading_wait()
        personal_cabinet_page.order_history_button_click()
        personal_cabinet_page.main_page_loading_wait()
        last_order_number = personal_cabinet_page.get_last_order_in_history()
        personal_cabinet_page.main_page_loading_wait()
        order_feed_page.feed_order_click()
        order_feed_page.wait_for_element_order_feed(OrderFeedLocators.ORDER_FEED_LIST)
        assert order_feed_page.find_order_in_feed(last_order_number), f"Заказ с номером {last_order_number} найден в ленте заказов"

    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_new_order_increase_total_counter(self, driver):
        order_feed_page = OrderFeedPage(driver)
        page_element = MainFunctionalityPage(driver)
        page_element.main_page_loading_wait()
        order_feed_page.feed_order_click()
        initial_completed_count = order_feed_page.get_completed_total_orders_count()
        page_element.main_page_loading_wait()
        page_element.constructor_click()
        page_element.main_page_loading_wait()
        page_element.wait_for_element_bun()
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
        page_element.main_page_loading_wait()
        order_feed_page.order_details_close_click()
        page_element.main_page_loading_wait()
        page_element.feed_order_click()
        order_feed_page.wait_for_element_order_total()
        page_element.main_page_loading_wait()
        # Проверяем, что значение счётчика увеличилось
        updated_completed_count = order_feed_page.get_completed_total_orders_count()
        assert updated_completed_count > initial_completed_count, "Счётчик за все время увеличился после создания заказа"

    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_new_order_increase_total_counter_current_data(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.feed_order_click()
        initial_completed_count = order_feed_page.get_completed_total_orders_count_current_data()
        page_element = MainFunctionalityPage(driver)
        page_element.main_page_loading_wait()
        page_element.constructor_click()
        page_element.main_page_loading_wait()
        page_element.wait_for_element_bun()
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
        page_element.main_page_loading_wait()
        order_feed_page.order_details_close_click()
        page_element.main_page_loading_wait()
        page_element.feed_order_click()
        order_feed_page.wait_for_element_order_total()
        page_element.main_page_loading_wait()
        # Проверяем, что значение счётчика увеличилось
        updated_completed_count = order_feed_page.get_completed_total_orders_count_current_data()
        assert updated_completed_count > initial_completed_count, "Счётчик за сегодня увеличился после создания заказа"

    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе В работе')
    def test_id_order_in_progress_section_after_creation(self, driver):
        order_feed_page = OrderFeedPage(driver)
        page_element = MainFunctionalityPage(driver)
        page_element.main_page_loading_wait()
        personal_cabinet_page = PersonalCabinetPage(driver)
        personal_cabinet_page.main_page_loading_wait()
        personal_cabinet_page.personal_cabinet_click()
        email = user_data['email']
        page_element.set_email_input(email)
        password = user_data['password']
        page_element.set_password_input(password)
        page_element.main_page_loading_wait()
        page_element.account_login_bun_click()
        # Открываем второе окно для Ленты заказов
        order_feed_page.open_new_window('https://stellarburgers.nomoreparties.site/feed')
        windows = order_feed_page.get_window_handles()
        main_window = windows[0]
        feed_window = windows[1]
        # Оформляем заказ в первом окне
        order_feed_page.switch_to_window(main_window)
        order_feed_page.main_page_loading_wait()
        page_element.constructor_click()
        page_element.main_page_loading_wait()
        page_element.wait_for_element_bun()
        page_element.main_page_loading_wait()
        page_element.put_ingredient_into_order()
        page_element.main_page_loading_wait()
        page_element.make_order_click()
        # Извлекаем номер заказа из модального окна с ожиданием его появления
        order_number = order_feed_page.get_order_number()
        page_element.main_page_loading_wait()
        # Переходим во второе окно с лентой заказов
        order_feed_page.switch_to_window(feed_window)
        page_element.main_page_loading_wait()
        # Проверяем, что заказ появился в разделе "В работе"
        assert order_feed_page.is_order_in_progress(order_number), f"Заказ с номером {order_number} найден в разделе 'В работе'"

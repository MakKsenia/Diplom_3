import allure
import data
import urls
from locators.main_functionality_locators import MainFunctionalityLocators
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage

class OrderFeedPage(BasePage):
    @allure.step('Ждем загрузки главной')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(OrderFeedLocators.OVERLAY)

    @allure.step('Нажимаем на кнопку Лента заказов')
    def feed_order_click(self):
        self.click(OrderFeedLocators.ORDER_FEED_BUTTON)

    @allure.step('Ожидаем появления поля списка заказов')
    def wait_for_element_order_feed(self, locator):
        self.wait_and_find_element(OrderFeedLocators.FIRST_ORDER_BUTTON)

    @allure.step('Скроллим, пока не увидим нужный элемент по локатору')
    def scroll_to_open_first_order(self):
        self.scroll(OrderFeedLocators.FIRST_ORDER_BUTTON)

    @allure.step("Открываем окно заказа")
    def first_order_click(self):
        self.click(OrderFeedLocators.FIRST_ORDER_BUTTON)

    @allure.step("Проверка отображения окна c деталями заказа")
    def is_modal_order_displayed(self):
        return self.is_element_displayed(OrderFeedLocators.ORDER_DETAILS_FIELD)

    @allure.step("Поиск заказа в ленте по номеру")
    def find_order_in_feed(self, order_number):
        # Форматируем номер заказа с префиксом, если он используется в интерфейсе
        order_number_with_prefix = f"#{order_number.lstrip('#')}"

        # Убедимся, что список заказов виден
        self.wait_until_visible(OrderFeedLocators.ORDER_FEED_LIST)

        # Используем уже методы "is_text_in_elements" в BasePage для проверки текста в элементах
        return self.is_text_in_elements(OrderFeedLocators.ORDER_FEED_LIST, order_number_with_prefix)

    @allure.step("Получение количества выполненных заказов за всё время")
    def get_completed_total_orders_count(self):
        completed_count_text = self.get_text(OrderFeedLocators.ORDER_COMPLETED_TOTAL)
        return int(completed_count_text)

    @allure.step("Получение количества выполненных заказов за сегодня")
    def get_completed_total_orders_count_current_data(self):
        completed_count_text = self.get_text(OrderFeedLocators.ORDER_COMPLETED_TODAY)
        return int(completed_count_text)

    @allure.step("Проверка наличия заказа в разделе 'В работе'")
    def check_order_in_progress(self, order_number):
        return self.wait_for_condition(lambda _: self.is_order_in_progress(order_number))

    @allure.step('Ожидаем появления кратерной булки')
    def wait_for_element_bun(self):
        self.wait_and_find_element(MainFunctionalityLocators.CRATER_BUN)

    @allure.step('Ожидаем появления количества заказов за все время')
    def wait_for_element_order_total(self):
        self.wait_and_find_element(OrderFeedLocators.ORDER_COMPLETED_TOTAL)

    @allure.step('Нажимаем на кнопку Войти в аккаунт')
    def order_details_close_click(self):
        self.click(OrderFeedLocators.CLOSE_ORDER_DETAILS_FIELD)

    @allure.step("Открытие нового окна с URL: {url}")
    def open_new_window_for_check(self):
        self.open_new_window(urls.ORDER_FEED)

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        # Ожидание появления номера заказа в модальном окне
        self.wait_until_visible(OrderFeedLocators.ORDER_NUMBER_MODAL)

        # Ожидание, пока номер заказа изменится с заглушки "9999" на другой номер
        order_number_element = self.wait_and_find_element(OrderFeedLocators.ORDER_NUMBER_MODAL)
        self.wait_for_condition(lambda driver: order_number_element.text != "9999")

        return order_number_element.text

    @allure.step("Проверка, что заказ в разделе 'В работе'")
    def is_order_in_progress(self, order_number):
        # Получаем все элементы с номерами заказов "В работе"
        orders_in_progress_elements = self.wait_and_find_elements(OrderFeedLocators.ORDERS_IN_PROGRESS)

        # Извлекаем текст и убираем ведущие нули
        orders_in_progress = [el.text.lstrip('0') for el in orders_in_progress_elements]

        # Проверяем наличие нужного номера заказа
        return order_number.lstrip('0') in orders_in_progress





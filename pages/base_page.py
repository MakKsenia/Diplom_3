import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step('Ждем пока элемент станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step('Запрашиваем URL текущей страницы')
    def get_current_url(self, url):
        return self.driver.current_url

    @allure.step('Переключаем драйвер')
    def switch_driver(self):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Очевидно дожидаемся нужного элемента по локатору')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Очевидно дожидаемся нужных элементов по локатору')
    def wait_and_find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))


    @allure.step('Ожидание появления заголовка на странице')
    def wait_for_title_is(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))

    @allure.step('Дожидаемся смены URL страницы')
    def wait_url_changes(self, url):
        WebDriverWait(self.driver, 15).until(EC.url_changes(url))

    @allure.step('Кликаем по элементу с нужным локатором')
    def click(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    @allure.step('Скроллим, пока не увидим нужный элемент по локатору')
    def scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_and_find_element(locator, timeout)
        return element.text

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_and_find_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )

    @allure.step("Проверка отображения элемента")
    def is_element_displayed(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Ожидание видимости элемента")
    def wait_until_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Получение текста всех элементов из писка по локатору")
    def get_elements_text(self, locator):
        elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
        return [element.text for element in elements]

    @allure.step("Проверка, что текст '{text}' присутствует в списке элементов")
    def is_text_in_elements(self, locator, text):
        # Получаем текст всех элементов, соответствующих локатору
        elements_text = self.get_elements_text(locator)
        # Проверяем, содержится ли нужный текст в списке элементов
        return any(text == element_text.strip() for element_text in elements_text)

    @allure.step("Ожидание выполнения условия")
    def wait_for_condition(self, condition, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(condition)
            return True
        except TimeoutException:
            return False

    @allure.step("Открытие нового окна с URL: {url}")
    def open_new_window(self, url):
        self.driver.execute_script(f"window.open('{url}', '_blank');")

    @allure.step("Получение списка всех окон")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключение на окно")
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)
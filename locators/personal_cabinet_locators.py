from selenium.webdriver.common.by import By

class PersonalCabinetLocators:
    PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')  # Кнопка "Личный Кабинет на главной странице"
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')  # Кнопка "Войти" на странице входа в Личный кабинет
    ORDER_HISTORY_FIELD = (By.XPATH, '//a[@href = "/account/order-history"]')  # Кнопка "История заказов" в Личном кабинете
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')  # Кнопка "Выйти" в Личном Кабинете
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    EMAIL_FIELD = (By.XPATH, '//input[@class="text input__textfield text_type_main-default" and @name="name"]') #Поле ввода email
    PASSWORD_INPUT_FIElD = (By.XPATH, ".//input[@type='password']")
    ORDER_HISTORY_LIST = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList__374GU')]//li")
    LAST_ORDER_NUMBER = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList__374GU')]//li[last()]//p[contains(@class, 'text_type_digits-default')]")

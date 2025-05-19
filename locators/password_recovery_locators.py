from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:
    PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')  # Кнопка "Личный Кабинет на главной странице"
    RESTORE_PASSWORD_BUTTON = (By.XPATH, '//a[contains(text(), "Восстановить пароль")]')  # Кнопка "Восстановить пароль" на странице входа
    RESTORE_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')  # Кнопка "Восстановить" на странице после нажатия на кнопку Восстановить пароль
    RESTORE_PASSWORD_EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Поле ввода Email на странице после нажатия Востановить пароль
    RESET_PASSWORD_PASSWORD_INPUT = (By.NAME, 'Пароль')  # Поле ввода Пароля на странице послеввода Email и нажатия кнопки "Восстановить"
    ICON_ACTION_BUTTON = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]') #Кнопка показать/скрыть пароль
    ACTIVE_PASSWORD_FIELD_FRAME  = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, "input_status_active")]') #Поле пароль активное(подсвечено) после клика по кнопке показать/скрыть

    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"


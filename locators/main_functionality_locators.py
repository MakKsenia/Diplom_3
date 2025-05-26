from selenium.webdriver.common.by import By

class MainFunctionalityLocators:
    ORDER_FEED_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and .//p[text()='Лента Заказов']]")  # Кнопка Лента заказов на главной странице"
    CONSTRUCTOR_BUTTON = ( By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and .//p[text()='Конструктор']]") # Кнопка Конструктор на главной странице"
    CRATER_BUN =  (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH']") # Кнопка Краторная булка в конструкторе"
    CRATER_DETAILS_FIELD = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")  # Поле деталей краторной булки
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    CLOSE_DETAILS_FIELD = (By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]') # Крестик закрытия деталей ингредиента
    ACCOUNT_LOGIN_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')  # Кнопка Войти в аккаунт
    MAKE_ORDER_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')  # Кнопка Оформить заказ
    ID_ORDER_FIELD = (By.XPATH, '//p[@class="undefined text text_type_main-medium mb-15"]')  # Поле с идентификатором заказа
    BUN_FIELD_IN_ORDER = (By.XPATH, '//span[@class="constructor-element__text"]')  # Поле булки в заказе
    INGREDIENT_COUNTER =  (By.XPATH, "//p[@class='counter_counter__num__3nue1' and text()='2']") #Cчетчик ингредиента
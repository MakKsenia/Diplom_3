from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')  # Кнопка Лента заказов на главной странице
    FIRST_ORDER_BUTTON = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem') and contains(@class, 'mb-6')]") #Кнопка первого заказа в Ленте заказов
    ORDER_DETAILS_FIELD = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]/div[contains(@class, 'Modal_modal__container')]") # Поле с деталями первого заказа
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    ORDER_FEED_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list__OLh59')]//p[contains(@class, 'text_type_digits-default')]")
    ORDER_COMPLETED_TOTAL = (By.XPATH, "//p[contains(@class, 'text_type_digits-large')]")
    ORDER_COMPLETED_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li[contains(@class, 'text_type_digits-default')]")
    CLOSE_ORDER_DETAILS_FIELD = (By.XPATH, '//button[@type="button" and @class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]') # Крестик закрытия деталей оформленного заказа
    ORDER_NUMBER_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq') and contains(@class, 'text_type_digits-large')]")
    ORDER_NUMBER_IN_FEED = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default') and contains(text(), '{}')]")


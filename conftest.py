from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium import webdriver
from urls import MAIN_URL


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(MAIN_URL)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1280, 720)
        driver.get(MAIN_URL)
    yield driver
    driver.quit()

@pytest.fixture
def wait_for_element_located(driver, locator, time, condition):
        return WebDriverWait(driver, time).until(condition(locator))


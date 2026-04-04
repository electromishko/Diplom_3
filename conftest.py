import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from data.urls import Urls
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from utils.user_helpers import create_and_authorize_user, generate_test_user


@pytest.fixture
def main_page(driver):
    """Фикстура главной страницы"""
    return MainPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def forgot_password_page(driver):
    return ForgotPasswordPage(driver)


@pytest.fixture
def user():
    return generate_test_user()


@pytest.fixture
def authorized_user(driver, user):
    return create_and_authorize_user(driver)


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()

    else:
        raise ValueError(f"Browser '{browser_name}' is not supported.")

    driver.get(Urls.BASE_URL)

    yield driver

    driver.quit()

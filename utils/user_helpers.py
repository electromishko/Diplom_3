from utils.user_generator import generate_user
from pages.register_page import RegisterPage
from pages.login_page import LoginPage


def create_and_authorize_user(driver):
    user = generate_user()
    
    register_page = RegisterPage(driver)
    register_page.open()
    register_page.register(user["name"], user["email"], user["password"])
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(user["email"], user["password"])
    
    return user


def generate_test_user():
    return generate_user()

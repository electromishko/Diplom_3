from pages.base_page import BasePage
from locators.register_page_locators import RegisterPageLocators
from data.urls import Urls


class RegisterPage(BasePage):

    def open(self):
        self.click_account_button()
        self.click_register_link()

    def open_via_url(self):
        self.navigate(Urls.REGISTER)
        self.wait_for_element_visible(RegisterPageLocators.NAME_INPUT)

    def click_register_link(self):
        self.click_element(RegisterPageLocators.REGISTER_LINK)
        self.wait_for_element_visible(RegisterPageLocators.NAME_INPUT)

    def register(self, name, email, password):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_register_button()

    def enter_name(self, name):
        self.enter_text(RegisterPageLocators.NAME_INPUT, name)

    def enter_email(self, email):
        self.enter_text(RegisterPageLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.enter_text(RegisterPageLocators.PASSWORD_INPUT, password)

    def click_register_button(self):
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)

    def wait_for_page_load(self, timeout=10):
        self.wait_for_element_visible(RegisterPageLocators.NAME_INPUT, timeout=timeout)

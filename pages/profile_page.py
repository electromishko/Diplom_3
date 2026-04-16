from locators.history_order_page_locators import HistoryOrderPageLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.login_page_locators import LoginPageLocators

from pages.base_page import BasePage


class ProfilePage(BasePage):

    def wait_for_profile_load(self):
        self.wait_for_element_visible(ProfilePageLocators.HISTORY_BUTTON)

    def go_to_order_history(self):
        self.click_element(ProfilePageLocators.HISTORY_BUTTON)

    def is_order_history_opened(self):
        return self.wait_for_element_present(HistoryOrderPageLocators.ORDERS_HISTORY_CONTENT, timeout=5) is not None

    def is_profile_opened(self):
        return self.wait_for_element_visible(ProfilePageLocators.HISTORY_BUTTON, timeout=5) is not None

    def is_login_page_opened(self):
        return self.wait_for_element_visible(LoginPageLocators.EMAIL_INPUT, timeout=5) is not None

    def click_logout(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    def wait_for_page_load(self):
        self.wait_for_element_visible(ProfilePageLocators.HISTORY_BUTTON)


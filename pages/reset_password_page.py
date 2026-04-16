from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage
import allure


class ResetPasswordPage(BasePage):

    @allure.step("Ожидание кнопки 'Сохранить'")
    def wait_save_button(self):
        self.wait_for_element_visible(ResetPasswordPageLocators.SUBMIT_BUTTON)
        self.wait_for_element_clickable(ResetPasswordPageLocators.SUBMIT_BUTTON)

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_password_button(self):
        self.click_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Ожидание подсветки поля ввода нового пароля")
    def wait_password_button_active(self):
        self.wait_for_element_visible(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON_ACTIVE)

    @allure.step("Поиск подсвеченного элемента")
    def find_field_password_active(self):
        return self.find_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON_ACTIVE)

    @allure.step("Проверка, что поле пароля активно")
    def is_password_field_active(self):
        """Проверка, что поле пароля подсвечено"""
        try:
            self.wait_for_element_visible(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON_ACTIVE, timeout=5)
            return True
        except:
            return False

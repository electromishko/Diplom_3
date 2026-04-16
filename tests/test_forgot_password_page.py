import allure


class TestForgotPasswordPage:

    @allure.title("Переход на страницу восстановления пароля со страницы авторизации с проверкой поля ввода почты")
    def test_open_forgot_password_page(self, main_page, login_page, forgot_password_page):
        with allure.step("Открыть страницу логина"):
            login_page.open()
        
        with allure.step("Перейти на страницу восстановления пароля"):
            login_page.go_to_forgot_password()
        
        with allure.step("Проверить, что поле ввода почты видимо"):
            assert forgot_password_page.is_email_input_visible()

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_forgot_password_submit_email(self, forgot_password_page):
        with allure.step("Открыть страницу восстановления пароля"):
            forgot_password_page.open()
        
        with allure.step("Ввести email"):
            forgot_password_page.enter_email("testle@testle.com")
        
        with allure.step("Нажать кнопку восстановления"):
            forgot_password_page.submit()
        
        with allure.step("Проверить, что появилось поле для ввода пароля"):
            assert forgot_password_page.is_password_input_visible()

    @allure.title("Проверка переключателя отображения пароля")
    def test_toggle_password_visibility(self, forgot_password_page):
        with allure.step("Открыть страницу восстановления пароля"):
            forgot_password_page.open()
        
        with allure.step("Ввести email"):
            forgot_password_page.enter_email("testle@testle.com")
        
        with allure.step("Нажать кнопку восстановления"):
            forgot_password_page.submit()
        
        with allure.step("Ввести пароль"):
            forgot_password_page.enter_password("Aa1234567890")
        
        with allure.step("Нажать на переключатель отображения пароля"):
            forgot_password_page.toggle_password_visibility()
        
        with allure.step("Проверить, что пароль виден"):
            assert forgot_password_page.is_password_visible()

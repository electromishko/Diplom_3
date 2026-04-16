import allure


class TestProfilePage:
    @allure.title("Переход в профиль")
    def test_open_profile_page(self, main_page, authorized_user):
        with allure.step("Кликнуть по кнопке аккаунта"):
            main_page.click_account_button()
        
        with allure.step("Создать объект страницы профиля и дождаться загрузки"):
            profile_page = main_page.get_profile_page()
            profile_page.wait_for_profile_load()
        
        with allure.step("Проверить, что страница профиля открыта"):
            assert profile_page.is_profile_opened()

    @allure.title("Переход в историю заказов")
    def test_go_to_order_history(self, main_page, authorized_user):
        with allure.step("Кликнуть по кнопке аккаунта"):
            main_page.click_account_button()
        
        with allure.step("Создать объект страницы профиля и дождаться загрузки"):
            profile_page = main_page.get_profile_page()
            profile_page.wait_for_profile_load()
        
        with allure.step("Перейти в историю заказов"):
            profile_page.go_to_order_history()
        
        with allure.step("Проверить, что страница истории заказов открыта"):
            assert profile_page.is_order_history_opened()

    @allure.title("Выход из аккаунта")
    def test_logout(self, main_page, authorized_user):
        with allure.step("Кликнуть по кнопке аккаунта"):
            main_page.click_account_button()
        
        with allure.step("Создать объект страницы профиля и дождаться загрузки"):
            profile_page = main_page.get_profile_page()
            profile_page.wait_for_profile_load()
        
        with allure.step("Нажать кнопку выхода"):
            profile_page.click_logout()
        
        with allure.step("Проверить, что страница логина открыта"):
            assert profile_page.is_login_page_opened()

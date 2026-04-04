import allure


class TestMakeOrder:

    @allure.title("Заказ авторизованного пользователя")
    def test_make_order_authorized_user(self, main_page, authorized_user):
        with allure.step("Открыть главную страницу для авторизованного пользователя"):
            main_page.open_for_authorized()

        with allure.step("Создать заказ"):
            order_number = main_page.create_order()

        with allure.step("Проверить, что заказ создан (номер не пустой)"):
            assert order_number is not None

    @allure.title("У неавторизованного пользователя отображается кнопка авторизации")
    def test_make_order_unauthorized_user(self, main_page):
        with allure.step("Открыть главную страницу для неавторизованного пользователя"):
            main_page.open_for_unauthorized()

        with allure.step("Добавить булку в заказ"):
            main_page.add_bun()

        with allure.step("Нажать кнопку 'Войти в аккаунт'"):
            main_page.click_create_order_unauthorized()

        with allure.step("Проверить, что открылась страница логина"):
            assert main_page.is_login_page_opened()

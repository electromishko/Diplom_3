import allure


class TestMainPage:

    @allure.title("Переход в профиль по кнопке 'Личный кабинет'")
    def test_open_profile_page(self, main_page, authorized_user):
        with allure.step("Кликнуть по кнопке 'Личный кабинет'"):
            main_page.click_account_button()
        
        with allure.step("Проверить, что открылась страница профиля"):
            assert main_page.is_profile_page_opened()

    @allure.title("Возврат в конструктор по логотипу")
    def test_return_to_constructor_by_logo(self, main_page, authorized_user):
        with allure.step("Кликнуть по кнопке 'Личный кабинет'"):
            main_page.click_account_button()
        
        with allure.step("Кликнуть по логотипу"):
            main_page.click_logo()
        
        with allure.step("Проверить, что открылась страница конструктора"):
            assert main_page.is_constructor_page_opened()

    @allure.title("Возврат в конструктор по кнопке 'Конструктор'")
    def test_return_to_constructor_by_button(self, main_page, authorized_user):
        with allure.step("Кликнуть по кнопке 'Личный кабинет'"):
            main_page.click_account_button()
        
        with allure.step("Кликнуть по кнопке 'Конструктор'"):
            main_page.click_constructor_button()
        
        with allure.step("Проверить, что открылась страница конструктора"):
            assert main_page.is_constructor_page_opened()

    @allure.title("Переключение на раздел 'Булки'")
    def test_switch_to_buns(self, main_page):
        with allure.step("Переключиться на раздел 'Соусы'"):
            main_page.open_tab("SAUCE_TAB")
        
        with allure.step("Переключиться на раздел 'Булки'"):
            main_page.open_tab("BUN_TAB")
        
        with allure.step("Проверить, что раздел 'Булки' активен"):
            assert main_page.is_buns_active(), "Раздел 'Булки' не активен"
    
    @allure.title("Переключение на раздел 'Соусы'")
    def test_switch_to_sauces(self, main_page):
        with allure.step("Переключиться на раздел 'Соусы'"):
            main_page.open_tab("SAUCE_TAB")
        
        with allure.step("Проверить, что раздел 'Соусы' активен"):
            assert main_page.is_sauces_active(), "Раздел 'Соусы' не активен"

    @allure.title("Переключение на раздел 'Начинки'")
    def test_switch_to_fillings(self, main_page):
        with allure.step("Переключиться на раздел 'Начинки'"):
            main_page.open_tab("FILLING_TAB")
        
        with allure.step("Проверить, что раздел 'Начинки' активен"):
            assert main_page.is_fillings_active(), "Раздел 'Начинки' не активен"

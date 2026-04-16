import allure


class TestFeedOrderPage:

    @allure.title("Созданный заказ появляется в работе")
    def test_order_in_work(self, main_page, authorized_user):
        with allure.step("Создать заказ"):
            number_order = main_page.create_order()
        with allure.step("Перейти на страницу ленты заказов"):
            main_page.go_to_feed()
            feed_page = main_page.get_feed_page()
        with allure.step("Проверить, что заказ в работе"):
            assert feed_page.is_order_in_work(number_order, timeout=20)

    @allure.title("Созданный заказ появляется в готовых")
    def test_order_ready(self, main_page, authorized_user):
        with allure.step("Создать заказ"):
            number_order = main_page.create_order()       
        with allure.step("Перейти на страницу ленты заказов"):
            main_page.go_to_feed()
            feed_page = main_page.get_feed_page()
        with allure.step("Проверить, что заказ готов"):
            assert feed_page.is_order_is_ready(number_order, timeout=120)

    @allure.title("Открытие карточки заказа из ленты заказов")
    def test_open_modal_page_order(self, main_page, authorized_user):
        with allure.step("Создать заказ"):
            number = main_page.create_order()
        with allure.step("Перейти на страницу ленты заказов"):
            main_page.go_to_feed()
            feed_page = main_page.get_feed_page()
        with allure.step("Дождаться появления заказа в ленте"):
            feed_page.wait_for_order_in_feed(number, timeout=10)
        with allure.step("Открыть карточку заказа"):
            feed_page.open_order_by_number(number)
        with allure.step("Проверить, что модальное окно открылось"):
            feed_page.is_modal_opened()
        with allure.step("Получить номер заказа из модального окна и сравнить"):
            modal_number = feed_page.get_modal_order_number()
            assert modal_number == number

    @allure.title("Увеличение счётчика заказов за день")
    def test_counter_today_incremented(self, main_page, authorized_user):
        with allure.step("Создать первый заказ"):
            main_page.create_order()
        with allure.step("Перейти на страницу ленты заказов"):
            main_page.go_to_feed()
            feed_page = main_page.get_feed_page()
        with allure.step("Получить текущее значение счётчика за день"):
            before = feed_page.get_today_counter()
        with allure.step("Нажать на логотип и вернуться на главную"):
            main_page.click_logo()
        with allure.step("Создать второй заказ"):
            main_page.create_order()
        with allure.step("Перейти на страницу ленты заказов"):
            main_page.go_to_feed()
            feed_page = main_page.get_feed_page()
        with allure.step("Дождаться увеличения счётчика за день"):
            feed_page.wait_today_increase(before)
        with allure.step("Проверить, что счётчик увеличился"):
            assert feed_page.get_today_counter() >= before + 1

    @allure.title("Увеличение счётчика заказов за всё время")
    def test_counter_total_incremented(self, main_page, authorized_user):
        with allure.step("Создать первый заказ"):
            main_page.create_order()
        with allure.step("Перейти на страницу ленты заказов"):
            main_page.go_to_feed()
            feed_page = main_page.get_feed_page()
        with allure.step("Получить текущее значение общего счётчика"):
            before = feed_page.get_orders_total()
        with allure.step("Нажать на логотип и вернуться на главную"):
            main_page.click_logo()
        with allure.step("Создать второй заказ"):
            main_page.create_order()
        with allure.step("Перейти на страницу ленты заказов"):
            main_page.go_to_feed()
            feed_page = main_page.get_feed_page()
        with allure.step("Дождаться увеличения общего счётчика"):
            feed_page.wait_total_increase(before)
        with allure.step("Проверить, что общий счётчик увеличился"):
            assert feed_page.get_orders_total() >= before + 1

    @allure.title("Заказ из истории отображается в ленте")
    def test_show_order_user_in_feed_page(self, main_page, authorized_user):
        with allure.step("Создать заказ"):
            main_page.create_order()
        with allure.step("Перейти в профиль"):
            main_page.go_to_profile()
            profile_page = main_page.get_profile_page()
            profile_page.wait_for_profile_load()
        with allure.step("Перейти в историю заказов"):
            profile_page.go_to_order_history()
            history_page = main_page.get_history_order_page()
            history_page.wait_for_page_load()
        with allure.step("Получить номер последнего заказа из истории"):
            number_history = history_page.get_last_order_number()
        with allure.step("Нажать на логотип и вернуться на главную"):
            main_page.click_logo()
        with allure.step("Перейти на страницу ленты заказов"):
            feed_page = main_page.go_to_feed()
        with allure.step("Проверить, что заказ отображается в ленте"):
            assert feed_page.wait_for_order_in_feed(number_history, timeout=10)

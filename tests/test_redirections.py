import allure
from page_objects.home_page import HomePage


@allure.feature('Редиректы через ссылки в хедере')
class TestRedirections:

    @allure.description('Ссылка "Самокат" открывает главную страницу сервиса')
    def test_redirect_to_main_page_by_header_link(self, driver):
        with allure.step('Сначала открываем форму заказа, затем жмем на Самокат и возвращаемся на главную страницу'):
            page = HomePage(driver)
            page.click_order_btn_in_header()
            home_url = page.click_scooter_logo()
            assert home_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.description('Ссылка "Яндекс" открывает в новом окне Яндекс.Дзен')
    def test_redirect_to_dzen_by_header_link(self, driver):
        with allure.step('Нажимаем Яндекс и переходим в новое окно на страницу Дзена'):
            page = HomePage(driver)
            dzen_url = page.go_to_yandex_from_logo()
            assert "dzen.ru" in dzen_url

import pytest
import allure
from page_objects.scooter_order import OrderPage
from page_objects.accept_cookie import CookieHandler
from page_objects.logo_links import ClickLink
from order_dataset import order_data


@allure.title('Заказ самоката')
class TestScooterOrder:

    @allure.description('Заказ самоката через кнопку в хедере с заполнением формы рандомными данными '
                        'из файла order_dataset, проверкой получения сообщения: "Заказ оформлен" '
                        'и возвратом на главную страницу Самоката')
    @pytest.mark.parametrize("name, surname, address, phone, color, comment", [order_data()])
    def test_order_through_top_button_return_to_main_page(self, driver, name, surname, address, phone, color, comment):
        with allure.step('Принимаем куки'):
            cookie = CookieHandler(driver)
            cookie.accept_cookies()
        with allure.step('Нажимаем на кнопку Заказать в хедере'):
            page = OrderPage(driver)
            page.click_order_button_top()
        with allure.step('Заполняем форму заказа'):
            page.make_order_step_1(name, surname, address, phone)
            page.make_order_step_2(color, comment)
        with allure.step('Проверяем сообщение об оформлении заказа'):
            assert "Заказ оформлен" in page.get_order_confirmation()
        with allure.step('Переходим на главную страницу Самоката'):
            page.go_to_order_status()
            link_scooter = ClickLink(driver)
            link_scooter.return_to_main_from_logo()
            assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.description('Заказ самоката на главной странице через кнопку под описанием с заполнением формы '
                        'рандомными данными из файла order_dataset, проверкой получения сообщения: "Заказ оформлен" '
                        'и переходом на страницу Дзена по клику на логотип в хедере')
    @pytest.mark.parametrize("name, surname, address, phone, color, comment", [order_data()])
    def test_order_through_big_button_redirect_to_dzen(self, driver, name, surname, address, phone, color, comment):
        with allure.step('Принимаем куки'):
            cookie = CookieHandler(driver)
            cookie.accept_cookies()
        with allure.step('Нажимаем на большую кнопку Заказать под описанием'):
            page = OrderPage(driver)
            page.click_order_button_big()
        with allure.step('Заполняем форму заказа'):
            page.make_order_step_1(name, surname, address, phone)
            page.make_order_step_2(color, comment)
        with allure.step('Проверяем сообщение об оформлении заказа'):
            assert "Заказ оформлен" in page.get_order_confirmation()
        with allure.step('Переходим на страницу Дзена'):
            page.go_to_order_status()
            link_dzen = ClickLink(driver)
            link_dzen.go_to_yandex_from_logo()
            assert "dzen.ru" in driver.current_url

import pytest
import allure
from page_objects.order_page import OrderPage
from page_objects.home_page import HomePage
from order_dataset import order_data


@allure.feature('Заказ самоката')
class TestScooterOrder:

    @allure.description('Заказ самоката через кнопку в хедере с заполнением формы рандомными данными '
                        'из файла order_dataset, проверкой получения сообщения: "Заказ оформлен"')
    @pytest.mark.parametrize("name, surname, address, phone, color, comment", [order_data()])
    def test_order_through_top_button_return_to_main_page(self, driver, name, surname, address, phone, color, comment):
        with allure.step('Принимаем куки'):
            home = HomePage(driver)
            home.accept_cookies()
        with allure.step('Нажимаем на кнопку Заказать в хедере'):
            home.click_order_btn_in_header()
        with allure.step('Заполняем форму заказа'):
            order = OrderPage(driver)
            order.make_order_step_1(name, surname, address, phone)
            order.make_order_step_2(color, comment)
        with allure.step('Проверяем сообщение об оформлении заказа'):
            assert "Заказ оформлен" in order.get_order_confirmation()


    @allure.description('Заказ самоката на главной странице через кнопку под описанием с заполнением формы '
                        'рандомными данными из файла order_dataset, проверкой получения сообщения: "Заказ оформлен"')
    @pytest.mark.parametrize("name, surname, address, phone, color, comment", [order_data()])
    def test_order_through_big_button_redirect_to_dzen(self, driver, name, surname, address, phone, color, comment):
        with allure.step('Принимаем куки'):
            home = HomePage(driver)
            home.accept_cookies()
        with allure.step('Нажимаем на большую кнопку Заказать под описанием'):
            home.click_order_btn_under_description()
        with allure.step('Заполняем форму заказа'):
            order = OrderPage(driver)
            order.make_order_step_1(name, surname, address, phone)
            order.make_order_step_2(color, comment)
        with allure.step('Проверяем сообщение об оформлении заказа'):
            assert "Заказ оформлен" in order.get_order_confirmation()

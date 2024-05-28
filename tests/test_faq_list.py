import pytest
import allure
from page_objects.faq_list import FAQPage
from page_objects.accept_cookie import CookieHandler


@allure.title('Проверка наличия ответов на важные вопросы')
class TestFAQ:

    @allure.description('Скроллим главную страницу до конца вниз, нажимаем на каждый вопрос, тесты проходят по циклу '
                        'на каждый вопрос - отдельный тест, при наличии ответа атрибут вопроса '
                        '"aria-expanded" меняется на "true"')
    @pytest.mark.parametrize("index", list(range(8)))
    def test_faq_questions(self, driver, index):
        with allure.step('Принимаем куки'):
            cookie = CookieHandler(driver)
            cookie.accept_cookies()
        with allure.step(f'Нажимаем на вопрос № {index} и проверяем изменение атрибута "aria-expanded"'):
            page = FAQPage(driver)
            assert page.toggle_faq_question(index) == True

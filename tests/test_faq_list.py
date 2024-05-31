import pytest
import allure
from page_objects.home_page import HomePage
from answers_data import expected_answers


@allure.feature('Проверка ответов на важные вопросы')
class TestFAQ:

    @allure.title('Скроллим главную страницу до конца вниз, нажимаем поочередно на каждый вопрос'
                        'и проверяем наличие нужного ответа')
    @pytest.mark.parametrize("index", list(range(8)))
    def test_faq_questions(self, driver, index):
        with allure.step('Принимаем куки'):
            home = HomePage(driver)
            home.accept_cookies()
        with allure.step(f'Нажимаем на вопрос № {index} и проверяем текст ответа'):
            actual_answer = home.toggle_faq_question(index)
            expected_answer = expected_answers[index]
            assert actual_answer == expected_answer, f"Ожидали ответ: {expected_answer}, но получили: {actual_answer}"

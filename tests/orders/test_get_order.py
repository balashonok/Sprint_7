import allure

from methods.order_methods import OrderMethods
from data import TRACK, WRONG_TRACK

class TestGetOrder:

    @allure.title('Проверка запроса существующего заказа, ответ содержит объект с заказом')
    def test_get_order(self):
        order = OrderMethods
        status_code, response_context = order.get_order(self, TRACK)
        assert status_code == 200 and 'id' in response_context['order'].keys()

    @allure.title('Проверка запроса без номера заказа, проверка текста ошибки')
    def test_get_order_no_track(self):
        order = OrderMethods
        status_code, response_context = order.get_order(self, '')
        assert status_code == 400 and response_context['message'] == 'Недостаточно данных для поиска'

    @allure.title('Проверка запроса с несуществующим номером заказа, проверка текста ошибки')
    def test_get_order_wrong_track(self):
        order = OrderMethods
        status_code, response_context = order.get_order(self, WRONG_TRACK)
        assert status_code == 404 and response_context['message'] == 'Заказ не найден'

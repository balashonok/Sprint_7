import allure

from methods.order_methods import OrderMethods
from data import TRACK, WRONG_TRACK
from errors import OrderErrors

class TestGetOrder:

    @allure.title('Проверка запроса существующего заказа, ответ содержит объект с заказом')
    def test_get_order(self):
        order = OrderMethods
        status_code, response_context = order.get_order(TRACK)
        assert status_code == 200 and 'id' in response_context['order'].keys()

    @allure.title('Проверка запроса без номера заказа, проверка текста ошибки')
    def test_get_order_no_track(self):
        order = OrderMethods
        status_code, response_context = order.get_order('')
        assert status_code == 400 and response_context['message'] == OrderErrors.REQUIRED_FIELDS_MISSING

    @allure.title('Проверка запроса с несуществующим номером заказа, проверка текста ошибки')
    def test_get_order_wrong_track(self):
        order = OrderMethods
        status_code, response_context = order.get_order(WRONG_TRACK)
        assert status_code == 404 and response_context['message'] == OrderErrors.ORDER_NOT_FOUND

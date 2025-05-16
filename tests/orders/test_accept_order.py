import allure

from methods.order_methods import OrderMethods
from data import TRACK, COLORS, COURIER_ID, WRONG_ORDER_ID, WRONG_COURIER_ID

class TestAcceptOrder:

    @allure.title('Проверка подтверждения заказа')
    def test_accept_order(self):
        order = OrderMethods
        _, create_response = order.create_order(self, COLORS[0])
        status_code, response_context = order.accept_order_by_track(self, create_response['track'], COURIER_ID)
        assert status_code == 200 and response_context == {'ok': True}

    @allure.title('Проверка подтверждения заказа, не передан id курьера, запрос возвращает ошибку')
    def test_accept_order_no_courier_id(self):
        order = OrderMethods
        status_code, response_context = order.accept_order_by_track(self, TRACK, '')
        assert status_code == 400 and response_context['message'] == 'Недостаточно данных для поиска'

    @allure.title('Проверка подтверждения заказа, передан неверный id курьера, запрос возвращает ошибку')
    def test_accept_order_wrong_courier_id(self):
        order = OrderMethods
        status_code, response_context = order.accept_order_by_track(self, TRACK, WRONG_COURIER_ID)
        assert status_code == 404 and response_context['message'] == 'Курьера с таким id не существует'

    @allure.title('Проверка подтверждения заказа, не передан id заказа')
    def test_accept_order_no_order_id(self):
        order = OrderMethods
        status_code, response_context = order.accept_order(self, '', COURIER_ID)
        assert status_code == 404 and response_context['message'] == 'Not Found.'

    @allure.title('Проверка подтверждения заказа, передан неверный id заказа')
    def test_accept_order_wrong_order_id(self):
        order = OrderMethods
        status_code, response_context = order.accept_order(self, WRONG_ORDER_ID, COURIER_ID)
        assert status_code == 404 and response_context['message'] == 'Заказа с таким id не существует'

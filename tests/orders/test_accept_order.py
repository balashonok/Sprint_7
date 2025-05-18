import allure

from methods.order_methods import OrderMethods
from data import TRACK, COLORS, COURIER_ID, WRONG_ORDER_ID, WRONG_COURIER_ID
from errors import OrderErrors

class TestAcceptOrder:

    @allure.title('Проверка подтверждения заказа')
    def test_accept_order(self):
        order = OrderMethods
        _, create_response = order.create_order(COLORS[0])
        status_code, response_context = order.accept_order_by_track(create_response['track'], COURIER_ID)
        assert status_code == 200 and response_context == {'ok': True}

    @allure.title('Проверка подтверждения заказа, не передан id курьера, запрос возвращает ошибку')
    def test_accept_order_no_courier_id(self):
        order = OrderMethods
        status_code, response_context = order.accept_order_by_track(TRACK, '')
        assert status_code == 400 and response_context['message'] == OrderErrors.REQUIRED_FIELDS_MISSING

    @allure.title('Проверка подтверждения заказа, передан неверный id курьера, запрос возвращает ошибку')
    def test_accept_order_wrong_courier_id(self):
        order = OrderMethods
        status_code, response_context = order.accept_order_by_track(TRACK, WRONG_COURIER_ID)
        assert status_code == 404 and response_context['message'] == OrderErrors.COURIER_NOT_FOUND

    @allure.title('Проверка подтверждения заказа, не передан id заказа')
    def test_accept_order_no_order_id(self):
        order = OrderMethods
        status_code, response_context = order.accept_order('', COURIER_ID)
        assert status_code == 404 and response_context['message'] == 'Not Found.'

    @allure.title('Проверка подтверждения заказа, передан неверный id заказа')
    def test_accept_order_wrong_order_id(self):
        order = OrderMethods
        status_code, response_context = order.accept_order(WRONG_ORDER_ID, COURIER_ID)
        assert status_code == 404 and response_context['message'] == OrderErrors.INVALID_ORDER_ID

import pytest
import allure

from methods.order_methods import OrderMethods
from data import COLORS

class TestCreateOrder:

    @allure.title('Проверка создания заказа с разными цветами самоката')
    @pytest.mark.parametrize('color', COLORS)
    def test_create_order(self, color):
        order = OrderMethods
        status_code, response_context = order.create_order(self, color)
        assert status_code == 201

    @allure.title('Проверка полученного ответа при создании заказа с разными цветами самоката')
    @pytest.mark.parametrize('color', COLORS)
    def test_create_order_check_response(self, color):
        order = OrderMethods
        status_code, response_context = order.create_order(self, color)
        assert status_code == 201 and "track" in response_context.keys(), f'Status is {status_code} == 201, context is {response_context}'

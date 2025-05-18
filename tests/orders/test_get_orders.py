import allure

from methods.order_methods import OrderMethods

class TestGetOrders:

    @allure.title('Проверка получения списка заказов')
    def test_get_orders(self):
        orders = OrderMethods
        status_code, response_context = orders.get_list_of_orders()
        assert status_code == 200 and 'id' in response_context['orders'][0].keys()
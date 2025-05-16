import allure

from methods.courier_methods import CourierMethods
from conftests import courier

from data import WRONG_COURIER_ID

class TestDeleteCourier:

    @allure.title("Проверка удаления курьера, успешный запрос возвращает {'ok': True}")
    def test_delete_courier(self, courier):
        courier_client = CourierMethods
        status_code, response_context = courier_client.delete_courier(self, courier)
        assert status_code == 200 and response_context == {'ok': True}

    @allure.title("Проверка удаления курьера, в запрос не передан id курьера")
    def test_delete_courier_no_id(self, courier):
        courier_client = CourierMethods
        status_code, response_context = courier_client.delete_courier(self, '')
        assert status_code == 404 and response_context == {'code': 404, 'message': 'Not Found.'}

    @allure.title("Проверка удаления курьера, в запрос передан несуществующий id курьера")
    def test_delete_courier_wrong_id(self, courier):
        courier_client = CourierMethods
        status_code, response_context = courier_client.delete_courier(self, WRONG_COURIER_ID)
        assert status_code == 404 and response_context == {'code': 404, 'message': 'Курьера с таким id нет.'}

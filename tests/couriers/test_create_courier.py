import pytest
import allure

from methods.courier_methods import CourierMethods

class TestCreateCourier:

    @allure.title('Проверка возможности создания курьера, в случае успеха получен статус 201')
    def test_create_courier(self):
        courier = CourierMethods
        status_code, response_context = courier.create_courier(self)
        assert status_code == 201, f'Status is {status_code} == 201, context is {response_context}'

    @allure.title('Проверка полученного результата в случае успешного создания курьера')
    def test_create_courier_message(self):
        courier = CourierMethods
        status_code, response_context = courier.create_courier(self)
        assert status_code == 201 and response_context == {
            'ok': True}, f'Status is {status_code} == 201, context is {response_context}'

    @allure.title('Проверка получения ошибки создания курьера в случае если не передано одно из обязательных полей')
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field(self, missing_field):
        courier = CourierMethods
        status_code, response_context = courier.create_courier_missing_field(self, missing_field)
        assert status_code == 400 and response_context['message'] == 'Недостаточно данных для создания учетной записи', f'Status is {status_code} == 400, context is {response_context}'

    @allure.title('Проверка недоступности создания курьера с тем же логином')
    def test_create_same_courier_error(self):
        courier = CourierMethods
        status_code, response_context = courier.create_same_courier(self)
        assert status_code == 409, f'Status is {status_code} == 409, context is {response_context}'

    @allure.title('Проверка текста ошибки при попытке создания курьера с уже существующим логином')
    def test_create_same_courier_error_message(self):
        courier = CourierMethods
        status_code, response_context = courier.create_same_courier(self)
        assert status_code == 409 and response_context['message'] == 'Этот логин уже используется. Попробуйте другой.', f'Status is {status_code} == 409, context is {response_context}'

import pytest
import allure

from methods.courier_methods import CourierMethods
from errors import CourierErrors

class TestLoginCourier:

    @allure.title('Проверка успешной авторизации курьера')
    def test_login_courier(self):
        courier = CourierMethods
        status_code, response_context = courier.login_courier()
        assert status_code == 200, f'Status is {status_code} == 200, context is {response_context}'

    @allure.title('Проверка что при успешной авторизации курьера в ответе содержится id')
    def test_login_courier_check_message(self):
        courier = CourierMethods
        status_code, response_context = courier.login_courier()
        assert status_code == 200 and "id" in response_context.keys(), f'Status is {status_code} == 200, context is {response_context}'

    @allure.title('Проверка получения ошибки авторизации курьера в случае если не передан логин')
    @pytest.mark.parametrize("missing_field", ["login"])
    def test_login_courier_missing_required_field(self, missing_field):
        courier = CourierMethods
        status_code, response_context = courier.login_courier_missing_field(missing_field)
        assert status_code == 400 and response_context['message'] == CourierErrors.LOGIN_REQUIRED_FIELDS_MISSING, f'Status is {status_code} == 400, context is {response_context}'

    @allure.title('Проверка получения ошибки авторизации курьера в случае если в одном из полей ошибка')
    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_login_courier_wrong_field(self, wrong_field):
        courier = CourierMethods
        status_code, response_context = courier.login_courier_wrong_field(wrong_field)
        assert status_code == 404 and response_context[
            'message'] == CourierErrors.ACCOUNT_NOT_FOUND, f'Status is {status_code} == 404, context is {response_context}'

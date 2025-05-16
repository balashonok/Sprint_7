import pytest

from methods.courier_methods import CourierMethods

@pytest.fixture()
def courier():
    courier_client = CourierMethods()
    courier_client.create_courier()
    login_response = courier_client.login_new_courier()[1]
    courier_id = login_response["id"]
    yield courier_id
    courier_client.delete_courier(courier_id)

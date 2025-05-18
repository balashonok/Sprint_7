import requests

from data import BASE_URL, COURIERS_URL, COURIER_DATA
from data_generator import generate_courier_data

class CourierMethods:
    @staticmethod
    def create_courier():
        payload = generate_courier_data()
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        return response.status_code, response.json()

    @staticmethod
    def create_courier_missing_field(missing_field):
        payload = generate_courier_data().pop(missing_field)
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        return response.status_code, response.json()

    @staticmethod
    def create_same_courier():
        payload = generate_courier_data()
        requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        return response.status_code, response.json()

    @staticmethod
    def login_courier():
        payload = COURIER_DATA
        response = requests.post(f'{BASE_URL}{COURIERS_URL}/login', data=payload)
        return response.status_code, response.json()

    @staticmethod
    def login_new_courier():
        payload = generate_courier_data()
        requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        payload.pop("firstName")
        response = requests.post(f'{BASE_URL}{COURIERS_URL}/login', data=payload)
        return response.status_code, response.json()

    @staticmethod
    def login_courier_missing_field(missing_field):
        payload = COURIER_DATA
        payload.pop(missing_field)
        response = requests.post(f'{BASE_URL}{COURIERS_URL}/login', json=payload)
        return response.status_code, response.json()

    @staticmethod
    def login_courier_wrong_field(wrong_field):
        payload = COURIER_DATA
        payload[wrong_field] = "wrongstring"
        response = requests.post(f'{BASE_URL}{COURIERS_URL}/login', json=payload)
        return response.status_code, response.json()

    @staticmethod
    def delete_courier(courier_id):
        response = requests.delete(f'{BASE_URL}{COURIERS_URL}/{courier_id}')
        return response.status_code, response.json()


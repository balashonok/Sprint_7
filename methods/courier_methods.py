import requests

from data import BASE_URL, COURIERS_URL, COURIER_DATA
from data_generator import generate_courier_data

class CourierMethods:
    def create_courier(self):
        payload = generate_courier_data()
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        return response.status_code, response.json()

    def create_courier_missing_field(self, missing_field):
        payload = generate_courier_data().pop(missing_field)
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        return response.status_code, response.json()

    def create_same_courier(self):
        payload = generate_courier_data()
        requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        return response.status_code, response.json()

    def login_courier(self):
        payload = COURIER_DATA
        response = requests.post(f'{BASE_URL}{COURIERS_URL}/login', data=payload)
        return response.status_code, response.json()

    def login_new_courier(self):
        payload = generate_courier_data()
        requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        payload.pop("firstName")
        response = requests.post(f'{BASE_URL}{COURIERS_URL}/login', data=payload)
        return response.status_code, response.json()

    def login_courier_missing_field(self, missing_field):
        payload = COURIER_DATA
        payload.pop(missing_field)
        response = requests.post(f'{BASE_URL}{COURIERS_URL}/login', json=payload)
        return response.status_code, response.json()

    def login_courier_wrong_field(self, wrong_field):
        payload = COURIER_DATA
        payload[wrong_field] = "wrongstring"
        response = requests.post(f'{BASE_URL}{COURIERS_URL}/login', json=payload)
        return response.status_code, response.json()

    def delete_courier(self, courier_id):
        response = requests.delete(f'{BASE_URL}{COURIERS_URL}/{courier_id}')
        return response.status_code, response.json()


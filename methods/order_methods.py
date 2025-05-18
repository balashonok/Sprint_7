import requests

from data import BASE_URL, ORDERS_URL, ORDER_DATA, TRACK_URL, ACCEPT_URL, COURIER_ID

class OrderMethods:
    @staticmethod
    def create_order(color):
        payload = ORDER_DATA
        payload['color'] = color
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=payload)
        return response.status_code, response.json()

    @staticmethod
    def get_list_of_orders():
        response = requests.get(f'{BASE_URL}{ORDERS_URL}')
        return response.status_code, response.json()

    @staticmethod
    def get_order(track):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}{TRACK_URL}{track}')
        return response.status_code, response.json()

    @staticmethod
    def accept_order(order_id, courier_id):
        response = requests.put(f'{BASE_URL}{ORDERS_URL}{ACCEPT_URL}{order_id}?courierId={courier_id}')
        return response.status_code, response.json()

    @staticmethod
    def accept_order_by_track(track, courier_id):
        status_code, response = OrderMethods.get_order(track)
        order_id = response['order']['id']
        return OrderMethods.accept_order(order_id, courier_id)

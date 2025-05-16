import requests

from data import BASE_URL, ORDERS_URL, ORDER_DATA, TRACK_URL, ACCEPT_URL, COURIER_ID

class OrderMethods:
    def create_order(self, color):
        payload = ORDER_DATA
        payload['color'] = color
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=payload)
        return response.status_code, response.json()

    def get_list_of_orders(self):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}')
        return response.status_code, response.json()

    def get_order(self, track):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}{TRACK_URL}{track}')
        return response.status_code, response.json()

    def accept_order(self, order_id, courier_id):
        response = requests.put(f'{BASE_URL}{ORDERS_URL}{ACCEPT_URL}{order_id}?courierId={courier_id}')
        return response.status_code, response.json()

    def accept_order_by_track(self, track, courier_id):
        status_code, response = OrderMethods.get_order(self, track)
        order_id = response['order']['id']
        return OrderMethods.accept_order(self, order_id, courier_id)




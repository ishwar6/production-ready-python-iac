import requests
import json

BASE_URL = "https://socialpaidpromotion.com/api/v2"
API_KEY = "88f07c5eb8193529b041be49066fc2e8"


def add_order(service_id, url, quantity, comments=None, runs=None, interval=None):
    payload = {
        "key": API_KEY,
        "action": "add",
        "service": service_id,
        "url": url,
        "quantity": quantity,
    }
    if comments:
        payload["comments"] = comments
    if runs:
        payload["runs"] = runs
    if interval:
        payload["interval"] = interval

    response = requests.post(BASE_URL, data=payload)
    return response.json()


def get_services_list():
    payload = {
        "key": API_KEY,
        "action": "services"
    }
    response = requests.post(BASE_URL, data=payload)
    return response.json()


def get_order_status(order_id):
    print("calling")
    payload = {
        "key": API_KEY,
        "action": "status",
        "order": int(order_id)
    }
    response = requests.post(BASE_URL, data=payload)
    print(response.text)
    return response.text
    return response.json()


def get_multiple_order_status(order_ids):
    # Convert list of order IDs to comma-separated string
    order_ids_str = ",".join(map(str, order_ids))

    payload = {
        "key": API_KEY,
        "action": "status",
        "orders": order_ids_str
    }
    response = requests.post(BASE_URL, data=payload)
    return response.json()


def get_balance():
    payload = {
        "key": API_KEY,
        "action": "balance"
    }
    response = requests.post(BASE_URL, data=payload)
    return response.json()


def refill_order(order_id):
    payload = {
        "key": API_KEY,
        "action": "refill",
        "order": order_id
    }
    response = requests.post(BASE_URL, data=payload)
    return response.json()


def cancel_order(order_id):
    payload = {
        "key": API_KEY,
        "action": "cancel",
        "order": order_id
    }
    response = requests.post(BASE_URL, data=payload)
    return response.json()


# Example usage:
# services = get_services_list()
# print(services)
status = get_order_status(34410)
order_response = add_order(service_id=1, url="https://example.com", quantity=100)
print(order_response)

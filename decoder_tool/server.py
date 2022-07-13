import requests


class Server:
    def check_payment(self):
        result = requests.get("url which checks client credentials")
        subscription_state = result.json()
        return subscription_state["status"] == "OK"

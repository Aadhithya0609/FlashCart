
from locust import HttpUser, task, between


class FlashCartUser(HttpUser):
    wait_time = between(0,0)

    @task
    def get_products(self):
        self.client.get(
            "/api/products",
            name="/api/products"
        )

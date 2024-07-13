rom locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Time between requests in seconds
    host = "https://5b793895494047.lhr.life/"  # Specify your base host URL

    @task
    def my_task(self):
        self.client.get("/")  # Adjust the endpoint path as needed

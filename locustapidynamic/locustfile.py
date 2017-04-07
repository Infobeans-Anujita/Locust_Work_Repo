from locust import HttpLocust, TaskSet, task


class MyClass(TaskSet):
    def on_start(self):
        print "hello anu"

    @task(1)
    def get_value(self):
        self.client.get("/")

    @task(2)
    def get_all(self):
        self.client.get("/users")

    @task(1)
    def get_one(self):
        # self.client.get("/users/id")
        for i in range(30):
            self.client.get("/users?id=%i" % i, name="/users?id=[id]")


class UserBehaviour(HttpLocust):
    task_set = MyClass
    min_wait = 5000
    max_wait = 10000

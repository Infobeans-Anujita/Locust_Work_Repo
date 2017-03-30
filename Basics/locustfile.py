from locust import HttpLocust, TaskSet, task


class MyLocustClass(TaskSet):
    @task(1)
    def on_start(self):
        headers = {"Referrer":"http://demo6865624.mockable.io"}
        res = self.client.post("http://demo6865624.mockable.io", {"msg":"Hello World"}, headers=headers)
        print (res.text)

    @task(2)
    def get_url(self):
        headers = {"Referrer": "http://demo6865624.mockable.io"}
        res = self.client.get("http://demo6865624.mockable.io", headers=headers)
        print (res.text)

    @task(2)
    def del_url(self):
        headers = {"Referrer": "http://demo6865624.mockable.io"}
        res = self.client.delete("http://demo6865624.mockable.io", headers=headers)
        print (res.text)


class UserBehaviour(HttpLocust):
    task_set = MyLocustClass
    min_wait = 5000
    max_wait = 10000


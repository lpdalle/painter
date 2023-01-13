import httpx

from painter.clients.schema import Task


class TaskClient:
    def __init__(self, url) -> None:
        self.url = url

    def acquire(self):
        url = f'{self.url}/api/v1/generation/acquire'
        response = httpx.post(url)
        if not response.json():
            return None
        task = Task(**response.json())
        return task.uid

    def complete(self, uid: int):
        url = f'{self.url}/api/v1/generation/{uid}/complete'
        httpx.post(url)

import httpx

from painter.clients.schema import Task


class TaskClient:
    def __init__(self, url: str) -> None:
        self.url = url

    def acquire(self) -> Task | None:
        url = f'{self.url}/api/v1/generation/acquire'
        response = httpx.post(url)
        if not response.json():
            return None
        return Task(**response.json())

    def complete(self, uid: int) -> None:
        url = f'{self.url}/api/v1/generation/{uid}/complete'
        httpx.post(url)

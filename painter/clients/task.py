import httpx


class TaskClient:
    def __init__(self, url) -> None:
        self.url = url

    def acquire(self):
        url = f'{self.url}/api/v1/generation/acquire'
        headers = {'Contet-Type': 'application/json'}
        response = httpx.post(url, headers=headers)
        if not response.json():
            return 0
        return response.json()['uid']

    def complete(self, uid: int):
        url = f'{self.url}/api/v1/generation/{uid}/complete'
        httpx.post(url)

import httpx


class TaskClient:
    def __init__(self, url) -> None:
        self.url = url

    def acquire(self):
        url = f'{self.url}/api/v1/generation/acquire'
        headers = {'Contet-Type': 'application/json'}
        response = httpx.put(url, headers=headers)
        if response.status_code == 422:  # noqa: WPS432
            return 0
        return response.json()['uid']

    def complete(self, uid: int):
        url = f'{self.url}/api/v1/generation/{uid}/complete'
        httpx.put(url)

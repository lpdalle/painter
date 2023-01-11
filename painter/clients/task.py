import httpx


class TaskClient:
    def __init__(self, url) -> None:
        self.url = url

    def acquire(self):
        url = f'{self.url}/api/v1/generation/acquire'
        headers = {'Contet-Type': 'application/json'}
        response = httpx.put(url, headers=headers)
        response.raise_for_status()

    def complete(self, uid: int):
        url = f'{self.url}/api/v1/generation/{uid}/complete'
        response = httpx.put(url)
        if response.status_code == 404:  # noqa: WPS432
            return None
        return response.json()

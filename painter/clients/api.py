from painter.clients.task import TaskClient

base_url = 'http://127.0.0.1:5000'


class ApiClients:
    def __init__(self, url: str) -> None:
        self.task = TaskClient(url)


api = ApiClients(base_url)

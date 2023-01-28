from painter.clients.task import TaskClient
from painter.config import conf


class ApiClients:
    def __init__(self, url: str) -> None:
        self.task = TaskClient(url)


api = ApiClients(conf.backend_url)

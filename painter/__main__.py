import logging
import time

from painter.clients.api import api

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)


def main():
    api.task.acquire()
    time.sleep(5)
    api.task.complete(uid=1)


if __name__ == '__main__':
    main()

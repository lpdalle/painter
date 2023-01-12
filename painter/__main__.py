import logging
import time

from painter.clients.api import api

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)


def main():

    while True:
        time.sleep(3)

        gen_uid = api.task.acquire()
        if not gen_uid:
            logger.info('All tasks done!')
            return
        time.sleep(5)
        api.task.complete(uid=gen_uid)


if __name__ == '__main__':
    main()

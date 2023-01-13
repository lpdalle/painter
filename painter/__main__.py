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

        task = api.task.acquire()
        if not task:
            logger.info('All tasks done!')
            return
        time.sleep(5)
        api.task.complete(uid=task.uid)
        logger.info(f'Task [{task.prompt}] done!')


if __name__ == '__main__':
    main()

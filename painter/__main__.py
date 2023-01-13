import logging
import time

from painter.clients.api import api

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)


def main():
    sleep_interval = 3
    while True:
        task = api.task.acquire()
        time.sleep(sleep_interval)

        if not task:
            logger.info('All tasks done!')
            return
        time.sleep(sleep_interval)
        api.task.complete(uid=task.uid)
        logger.info(f'Task [{task.prompt}] done!')


if __name__ == '__main__':
    main()

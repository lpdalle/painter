import logging
from time import sleep

from painter.clients.api import api
from painter.clients.generation import start
from painter.server import upload

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)


def main():
    sleep_time = 5
    is_working = True
    while is_working:
        task = api.task.acquire()

        if not task:
            logger.info('No new task found')
            sleep(sleep_time)
            continue

        logger.info(f'Task [{task.prompt}] has started')
        start(text=task.prompt)
        upload(task.uid)
        api.task.complete(uid=task.uid)
        logger.info(f'Task [{task.prompt}] done!')


if __name__ == '__main__':
    main()

import logging

import httpx

from painter.config import UPLOAD_FOLDER


def upload(uid: int):
    with open(f'{UPLOAD_FOLDER}/img_0.png', 'rb') as file:
        image = file.read()
        logging.info('Sending file: {0}'.format(file))
        header = {'Content-Type': 'image/png'}
        response = httpx.post(
            f'http://127.0.0.1:5000/api/v1/generation/{uid}/images/',
            data=image,
            headers=header,
        )
        response.raise_for_status()
        if response.status_code == 404:  # noqa: WPS432
            return logging.info('Error uploading file!')

        return logging.info('File uploaded!')


if __name__ == '__main__':
    upload(5)

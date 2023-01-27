import logging
from pathlib import Path

import httpx

from painter.config import conf


def upload(uid: int):
    logging.info('Sending file')
    file_path = Path(f'{conf.upload_folder}/img_0.png')
    with open(file_path, 'rb') as fs:
        files = {'file': fs}
        response = httpx.post(
            f'{conf.backend_url}/v1/generations/{uid}/images/',
            files=files,
            timeout=10,
        )
        response.raise_for_status()
        file_path.unlink()
        return logging.info('File uploaded!')

import os
from dataclasses import dataclass


@dataclass
class Confg:
    upload_folder: str
    backend_url: str


def load() -> Confg:
    return Confg(
        upload_folder=os.environ['UPLOAD_FOLDER'],
        backend_url=os.environ['BACKEND_URL'],
    )


conf = load()

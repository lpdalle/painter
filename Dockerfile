FROM python:3.10.9

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN pip install cython

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:$PATH"

RUN pip install rudalle

RUN pip install httpx

COPY painter /app/painter

CMD ["python", "-m", "painter"]

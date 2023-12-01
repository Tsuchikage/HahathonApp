FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/server/requirements.txt

RUN apt-get update && \
    apt-get install -y netcat-traditional && \
    rm -rf /var/lib/apt/lists/*

COPY ./alembic.ini /app/alembic.ini

COPY ./start.sh /app/start.sh

COPY ./src /app/server/src

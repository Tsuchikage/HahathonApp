FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/server/requirements.txt
COPY ./alembic.ini /app/server/alembic.ini

RUN pip install --no-cache-dir --upgrade -r /app/server/requirements.txt

COPY ./src /app/server/src
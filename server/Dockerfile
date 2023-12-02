FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/server/requirements.txt

RUN pip install -r /app/server/requirements.txt

COPY ./alembic.ini /app/alembic.ini

COPY ./src /app/server/src

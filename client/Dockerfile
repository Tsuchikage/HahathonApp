FROM node:18-alpine

WORKDIR /app

COPY ./src .

RUN npm ci

RUN npm run build
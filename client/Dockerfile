FROM node:18-alpine
RUN apk add --no-cache libc6-compat
WORKDIR /app

COPY ./src .

RUN npm ci

ENV NODE_ENV production
ENV NEXT_TELEMETRY_DISABLED 1

RUN npm run build
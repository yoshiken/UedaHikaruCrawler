FROM python:3.6.5-alpine

RUN apk add --no-cache --update \
        curl \
        bash \
        build-base \
        ca-certificates \
        git \
        bzip2-dev \
        linux-headers \
        ncurses-dev \
        openssl \
        openssl-dev \
        readline-dev \
        sqlite-dev

RUN update-ca-certificates
RUN rm -rf /var/cache/apk/*

COPY . /app
WORKDIR /app

RUN pip install -r /app/requirements-dev.txt

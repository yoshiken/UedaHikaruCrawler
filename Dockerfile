FROM python:3.6.5-alpine

RUN apk update && \
    apk upgrade && \
    apk add --no-cache --update \
        curl \
        bash \
        build-base \
        ca-certificates \
        git \
        bzip2-dev \
        linux-headers \
        ncurses-dev \
        openssl \
        readline-dev \
        sqlite-dev \
        libxml2-dev \
        libxslt-dev \
        libpq \
        postgresql-dev


RUN update-ca-certificates &&\
    rm -rf /var/cache/apk/*

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip &&\
    pip install --upgrade setuptools &&\
    pip install -r /app/requirements-dev.txt
CMD /bin/bash

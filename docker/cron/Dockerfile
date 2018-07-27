FROM python:3.6.5-alpine

RUN apk update && \
    apk upgrade && \
    apk add --no-cache --update \
        bash \
        build-base \
        ca-certificates \
        git \
        bash \
        libpq \
        postgresql-dev \
        libxml2-dev \
        libxslt-dev

RUN update-ca-certificates &&\
    rm -rf /var/cache/apk/*

COPY requirements-dev.txt .

RUN pip install --upgrade pip &&\
    pip install --upgrade setuptools &&\
    pip install -r requirements-dev.txt

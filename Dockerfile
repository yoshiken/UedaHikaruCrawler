FROM python:3.6.5-alpine

RUN apk update && \
    apk upgrade && \
    apk add --no-cache --update \
        tzdata \
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


RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata


RUN update-ca-certificates &&\
    rm -rf /var/cache/apk/*

COPY requirements-dev.txt .

RUN pip install --upgrade pip &&\
    pip install --upgrade setuptools &&\
    pip install -r requirements-dev.txt
CMD /bin/bash

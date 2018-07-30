FROM python:3.6.5-alpine

RUN apk update && \
    apk upgrade && \
    apk add --no-cache --update \
        tzdata \
        bash \
        build-base \
        ca-certificates \
        git \
        bash \
        libpq \
        postgresql-dev \
        libxml2-dev \
        libxslt-dev \
        apk-cron \
        postgresql-client

RUN update-ca-certificates &&\
    rm -rf /var/cache/apk/*

RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata

COPY requirements-dev.txt .

RUN pip install --upgrade pip &&\
    pip install --upgrade setuptools &&\
    pip install -r requirements-dev.txt

COPY ./crontab /var/spool/cron/crontabs/root
COPY ./wait_postgres.sh .


CMD ["sh", "./wait_postgres.sh"]

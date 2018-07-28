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
        libxslt-dev \
        apk-cron

RUN update-ca-certificates &&\
    rm -rf /var/cache/apk/*

COPY requirements-dev.txt .

RUN pip install --upgrade pip &&\
    pip install --upgrade setuptools &&\
    pip install -r requirements-dev.txt

COPY ./crontab /var/spool/cron/crontabs/root


CMD ["crond", "-l", "2", "-f"]

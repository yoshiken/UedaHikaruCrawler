FROM postgres:11-alpine

RUN apk update && \
    apk upgrade && \
    apk add --no-cache --update \
    tzdata

RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata

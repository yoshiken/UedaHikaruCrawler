#!/bin/sh

echo "Waiting for Posgresql"
until psql &> /dev/null
do
        >$2 echo -n "."
        sleep 1
done

>&2 echo "Posgresql is up - executing command"

echo "start web"

cd /app/src
uwsgi --ini /app/docker/web/uwsgi.ini

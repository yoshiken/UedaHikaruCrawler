#!/bin/sh

echo "Waiting for Posgresql"
until psql &> /dev/null
do
        >$2 echo -n "."
        sleep 1
done

>&2 echo "Posgresql is up - executing command"

echo "start api"

cd api
gunicorn --bind 0.0.0.0:3032 main:app --worker-class sanic.worker.GunicornWorker

#!/bin/sh

if [ ! -d log/cron ]
echo "Waiting for Posgresql"
until psql &> /dev/null
do
        >$2 echo -n "."
        sleep 1
done

>&2 echo "Posgresql is up - executing command"

echo "start cron"

cd /app/src
python main.py
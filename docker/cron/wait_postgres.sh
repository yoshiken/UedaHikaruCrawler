#!/bin/sh

if [ ! -d log/cron ]
then
    echo "make dir log/cron"
    mkdir log/cron
fi

echo "Waiting for Posgresql"
until psql &> /dev/null
do
        >$2 echo -n "."
        sleep 1
done

>&2 echo "Posgresql is up - executing command"

echo "start cron"
crond -l 2 -f

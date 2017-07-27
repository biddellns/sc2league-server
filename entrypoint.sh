#!/bin/sh

while ! nc -z db 5432; do sleep 3; done

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --clear --no-input

exec gunicorn config.wsgi:application \
    --name sc2league-server \
    --bind 0.0.0.0:8000 \
    --workers 3 \

exec "$@"

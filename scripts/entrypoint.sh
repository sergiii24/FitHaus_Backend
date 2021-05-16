#!/bin/sh

set -e

python manage.py makemigrations users trainings routines programs PredefinedRoutine objectives exercises CustomRoutine colections classes categories activities

python manage.py migrate --run-syncdb

python manage.py collectstatic --noinput

uwsgi --socket :8000 --master --enable-threads --module fithaus.wsgi

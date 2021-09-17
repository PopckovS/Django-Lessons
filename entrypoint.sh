#! /bin/bash

python3 manage.py makemigrations --no-input

python3 manage.py migrate --no-input

#python3 manage.py runserver 0.0.0.0:8000
exec gunicorn prod.wsgi:application -b 0.0.0.0:8000 --reload

#!/bin/bash
trap 'exit' ERR

./wait-for-it.sh -t 15 postgres:5432
./wait-for-it.sh -t 15 rabbitmq:5672

python manage.py migrate
python manage.py runserver 0.0.0.0:8000

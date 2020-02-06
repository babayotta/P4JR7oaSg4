#!/bin/bash
trap 'exit' ERR

./wait-for-it.sh -t 15 rabbitmq:5672
./wait-for-it.sh -t 15 redis:6379
./wait-for-it.sh -t 15 django:8000

celery -A test_task worker -l info

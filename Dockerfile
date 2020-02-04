FROM python:3

WORKDIR /usr/src/test_task
RUN mkdir -p ./images
COPY dashboard ./dashboard
COPY test_task ./test_task
COPY manage.py .
COPY wait-for-it.sh .
COPY requirements.txt .

RUN pip install -U pip
RUN pip install -Ur requirements.txt

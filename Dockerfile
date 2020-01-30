FROM python:3

RUN mkdir -p /usr/src/test_task
WORKDIR /usr/src/test_task
COPY requirements.txt .

RUN pip install -U pip
RUN pip install -Ur requirements.txt

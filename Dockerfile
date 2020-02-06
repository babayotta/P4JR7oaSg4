FROM python:3

WORKDIR /usr/src/test_task

COPY requirements.txt .
RUN pip install -U pip
RUN pip install -Ur requirements.txt

RUN mkdir -p ./media/images
COPY . .

CMD django_start.sh

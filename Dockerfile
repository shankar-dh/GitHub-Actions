FROM python:3.10-alpine

RUN mkdir /lab1
WORKDIR /lab1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

LABEL maintainer="Dheeraj <jadheeraj.inbox@gmail.com>" \version="1.0"


CMD python run --host=localhost --port=5000

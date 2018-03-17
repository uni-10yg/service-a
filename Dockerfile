FROM python:3.6-alpine

ARG BUILD_NUM

RUN mkdir /service

WORKDIR /service

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT python service.py
FROM python:3.6-alpine

ARG BUILD_NUM

RUN mkdir /service

WORKDIR /service

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
EXPOSE 6000

ENTRYPOINT python service.py
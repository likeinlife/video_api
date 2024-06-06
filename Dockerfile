FROM python:3.10.14-alpine3.20

WORKDIR /opt/app

RUN apk add curl

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./video_api .

RUN chmod +x ./api-docker-entrypoint.sh

ENTRYPOINT ./docker-entrypoint.sh
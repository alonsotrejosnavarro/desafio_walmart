FROM alpine:3.7
FROM python:2.7

WORKDIR /var/www
ADD . /var/www

RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt


FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

WORKDIR /var/www
ADD . /var/www

RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN apt-get install python3-distutils
RUN pip install -r /var/www/requirements.txt


FROM alpine:3.4
#FROM python:3.8-slim

WORKDIR /app
ADD . /app
RUN apk add --update python py-pip
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /app/app/static
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
CMD ["gunicorn","-b","0.0.0.0","app:app"]	


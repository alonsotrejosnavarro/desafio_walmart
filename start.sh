#!/bin/bash
app="flask/wal"
docker build -t ${app} .
sudo docker run -p 8003:8003 flask/wal

#docker run -d -p 56735:80 \
#  --name=${app} \
#  -v $PWD:/app ${app}

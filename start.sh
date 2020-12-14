#!/bin/bash
app="docker.walmart"
docker build -t ${app} .
#sudo docker run -d -p 8003:80  flask/wal

#docker run -d -p 56735:80 \
#  --name=${app} \
#  -v $PWD:/app ${app}

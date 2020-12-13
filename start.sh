#!/bin/bash
app="docker.walmart"
docker build -t ${app} .
docker run -d -p 56735:80 \
  --name=${app} \
  -v $PWD:/app ${app}

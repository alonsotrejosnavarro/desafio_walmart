Crear el contenedor:
docker build -t flask/wal .

Correr el proyecto en local:
En el DockerFile descomentar la última línea del archivo (CMD gunicorn -b 0.0.0.0:8003 app:app)
y luego comentar la linea redundante. Lo importante de esto es que heroku necesita setear el puerto como $PORT debido a que 
cambia en cada deploy.

Luego correr docker run -p 8003:8003 flask/wal

Correr proyecto en heroku:
heroku container:push web
heroku container:release web

Se accede desde la url http://serene-crag-46640.herokuapp.com/


from os import environ
from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=int(environ.get("PORT","8000")))

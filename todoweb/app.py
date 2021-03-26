from todo import app
from os import environ

if __name__ == '__main__':

    HOST = environ.get('SERVERHOST', 'localhost')

    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000

    app.run(HOST, PORT)
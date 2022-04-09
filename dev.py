from app import app
from livereload import Server

if __name__ == '__main__':
    server = server(app.wsgi_app)
    server.serve()
import configparser
import threading
import requests
import argparse

from flask import Flask, request

class Server:

    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.app = Flask(__name__)
        self.app.add_url_rule('/shutdown', view_func=self.shutdown)
        self.app.add_url_rule('/', view_func=self.get_home)
        self.app.add_url_rule('/home', view_func=self.get_home)

    def run_server(self):
        self.server = threading.Thread(target=self.app.run, kwargs={'host': self.host, 'port': self.port})
        self.server.start()
        return self.server

    def shutdown_server(self):
        request.get(f'http://{self.host}:{self.port}/shutdown')


    def shutdown(self):
        terminate_func = request.environ.get('werkzeug.server.shutdown')
        if terminate_func:
            terminate_func()


    def get_home(self):
        return 'Hello server'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, dest='config_file')

    args = parser.parse_args()


    config = configparser.ConfigParser()
    config.read(args.config_file)

    server_host = config['Server']['SERVER_HOST']
    server_port = config['Server']['SERVER_PORT']

    server = Server(host=server_host, port=server_port)

    server.run_server()
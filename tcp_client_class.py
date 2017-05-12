import socket
import time


class Client(object):

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_server(self, address, port):
        self.sock.connect((address, port))

    def send_data(self, data):
        self.sock.send(data)

    def recv_data(self):
        data = self.sock.recv(12)
        print data

    def close_client(self):
        self.sock.close()

if __name__ == '__main__':
    client = Client()
    client.connect_server('localhost', 8001)
    while True:
        client.send_data('hello server')
        client.recv_data()
    client.close_client()
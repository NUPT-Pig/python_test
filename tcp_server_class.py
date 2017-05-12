import socket
import thread


class Server(object):

    def __init__(self, address, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((address, port))

    def handle(self, client_sock, client_address):
        try:
            client_sock.settimeout(50)
            while True:
                buf = client_sock.recv(1024)
                print buf
                client_sock.send(buf)
        except Exception as e:
            print ('handle except %s' % str(e))
        client_sock.close()

    def start(self):
        self.sock.listen(5)
        while True:
            client_sock, client_address = self.sock.accept()
            thread.start_new_thread(self.handle, (client_sock, client_address))
            #self.handle(client_sock, client_address)

    def close(self):
        self.sock.close()


if __name__ == '__main__':
    server = Server('localhost', 8001)
    server.start()
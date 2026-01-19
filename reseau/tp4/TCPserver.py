#!/usr/bin/python3

import socket
from threading import Thread
from threading import Lock

class Server:
    def __init__(self):
        self.counter = 0
        self.lock = Lock()

    def mainServer(self, port):
        # tcp par default
        sock = socket.socket()
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("0.0.0.0", port))
        # active le socket pour accépter des connexions
        sock.listen(10)

        while True:
            cli, addr = sock.accept()
            sess = Session(self, cli, addr)
            sess.start()


class Session(Thread):
    def __init__(self, server, sock, addr):
        Thread.__init__(self)
        self.server = server
        self.socket = sock
        self.file = sock.makefile(mode="rw")
        self.addr = addr

    def run(self):
        while True:
            line = self.file.readline().strip()
            print(line)

            if line == "get":
                self.file.write(f"val {self.server.counter}\n")
                self.file.flush()
            
            print(line.split())
            if len(line.split()) == 2:
                command, nbre = line.split()
                if command == "incr":
                    self.server.lock.acquire()
                    self.server.counter+=int(nbre)
                    self.server.lock.release()
                    self.file.write(f"new val {self.server.counter}\n")
                    self.file.flush()

            elif line == "quit":
                self.file.write("quit\n")
                self.file.flush()
                break

            else:
                self.file.write("je connais ton adresse " + str(self.addr) + " mouhahahaha\n")
                self.file.flush()

        self.file.close()
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()


Server().mainServer(5556)

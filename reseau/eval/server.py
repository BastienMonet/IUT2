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
        self.liste_taches = {}
        sock = socket.socket()
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("0.0.0.0", port))
        # active le socket pour accépter des connexions
        sock.listen(10)

        while True:
            cli, addr = sock.accept()
            sess = Session(self, cli, addr, self)
            sess.start()


class Session(Thread):
    def __init__(self, server, sock, addr, serv):
        Thread.__init__(self)
        self.server = server
        self.socket = sock
        self.file = sock.makefile(mode="rw")
        self.addr = addr
        self.serv = serv

    def send(self, message):
        self.file.write(message)
        self.file.write("\n")
        self.file.flush()

    def run(self):
        while True:
            line = self.file.readline().strip().split()
            if len(line) > 0:
                command = line[0]
                command = command.upper()
            else:
                self.send("commande invalide")
            print(line)

            match command:
                case "CREER":
                    if len(line) >= 2:
                        with self.serv.lock:
                            if line[1] not in self.serv.liste_taches:
                                self.serv.liste_taches[line[1]] = []
                                message = f"OK"
                                self.send(message)
                            else:
                                self.send(f"ERR")
                    else:
                        self.send("il vous manque des parametres")
                case "TACHE":
                    if (len(line)) >= 3:
                        with self.serv.lock:
                            if line[1] in self.serv.liste_taches:
                                self.serv.liste_taches[line[1]].append(line[2])
                                self.send("OK")
                            else:
                                self.send("ERR")
                    else:
                        self.send("il vous manque des parametres")
                case "TERMINE":
                    if (len(line)) >= 3:
                        with self.serv.lock:
                            if line[1] in self.serv.liste_taches and line[2] in self.serv.liste_taches[line[1]]:
                                self.serv.liste_taches[line[1]].remove(line[2])
                                self.send("OK")
                            else:
                                self.send("ERR")
                    else:
                        self.send("il vous manque des parametres")
                case "PROGRESSION":
                    if (len(line)) >= 3:
                        with self.serv.lock:
                            if line[1] in self.serv.liste_taches and line[2] in self.serv.liste_taches:
                                if len(self.serv.liste_taches[line[1]]) >= len(self.serv.liste_taches[line[2]]):
                                    util = line[1]
                                else:
                                    util = line[2]
                                self.send(f"OCCUPE {util}")
                            else:
                                self.send("ERR")
                    else:
                        self.send("il vous manque des parametres")
                case "VIDER":
                    if (len(line)) >= 2:
                        with self.serv.lock:
                            if line[1] in self.serv.liste_taches:
                                self.serv.liste_taches[line[1]]= []
                                self.send("OK")
                            else:
                                self.send("ERR")
                    else:
                        self.send("il vous manque des parametres")


                case "QUIT":
                    self.send("QUIT")
                    break

                case _:
                    message = f"commande {command} inconnu"
                    self.send(message)
                    
        self.file.close()
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()


Server().mainServer(5555)


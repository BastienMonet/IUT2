#!/usr/bin/python3

import socket

def client(host, port):
    sock = socket.socket()
    sock.connect((host, port))

    f = sock.makefile(mode="rw")
    while True:
        a = input(">  ") 
        f.write(a + "\n")
        f.flush()
        res = f.readline()
        print(res)
        if a == "QUIT" :
            break


    # Fermeture
    f.close()
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

client("localhost", 5555)

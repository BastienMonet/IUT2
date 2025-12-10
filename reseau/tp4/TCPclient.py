#!/usr/bin/python3

import socket

def client(host, port):
    sock = socket.socket()
    sock.connect((host, port))

    f = sock.makefile(mode="rw")
    f.write("")
    f.flush()
    while True:
        a = input("veuillez rentrer une valeur\n") 
        f.write(a + "\n")
        f.flush()
        if a == "quit" :
            break
        print(f.readline())

    # Fermeture
    f.close()
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

client("localhost", 5556)

# "localhost"

# 

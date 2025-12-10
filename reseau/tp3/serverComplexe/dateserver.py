
import socket
import os

import datetime
BUFSIZE = 1024
def server(port):
    # protocol sock_dgram = UDP
    sock = socket.socket(type=socket.SOCK_DGRAM)
    # 0.0.0.0 -> bind a l'ip de la machine
    sock.bind(("0.0.0.0", port))
    while True:
        # on alloue 1024 octet de donnée a receptionner
        data, addr = sock.recvfrom(BUFSIZE)
        if data.decode() == "date":
            data = datetime.datetime.now()
            data = "%s\n" % data
        else:
            data = "%s\n" % ("numero de carte bancaire : 18 91")
        sock.sendto(data.encode(), addr)
server(5556)
import socket
import sys
import time

BUFSIZE = 1024
def client (host, port, request):
    sock = socket.socket(type=socket.SOCK_DGRAM)
    addr = (host, port)
    sock.sendto(request.encode(), addr)
    data = sock.recv(BUFSIZE)
    print(data.decode(), end="")
    time.sleep(1000000)
    
client(sys.argv[1], 5556, sys.argv[2])
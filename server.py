# UDPPingerServer.py

from random import randint
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 55200))

print("sucesso")
while True:


    message, address = serverSocket.recvfrom(1024)

    if randint(0, 10) < 4:
        continue

    serverSocket.sendto(message, address)

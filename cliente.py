from socket import *
from datetime import datetime


serverName = 'localhost'
serverPort = 55200

#cria um socket cliente. o primeiro parametro indica que o endereço é o IPv4. o segundo indica que é UDP
#se a porta não é especificada, o SO escolhe uma aleatória
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
ping = 1


while ping <= 10:
  
    message = 'Ping'
    try:   
        clientSocket.sendto(message.encode(),(serverName, serverPort))
        hsend = datetime.now()
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        hrecv = datetime.now()
        rtt = hrecv - hsend
        msg = modifiedMessage.decode()
        print(msg, ping, hsend,' RTT->', rtt)

    except timeout: 
        print('Solicitação expirada')

    ping += 1


clientSocket.close()

    

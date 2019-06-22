# Simulação de Ping com UDP

Este repositório contém um cliente e um servidor UDP, em **Python**. Simulando uma perda de 40% dos pacotes e mostrando o RTT (Round Trip Time).

# Cliente

O cliente simula um envio de 10 pacotes para um determinado servidor, já estabelecido, e com o **time out** de espera por uma reposta do servidor de apenas 1 segundo. 

# Servidor

O servidor recebe uma mensagem do cliente e simula uma perca de 40% dos pacotes (mensagens) e devolve a mensagem para o cliente. O servidor está com uma porta e IP fixo, porém pode ser alterado.

## Executando

Para rodar o servidor:
`python server.py`

Para rodar o cliente:
`python cliente.py`



## Exemplo de saída 

![Exemplo](https://github.com/RonierLima/UDP_Pinger-RTT/blob/master/funcionando.png)

```


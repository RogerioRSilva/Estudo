# script para sniffer
# import socket
# import os
#
# host = "192.168.0.14"  # este é o IP do meu host, o computador alvo que será escaneado
#
# # cria o socket
# if os.name == "nt":
#     socket_protocol = socket.IPPROTO_IP  # verifica se o protocolo é endereço IP ou ICMP
# else:
#     socket_protocol = socket.IPPROTO_ICMP
#
# sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
#
# sniffer.bind((host, 0))  # aguarda o host
#
# sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)  # captura os cabeçalhos IP dos pacotes
#
# if os.name == "nt":
#     sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)  # para Windows, habilita o modo promiscuo
#
# print(sniffer.recvfrom(10000))  # recebe o IP do pacote
#
# if os.name == "nt":
#     sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)  # para Windows, desabilita o modo promiscuo

import socket

host = "127.0.0.0"

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)  # considerando só o protocolo IP

sniffer.bind((host, 0))

sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)  # captura o cabeçalho IP dos cabeçalhos

sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)  # Para Windows

while True:
    dados = sniffer.recvfrom(10000)  # recebe o IP do pacote
    print(dados)
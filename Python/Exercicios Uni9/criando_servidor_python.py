import socket
import datetime

host = '127.0.0.1' # O mesmo que localhost
porta = 8800       # Porta da conexão

# Estou usando o TCP/IP
soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
recebe = (host, porta)
soquete.bind(recebe)
soquete.listen(2)

print('\nSERVIDOR INICIADO...IP: ', host, 'PORTA: ', porta)

while True:
    conexao, enderecoIP = soquete.accept()
    print('\nSERVIDOR ACESSADO PELO CLIENTE: ', enderecoIP, datetime.datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))

    while True:
        mensagem = conexao.recv(2048)
        if not mensagem:
            break
        print('\nIP CLIENTE:', enderecoIP)
        print('MENSAGEM RECEBIDA: ', mensagem.decode())

    print('CONEXÃO COM O CLIENTE FINALIZADA...', enderecoIP, 'EM:', datetime.datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
    conexao.close()
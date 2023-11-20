import socket

host = '127.0.0.1'
porta = 8800

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
envio = (host, porta)
soquete.connect(envio)

print('Digite: S e pressione ENTER para encerrar...')
print('DIGITE A MENSAGEM: ')
mensagem = input()

while mensagem not in ('s', 'S'):
    soquete.send(str(mensagem).encode())
    mensagem = input()

soquete.close()
import socket

host = '127.0.0.1'
port = 5050
HEADERSIZE = 10

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.setblocking(False)

while True:
    MSG = str(input('>>> '))

    if MSG:
        message = bytes(f"{len(MSG):<{HEADERSIZE}}"+MSG, 'utf-8')
        send = client.send(message)

    else:
        print('Not Send')

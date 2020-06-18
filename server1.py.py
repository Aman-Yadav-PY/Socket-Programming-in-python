import socket
import select

HEADERSIZE = 10

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 5050))
server.listen()

sockets = [server]

def reciever(client_socket):
	Header = client_socket.recv(HEADERSIZE)
	msglength = int(Header.decode('utf-8').strip())

	MSG = client_socket.recv(msglength)
	message = MSG.decode('utf-8')

	if len(message) == msglength:
		return message

	else:
		return False

result = True
while True:
	rlist, _, xlist = select.select(sockets, [], sockets)

	try:
		if result:
			for all_sockets in rlist:
					if all_sockets == server:
						clientsocket, address = server.accept()
						print(f'Connection with {address} has been established!')
						sockets.append(clientsocket)
						result = False

		while True:
			for notified_sockets in rlist:
				if notified_sockets != server:
					message = f'From {address[0]}: '+reciever(notified_sockets)
					print(message)
				else:
					print('NOT A CLIENTSOCKET')

			break

	except Exception as e:
		print(e)





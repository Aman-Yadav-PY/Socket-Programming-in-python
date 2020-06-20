import socket
import select

HEADERSIZE = 10
host = '127.0.0.1'
port = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))

# listening to clients
server.listen()

sockets = [server]

# create function for reciving message from client
def reciever(client_socket):
	# first retrive message length from client
	header = client_socket.recv(HEADERSIZE)

	# get integer for message length
	messagelength = int(header.decode('utf-8').strip())

	if messagelength:
		message = client_socket.recv(messagelength)
		msg = message.decode('utf-8')
		# completemessage = f'{address}: {msg}'
		return msg
	else:
		False


def sender(client_socket, addr):
	try:

		while True:
			message = str(input(f'To [{addr[1]}] : '))
			if client_socket.fileno() != -1:
				MSG = bytes(f"{len(message):<{HEADERSIZE}}"+message, 'utf-8')
				client_socket.send(MSG)

			else:
				print("[CLOSED]")
			break


	except Exception as e:
		print(e)


run = True
while True:
	# creating select object
	rlist, _, xlist = select.select(sockets, [], sockets)

	try:

		
		for client in rlist:
			if client == server:
				# Establishing connection with client
				clientsocket, address = client.accept()

				#appending clientsocket to sockets
				sockets.append(clientsocket)
				run = False

		while True:
			for connect in rlist:
				if connect != server:

					# retriving message from client
					message = reciever(connect)
					print(f"From [{address[1]}] : {message}")
			break

		# for sending message
		for connections in rlist:
			if connections == clientsocket:
				clientsocket.setblocking(False)
				sender(connections, address)



	except Exception as e:
		print(f"terminating as [{e}]")
		quit()
		break

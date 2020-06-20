import socket
import tkinter

# creating some constants
HEADERSIZE = 10
host = '127.0.0.1'
port = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connecting with server
client.connect((host, port))
client.setblocking(False)

while True:
	try:
		MSG = str(input(' >> '))

		if MSG:
			# sending message
			message = bytes(f"{len(MSG):<10}"+MSG, 'utf-8')
			sender = client.send(message)
		else:
			print('[404]')

		client.setblocking(True)

		# header
		header = client.recv(HEADERSIZE)
		msglength = int(header.decode('utf-8').strip())

		# recieving complete message 
		reciever = client.recv(msglength)
		recieved =reciever.decode('utf-8')

		# recieving message from ther host
		complete_message = f" <<< {recieved}"

		print(complete_message)
		client.setblocking(False)
	except Exception as e:
		print(e)
		quit()


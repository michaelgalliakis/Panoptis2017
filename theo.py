import socket
import fileinput

TCP_IP = '83.212.65.250'
TCP_PORT = 50123
BUFFER_SIZE = 2048

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

for line in fileinput.input():
	s.send(line)
	pass
	
s.close()

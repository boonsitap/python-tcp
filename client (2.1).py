import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5011
BUFFER_SIZE = 1024
num = '7'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(num)

numRtn = s.recv(BUFFER_SIZE)
s.close()

print "Received Result from Server:", numRtn

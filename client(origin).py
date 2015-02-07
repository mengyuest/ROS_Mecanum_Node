import socket

ECHO_SERVER_ADDRESS = "192.168.2.10"
ECHO_PORT = 7

while(1):
	print "Tinker#",
	cmd = raw_input()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
	s.connect((ECHO_SERVER_ADDRESS, ECHO_PORT))
	s.sendall(cmd)
	data = s.recv(1024)
	print str(data)
	s.close()

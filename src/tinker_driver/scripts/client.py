import socket

def send(cmd):
#def start():
    ECHO_SERVER_ADDRESS = "192.168.2.10"
    ECHO_PORT = 7

#def send(cmd):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.connect((ECHO_SERVER_ADDRESS, ECHO_PORT))
    s.settimeout(5)
    s.sendall(cmd)
    data = s.recv(1024)
    s.close()
   # print(type(data))
   # if(data == ''):
   #     print("on no !")
   #     return '0'
    return data

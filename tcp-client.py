import socket
import time

IP = input('Server address: ')
TCP_PORT = 5005
BUFFER_SIZE = 1024

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK.stream)
    s.connect((IP, TCP_PORT))
    MESSAGE = input('write to server : ')
    if(MESSAGE== 'q'):
        break
    
    s.send(MESSAGE.decode('utf-8'))
    print('sending_data:', MESSAGE)
    data = s.recv(BUFFER_SIZE)
    print('Data from server:', data.decode('utf-8'))
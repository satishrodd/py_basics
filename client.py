import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sock.connect(('127.0.0.1', 12345)))

while(1):
    str = raw_input()
    sock.sendall(str)
    print(sock.recv(512))
sock.close()
    

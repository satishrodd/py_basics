import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 12345))
sock.listen(1)
conn, addr = sock.accept()
print('connected to:', addr)
while 1:
    data = conn.recv(512)
    if not data: break
    conn.sendall(data)
conn.close()



import socket

def tcp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 12345))
    sock.listen(2)
    conn, addr = sock.accept()
    print('connected to:', addr)
    while True:
        data = conn.recv(512)
        if not data: break
        conn.sendall(data)
    conn.close()

def udp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 12345))
    while True:
        data, addr = sock.recvfrom(512)
        if not data: break
        sock.sendto(data, addr)
    conn.close()


tcp_server()
#udp_server()



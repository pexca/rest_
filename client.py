import socket

# создаём клиентский сокет, совместимый с серверным
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server: send some info packs to server, it responds with info packs if ready
client_sock.connect(('127.0.0.1', 53210))
client_sock.sendall(b'Hello!')  # 'b' coverts string to bytes
data = client_sock.recv(1024)  # receive response from server

client_sock.close()
print('Received: ', repr(data))


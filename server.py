import socket

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
print(type(serv_socket))
print(serv_socket.fileno())  # номер файлового дескриптора, назначенного сокету

serv_socket.bind(('127.0.0.1', 53210))  # пара значений - адрес сокета, хост и порт
serv_socket.listen(10)  # количество входящих соединений, queue, неблокирующий вызов

client_sock, client_address = serv_socket.accept()  # блокирующий вызов

while True:
    # пока клиент не отключился, читаем передаваемые им данные и отправляем их обратно
    data = client_sock.recv(1024)  # size of expected portion of data; returns only a part of it if more
    print('Received: ', data)
    if not data:
        break
    client_sock.sendall(data)

client_sock.close()


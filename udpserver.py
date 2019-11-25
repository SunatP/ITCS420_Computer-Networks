import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 8000))
server.listen(5)

while True:
    print('Waiting for connection . . . ')
    client, address = server.accept()
    print('... connected from:', address)
    data,address = client.recvfrom(1024)
    if data:
        if data.islower():
            client.sendall(data.upper())
        elif data.isupper():
            client.sendall(data.lower())
        elif data.isupper() is True or data.islower() is True:
            client.sendall(data)
        else:
            client.sendall(data)
    client.close()
server.close()


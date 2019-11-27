import socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 8000))

while True:
    # print('... connected from:', server)
    data,address = server.recvfrom(1024)
    if data:
        if data.islower():
            server.sendto(data.upper(),address)
        elif data.isupper():
            server.sendto(data.lower(),address)
        elif data.isupper() is True or data.islower() is True:
            server.sendto(data,address)
        else:
            server.sendto(data,address)
server.close()


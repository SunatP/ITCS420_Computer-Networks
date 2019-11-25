import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 8880))  # 8880 can change to any number
server.listen(5)

while True:
    print('Waiting for connection . . .')
    client, address = server.accept()
    print('... connected from:', address)
    data = client.recv(1024)
    dat = data.upper()
    header=('HTTP/1.1 200 OK\n')
    content=('Content-Type: text/html\n')
    body=("""
			<html>
			<body>
			<h3>HELLO EVERYONE!</h3>
			</body>
			</html>
			""")
    if data:
        client.sendall(header.encode('utf-8'))
        client.sendall(content.encode('utf-8'))
        client.sendall(body.encode('utf-8'))
    client.close()
server.close()

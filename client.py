import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
client.connect(('localhost',13245))

text = raw_input('Client Ready to Input \n') # simple for input text
client.send(text)
print client.recv(1024)

client.close()

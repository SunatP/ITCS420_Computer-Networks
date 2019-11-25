import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
client.connect(('localhost',8000))
text = ""
while True:
    text = input('Client Ready to Input \n') # simple for input text
    break

client.sendall(text.encode('utf-8'))
t = time.localtime(time.time())
print ("Result: ",client.recv(1024).decode('utf-8'))
print("Current Time: ",time.asctime(t))
client.close()

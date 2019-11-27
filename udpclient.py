import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
client.connect(('localhost',8000))
text = ""
while True:
    text = input('Client Ready to Input \n') # simple for input text
    break

client.sendto(text.encode('utf-8'), ('localhost',8000))
t = time.localtime(time.time())
a = client.recv(1024).decode('utf-8')
print ("Result: ",a)
print("Current Time: ",time.asctime(t))
client.close()

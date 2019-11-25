# Lab 5 ITCS420 Computer Networks 

## Part 2 Socket programming by Python

### เราต้องทำอะไรบ้าง

    1. Create a ​tcpserver.py​ and ​tcpclient.py​ with a server port ​12345
      - Client gets the message from the user input (keyboard) and sends to theserver. (while loop will be used)
      - Once Server receives message(s), then it will change the string to uppercaseor lowercase and send the message back
      - When the client received the message back, it will print out the current timein the asctime() format.
      - Do with your localhost or with your partner: one is server, one is client
      - Submit both the screen output of server and client, and also the source codesin the mycourse website.


    2. Change your Python programs from the previous task to support ​UDP​, and callthem as ​udpserver.py​ and ​udpclient.py​ with the server port of 8000
      - Do within your localhost or with your partner’s computer: one is server, oneis client
      - Submit both the screen output of server and client, and also the source codesin the mycourse website.


    3. Create a dummy HTTP server and name it as ​dummyhttp.py
      - Listen to port ​xxxx​ and if HTTP GET request arrives, the server returns amessage “HELLO EVERYONE!” (in HTML format)
      - Replace xxxx with the last two digits of your student ID and your partnerstudent ID. (totally 4 digits)
      - When user types in http://localhost:xxxx, the user should see “HELLOEVERYONE” on the page as the response
      - Submit both the screen output of your browser, and also the dummy HTTPserver codes on the mycourse website.

### เริ่มกันที่ข้อ 1.

สร้าง TCPclient.py ขึ้นมา<br> เราต้อง import อะไรบ้าง

```python
import time
import socket
```

เริ่มเขียนต่อ

```python
import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
client.connect(('localhost',12345)) # 12345 คือ port ที่กำหนด
text = ""
"""
Client gets the message from the user input (keyboard) and sends to theserver.
(while loop will be used)
ตรงนี้เราจะเอา While loop มาใช้เพื่อรอ user ป้อนข้อมูลเข้าไป
"""
while True: 
    text = input('Client Ready to Input \n') # simple for input text 
    """
    input ใช้ใน python version 3.X
    input_raw ใช้ใน python version 2.X
    """
    break

client.sendall(text.encode('utf-8')) # ถ้าใช้ python version 3.X จะต้องมีการ encode หรือเข้ารหัสตัวอักษรด้วย
t = time.localtime(time.time())

"""
When the client received the message back, 
it will print out the current timein the asctime() format. 
ตรงนี้จะใช้สำหรับ client เพื่อแสดง result และ เวลาในปัจจุบัน
"""
print ("Result:",client.recv(1024).decode('utf-8')) # ถ้าใช้ python version 3.X จะต้องมีการ decode เพื่อถอดรหัสข้อความด้วย
print("Current Time: ",time.asctime(t)) # asctime() is representing a time as returned by gmtime() or localtime() 
client.close()
```

สร้างไฟล์ tcpserver.py กันต่อ

เราจะอิมพอร์ตแค่ 

```python
import socket
```

เขียนต่อเลยนะ
```python
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 12345))
server.listen(5)


while True:
    print('Waiting for connection . . . ')
    client, address = server.accept()
    print('... connected from:', address)
    data = client.recv(1024)
    if data:
        """
        Once Server receives message(s), 
        then it will change the string 
        to uppercaseor lowercase and send the message back
        ใต้ if data: นี้จะเป็น condition แปลงตัวอักษรจากตัวเล็กไปตัวใหญ่หรือตัวใหญ่ไปตัวเล็กก็ไดเ
        """
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


```

### ต่อกันที่ข้อ 2.

เราเอาโค้ดจากข้อ 1. มาแก้โดยการเปลี่ยน 12345 มาเป็น 8000
<br> เริ่มที่ udpclient.py

```python
import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
client.connect(('localhost',8000)) # จากตอนแรก port 12345 เราจะเปลี่ยนให้เป็น 80000
text = ""
while True:
    text = input('Client Ready to Input \n') # simple for input text
    break

client.sendall(text.encode('utf-8'))
t = time.localtime(time.time())
print ("Result: ",client.recv(1024).decode('utf-8'))
print("Current Time: ",time.asctime(t))
client.close()

```

จบแล้วแค่นี้เลย ต่อกันที่ tcpclient.py

```python
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
```

### ต่อมาที่ข้อสุดท้าย 

เราจะสร้างดัมมี่ขึ้นมาโดยใช้ port หมายเลขอะไรก็ได้ เป็น server ขึ้นมาโดยข้างในจะส่ง html ออกไปแสดงผลที่ localhost:XXXX

```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 8880))  # ตรงเลขนี้สามารถเป็นหมายเลขอะไรก็ได้
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
        client.sendall(header.encode('utf-8')) # ถ้าใช้ python 3.X จะต้องแปลง format เป็น string ก่อนแล้วจึงค่อยเข้ามา encode แบบนี้
        client.sendall(content.encode('utf-8'))
        client.sendall(body.encode('utf-8'))    
    client.close()
server.close()

```
#//socketserver
import socket
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('127.0.0.1',10124))
socket.listen(5)
while True:
    client,addr=socket.accept()
    print("connection established with:",client,addr)
    msg=client.recv(102).decode('utf-8').title()
    print(msg)
    break




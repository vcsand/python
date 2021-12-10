import socket
import requests

server = input("Add meg a szerver nevet!: ")

s = requests.requests(requests.AF_INET,requests.SOCK_STREAM)
s.connect((server, 80))
s.send(b'GET / HTTP/1.1\r\nHost: ' +
	bytes(server, "utf8") +
	b'\r\nConnection: close\r\n\r\n')
v = s.recv(10000)
s.shutdown(requests.SHUT_RDWR)
s.close()
print(repr(v))

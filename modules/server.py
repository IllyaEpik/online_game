import socket
from .main_window import Screen

server_screen = Screen().run()
hostname = socket.gethostname()
server = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
ip = socket.gethostbyname(hostname)
#print(ip)

server.bind((f"{ip}", 8800))
server.listen()
client = server.accept()
data = client[0].recv(1024).decode()

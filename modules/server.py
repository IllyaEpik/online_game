import socket
# from .main_window import Screen

# server_screen = Screen().run()
# server = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(ip)
print(hostname)
# server.bind((f"{ip}", 8800))
# server.listen()
# client = server.accept()
# data = client[0].recv(1024).decode()
